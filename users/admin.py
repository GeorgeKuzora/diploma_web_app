from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    fieldsets = [(
        "Authentication information",
        {
            "fields": ["username", "password"]
        }
    ),
        (
        "Personal information",
        {
            "fields": ["first_name", "last_name", "email"]
                 }
        )]
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
