from django.db import models

# Create your models here.

class PlastGal(models.Model):
    class Meta:
        verbose_name_plural = "Plastic Gallery"
        verbose_name = "Plastic Gallery item"

    title = models.CharField(max_length=200, default='Plastic Product Example')
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=False)
    def __str__(self):
        return self.title