from django.db import models

# Create your models here.

class FabGal(models.Model):
    class Meta:
        verbose_name = "Fabrication Gallery item"
        verbose_name_plural = "Edit Fabrication Gallery"

    title = models.CharField(max_length=200, default='Fabrication Example')
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=False)
    def __str__(self):
        return self.title