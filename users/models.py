from django.contrib.auth.models import User
from django.db import models
from companies.models import Address
from skills.models import Skill


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parentname = models.CharField("user parent name", max_length=20, null=True, blank=True)
    birthdate = models.DateField("user birthdate", null=True, blank=True)
    skills = models.ManyToManyField(Skill, null=True, blank=True)
    phone = models.CharField("user phone", max_length=12, null=True, blank=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="user address"
    )

    class META:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return f"{self.user}"
