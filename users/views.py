from django.shortcuts import render
from .forms import UserAuthForm


def login_view(request):
    auth_form = UserAuthForm()
    context = {"form": auth_form}
    return render(request, "users/login.html", context=context)
