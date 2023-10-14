from datetime import date
from django.db import models
from skills.models import Skill


class User:
    name = models.CharField("user name", max_length=20)
    lastname = models.CharField("user lastname", max_length=30)
    parentname = models.CharField("user parent name", max_length=20)
    birthdate = models.DateField()
    email = models.EmailField("user email")
    password = models.CharField("user password")
    registration_date = models.DateField(default=date.today())
    skills = models.ManyToManyField(Skill)
    phone = models.CharField("company phone", max_length=12)
    address = models.ForeignKey(
        "Address", on_delete=models.SET_NULL, verbose_name="address"
    )

    class META:
        ordering = ["lastname", "name", "parentname"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.lastname} {self.name} {self.parentname}"
