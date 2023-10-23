from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from skills.models import Skill

from users.models import Profile
from .models import Job
from .forms import JobForm
from django.views import View


def get_job_list_from_user_skills(request) -> dict:
    user: User = request.user
    job_list: QuerySet[Job] | None = None
    if user.is_anonymous or not user.is_active:
        job_list = Job.objects.all()
    elif user.is_authenticated and user.is_active and user:
        try:
            profile: Profile = Profile.objects.get(user=user)
            skills = Skill.objects.filter(profile=profile)
        except Profile.DoesNotExist as e:
            skills = []
        if len(skills) > 0:
            job_list = Job.objects.filter(skills__in=skills).distinct()
        else:
            job_list = Job.objects.all()
    if not job_list:
        job_list = Job.objects.all()

    return {"job_list": job_list}


def index(request) -> HttpResponse:
    context = get_job_list_from_user_skills(request)
    return render(request, "jobs/index.html", context)


def job_detail(request, job_id):
    job_details = get_object_or_404(Job, pk=job_id)
    context = {"job_details": job_details, }
    return render(request, "jobs/details.html", context)


class JobSearch(View):

    def get(self, request, search_data={}):
        context = get_job_list_from_user_skills(request)
        job_form = JobForm()
        if search_data:
            context = get_job_list_from_search_form(search_data)
        context["job_form"] = job_form
        return render(request, "jobs/search.html", context)

    def post(self, request):
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            search_data = job_form.cleaned_data
            print(search_data)
            return self.get(request, search_data)
        return self.get(request)


def get_job_list_from_search_form(search_data: dict) -> dict:
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
