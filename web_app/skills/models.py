"""
Contains skills app models.

Content: Skill model.
"""
from django.db import models


class Skill(models.Model):
    """
    Skills required for jobs.

    Skill model is used in jobs and user apps.

    Attributes:
        skill_name: models.CharField Name of the skill
        skill_description: models.CharField Long description of the skill
    """
    skill_name = models.CharField(
        "skill title", max_length=50, unique=True
    )
    skill_description = models.TextField("skill description", blank=True, null=True)

    class Meta:
        ordering = ["skill_name"]
        verbose_name = "skill"
        verbose_name_plural = "skills"

    def __str__(self):
        return self.skill_name
