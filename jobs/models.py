from django.db import models
from skills.models import Skill


class Job(models.Model):
    job_name = models.CharField(max_length=100)
    job_description = models.TextField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.job_name
