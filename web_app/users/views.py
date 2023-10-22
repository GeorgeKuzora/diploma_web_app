from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views import View
from django.urls import reverse
from .forms import UserAuthForm, UserRegisterForm, UserSettingsForm


class UserLoginView(View):
    def get(self, request, auth_form=None):
        if not auth_form:
            auth_form = UserAuthForm()
        context = {"form": auth_form}
        return render(request, "users/login.html", context=context)

    def post(self, request):
        auth_form = UserAuthForm(request.POST)
        if auth_form.is_valid():
            login_name = auth_form.cleaned_data["username"]
            password = auth_form.cleaned_data["password"]
            user = authenticate(username=login_name, password=password)
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("jobs:search"))
            elif user:
                auth_form.add_error("__all__", "Error! User is not activated!")
            else:
                auth_form.add_error(
                    "__all__", "Error! username or password is incorrect!"
                )
        else:
            auth_form.add_error("__all__", "Error! Used values is not valid!")
        return self.get(request, auth_form)


class UserRegisterView(View):
    def get(self, request, auth_form=None):
        if not auth_form:
            auth_form = UserRegisterForm()
        context = {"form": auth_form}
        return render(request, "users/register.html", context=context)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user: User = form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            user.email = email
            user.save()
            auth_user = authenticate(username=username, password=raw_password)
            if auth_user and auth_user.is_active:
                login(request, auth_user)
                return HttpResponseRedirect(reverse("jobs:search"))
        else:
            form.add_error("__all__", "Failed to create a new user!")
            return render(request, "users/register.html", {"form": form})


class UserLogoutView(LogoutView):
    next_page = '/jobs/search/'


class UserSettingsView(View):
    def get(self, request, settings_form=None):
        if not settings_form:
            settings_form = UserSettingsForm()
        context = {"form": settings_form}
        return render(request, "users/settings.html", context=context)

    def post(self, request):
        form = UserSettingsForm(request.POST)
        user: User = request.user
        if form.is_valid():
            username = form.cleaned_data.get("username")
            firstname = form.cleaned_data.get("firstname")
            lastname = form.cleaned_data.get("lastname")
            parent_name = form.cleaned_data.get("parent_name")
            email = form.cleaned_data.get("email")
            birthdate = form.cleaned_data.get("birthdate")
            skills = form.cleaned_data.get("skills")
            phone = form.cleaned_data.get("phone")
            address = form.cleaned_data.get("address")
            if email:
                user.email = email
            user.save()
            return HttpResponseRedirect(reverse("users:settings"))
        else:
            form.add_error("__all__", "Failed to update user's data!")
            return render(request, "users/settings.html", {"form": form})
