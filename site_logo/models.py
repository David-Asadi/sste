from django.db import models

# Create your models here.

class Change_Logo(models.Model):
    class Meta:
        verbose_name_plural = "Change Site Logo"
        verbose_name = "Website Logo"
    logo = models.ImageField(null=True, blank=True, default="default-logo.png")

    def __str__(self):
        return "Change Logo"

    