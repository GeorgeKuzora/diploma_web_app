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
    if user.is_authenticated and user.is_active:
        profile: Profile = Profile.objects.get(user=user)
        skills = Skill.objects.filter(profile=profile)
        if len(skills) > 0:
            job_list = Job.objects.filter(skills__in=skills).distinct()
        else:
            job_list = Job.objects.all()
    if not job_list:
        job_list = Job.objects.all()

    return {"job_list": job_list, }


def index(request) -> HttpResponse:
    context = get_job_list_from_user_skills(request)
    return render(request, "jobs/index.html", context)


def job_detail(request, job_id):
    job_details = get_object_or_404(Job, pk=job_id)
    context = {"job_details": job_details, }
    return render(request, "jobs/details.html", context)


class JobSearch(View):

    def get(self, request, skill_name=""):
        context = get_job_list_from_user_skills(request)
        job_form = JobForm()
        if skill_name:
            context["job_list"] = Job.objects.filter(skills__skill_name=skill_name)
        context["job_form"] = job_form
        return render(request, "jobs/search.html", context)

    def post(self, request):
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            job_skill = job_form.cleaned_data["skill"]
            return self.get(request, job_skill)
        return self.get(request)
