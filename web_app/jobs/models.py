from django.core.validators import MinValueValidator
from django.utils.timezone import now
from django.db import models
from skills.models import Skill
from companies.models import Company, Address
from datetime import date


class Job(models.Model):
    class Experience(models.TextChoices):
        WITHOUT = "WITHOUT"
        UPTO3YEARS = "1-3YEARS"
        UPTO6YEARS = "3-6YEARS"
        UPTO9YEARS = "6-9YEARS"
        UPTO12YEARS = "9-12YEARS"

    job_name = models.CharField(max_length=100, verbose_name="job title")
    job_description = models.TextField(verbose_name="job description")
    skills = models.ManyToManyField(Skill)
    min_salary = models.IntegerField(
        "minimum salary",
        validators=[MinValueValidator(limit_value=0)],
        null=True
    )
    max_salary = models.IntegerField("maximum salary", null=True)
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, verbose_name="company", null=True
    )
    pub_date = models.DateField(null=True)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, verbose_name="address", null=True
    )
    is_archived = models.BooleanField("is archived", default=False)
    required_experience = models.CharField(
        "required experience", max_length=11, blank=True, choices=Experience.choices
    )

    class META:
        ordering = ["pub_date", "job_name"]
        verbose_name = "job"
        verbose_name_plural = "jobs"

    def __str__(self):
        return self.job_name
