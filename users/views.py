from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views import View
from django.urls import reverse
from .forms import UserAuthForm
from django.contrib.auth.views import LoginView


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
            auth_form.add_error(
                "__all__", "Error! Used values is not valid!"
            )
        return self.get(request, auth_form)
