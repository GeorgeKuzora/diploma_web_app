from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(
        "skill title", max_length=50, primary_key=True, unique=True
    )
    skill_description = models.TextField("skill description", blank=True, null=True)

    class Meta:
        ordering = ["skill_name"]
        verbose_name = "skill"
        verbose_name_plural = "skills"

    def __str__(self):
        return self.skill_name
