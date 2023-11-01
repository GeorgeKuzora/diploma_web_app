"""
Views for pages related to skills app.

Contains views:
    index - List of all skills.
    detail - Details for a particular skill.
"""
from django.shortcuts import get_object_or_404, render
from .models import Skill


def index(request):
    """
    List of all skills.

    Skills ordered by skill name.

    Args:
        request: HttpRequest request from a client.

    Returns:
        HttpResponse List of all skills rendered with
            skills/index.html template.
    """
    skill_list = Skill.objects.order_by("skill_name")
    context = {"skill_list": skill_list, }
    return render(request, "skills/index.html", context)


def detail(request, skill_id):
    """
    Details for a particular skill.

    Skill with all it's fields.

    Args:
        request: HttpRequest request from a client.
        skill_id: int id value for a particular skill.

    Returns:
        HttpResponse Skill details rendered with
            skills/details.html template.
    """
    skill_details = get_object_or_404(Skill, pk=skill_id)
    context = {"skill_details": skill_details, }
    return render(request, "skills/details.html", context)
