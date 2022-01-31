from django.db import models
import uuid

# Create your models here.

class Member(models.Model):
    class Meta:
        verbose_name_plural = "Team Members"
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    thumbnail_image = models.ImageField(null=True, blank=True, default="default_member.jpg")
    def __str__(self):
        return self.name