from datetime import date
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models
from companies.models import Address
from skills.models import Skill


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parentname = models.CharField("user parent name", max_length=20)
    birthdate = models.DateField()
    skills = models.ManyToManyField(Skill)
    phone = models.CharField("user phone", max_length=12)
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="user address"
    )

    class META:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return f"{self.user}"
