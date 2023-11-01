"""
Jobs app views
"""
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.views import View

from skills.models import Skill
from users.models import Profile
from .models import Job
from .forms import JobForm


def get_job_list_from_user_skills(request: HttpRequest) -> dict[str, QuerySet]:
    """
    Function to get a list of jobs which have some of user skills as required.

    If user is logged, function will return job list based on skills user has.
    If user isn't logged, function will return job list of all jobs.

    Args:
        request: HttpRequest Http request from user.

    Returns:
        dict[str, QuerySet] Dictionary that contains context of the response.
            contains: job list title as key, Job list QuerySet as value.
    """
    user: User = request.user
    job_list: QuerySet[Job] = Job.objects.all()
    if user and user.is_authenticated and user.is_active:
        try:
            profile: Profile = Profile.objects.get(user=user)
            skills: QuerySet[Skill] | None = Skill.objects.filter(
                profile=profile
            )
        except Profile.DoesNotExist as e:
            skills = None
        if skills and len(skills) > 0:
            job_list = Job.objects.filter(skills__in=skills).distinct()
    return {"job_list": job_list}


def index(request: HttpRequest) -> HttpResponse:
    """
    Function returns HttpResponse for jobs app index url.

    If user is logged, function will return the response
    with  job list based on skills user has.
    If user isn't logged, function will return the response
    with job list of all jobs.

    Args:
        request: HttpRequest Http request from user.

    Returns:
        HttpResponse rendered with jobs/index.html template and context as a
        dictionary.
    """
    context: dict[str, QuerySet] = get_job_list_from_user_skills(request)
    return render(request, "jobs/index.html", context)


def job_detail(request: HttpRequest, job_id: int):
    """
    Function returns HttpResponse for job details page.

    Function will return a HttpResponse with jobs details rendered with
    jobs/details.html template.

    Args:
        request: HttpRequest Http request from user.
        job_id: Id for a job we are looking for.

    Returns:
        HttpResponse rendered with jobs/details.html template and context as a
        dictionary.
    """
    job_details = get_object_or_404(Job, pk=job_id)
    context = {"job_details": job_details, }
    return render(request, "jobs/details.html", context)


class JobSearch(View):
    """
    Class based view for jobs search page.

    This view renders HttpResponse for GET and POST requests from jobs search
    page.
    """

    def get(self, request, search_data={}):
        """
        Function returns HttpResponse for a GET request from jobs search page.

        Function returns a HttpResponse with list of jobs rendered with
        jobs/search.html template.

        Args:
            request: HttpRequest Http request from user.
            search_data: Dictionary that contains search parameters.

        Returns:
            HttpResponse rendered with jobs/search.html template and context
            as a dictionary.
        """
        context = get_job_list_from_user_skills(request)
        job_form = JobForm()
        if search_data:
            context = get_job_list_from_search_form(search_data)
        context["job_form"] = job_form
        return render(request, "jobs/search.html", context)

    def post(self, request):
        """
        Function returns HttpResponse for a POST request from jobs search page.

        Function receives a POST request data from a JobForm.
        Function returns a HttpResponse with list of jobs rendered with
        jobs/search.html template.

        Args:
            request: HttpRequest Http request from user.

        Returns:
            HttpResponse rendered with jobs/search.html template and context
            as a dictionary.
        """
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            search_data = job_form.cleaned_data
            return self.get(request, search_data)
        return self.get(request)


def get_job_list_from_search_form(search_data: dict) -> dict:
    """
    Function to get a list of jobs based of search data argument.

    Function will request a list of Jobs from a database using different
    search filters from search_data argument.

    Args:
        search_data: Dictionary that contains search parameters.

    Returns:
        dict[str, QuerySet] Dictionary that contains:
            job_list title string as a key, Job list QuerySet as a value.
    """
    job_list: QuerySet[Job] = Job.objects.filter(is_archived=False)
    skills: str | None = search_data.get("skills", None)
    if skills:
        skills = skills.split(" ")
        job_list = job_list.filter(skills__skill_name__in=skills)
    salary = search_data.get("salary", None)
    if salary:
        job_list = job_list.filter(min_salary__lte=salary)
        job_list = job_list.filter(max_salary__gte=salary)
    company = search_data.get("company", None)
    if company:
        job_list = job_list.filter(company__icontains=company)
    pub_date = search_data.get("pub_date", None)
    if pub_date:
        job_list = job_list.filter(pub_date__gte=pub_date)
    country = search_data.get("country", None)
    if country:
        job_list = job_list.filter(address__country=pub_date)
    required_experience = search_data.get("required_experience", None)
    if required_experience:
        job_list = job_list.filter(required_experience=required_experience)

    return {"job_list": job_list}
