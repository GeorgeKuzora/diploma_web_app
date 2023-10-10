from django.shortcuts import get_object_or_404, render
from .models import Job
from .forms import JobForm
from django.views import View


def index(request):
    job_list = Job.objects.order_by("job_name")
    context = {"job_list": job_list, }
    return render(request, "jobs/index.html", context)


def job_detail(request, job_id):
    job_details = get_object_or_404(Job, pk=job_id)
    context = {"job_details": job_details, }
    return render(request, "jobs/details.html", context)


class JobSearch(View):

    def get(self, request, skill_name=""):
        job_list = Job.objects.order_by("job_name")
        job_form = JobForm()
        if skill_name:
            job_list = Job.objects.filter(skills__skill_name=skill_name)
        context = {"job_list": job_list, "job_form": job_form}
        return render(request, "jobs/search.html", context)

    def post(self, request):
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            job_skill = job_form.cleaned_data["skill"]
            return self.get(request, job_skill)
        return self.get(request)
