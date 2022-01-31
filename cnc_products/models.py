from email.policy import default
from tkinter import CASCADE, TRUE
from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.


class Cnc_Cat(models.Model):
    class Meta:
        verbose_name_plural = "CNC Subcategories"
        verbose_name = "CNC Sub-Category"

    name = models.CharField(max_length=50, blank=False,)
    def __str__(self):
        return self.name

class Cnc_Product(models.Model):

    class Meta:
        verbose_name_plural = "CNC Products"
        verbose_name = "CNC Product item"
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    sub_category = models.ForeignKey(Cnc_Cat, null=True, on_delete=models.CASCADE)
    used_for = models.CharField(max_length=200, null=True, blank=False)
    material = models.CharField(max_length=200, null=True, blank=False)
    thumbnail_image = models.ImageField(null=True, blank=True, default="product-placeholder.jpg")
    product_image_1 = models.ImageField(null=True, blank=True, default="product-placeholder.jpg")
    product_image_2 = models.ImageField(null=True, blank=True, )
    product_image_3 = models.ImageField(null=True, blank=True,)
    product_image_4 = models.ImageField(null=True, blank=True,)
    product_image_5 = models.ImageField(null=True, blank=True,)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
  


    def __str__(self):
        return self.title

