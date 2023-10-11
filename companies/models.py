from django.db import models


class Company(models.Model):
    title = models.CharField("company title", max_length=100)
    description = models.TextField("company description")
    email = models.EmailField("company email")
    phone = models.CharField("company phone", max_length=12)
    address = models.ForeignKey(
        "Address", on_delete=models.SET_NULL, verbose_name="address"
    )

    class META:
        ordering = ["title"]
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self):
        return self.title
