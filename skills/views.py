from django.shortcuts import get_object_or_404, render
from .models import Skill


def index(request):
    skill_list = Skill.objects.order_by("skill_name")
    context = {"skill_list": skill_list, }
    return render(request, "skills/index.html", context)


def detail(request, skill_id):
    skill_details = get_object_or_404(Skill, pk=skill_id)
    context = {"skill_details": skill_details, }
    return render(request, "skills/details.html", context)
