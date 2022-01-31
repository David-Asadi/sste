from django.db import models

# Create your models here.

class CncGal(models.Model):
    class Meta:
        verbose_name_plural = "Edit CNC Gallery"
        verbose_name = 'CNC Gallery item'


    title = models.CharField(max_length=200, default='CNC Machined Example')
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=False)
    def __str__(self):
        return self.title