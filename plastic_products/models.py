from email.policy import default
from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.

class Plast_Cat(models.Model):
    class Meta:
        verbose_name_plural = "Plastic Subcategories"
        verbose_name = "Plastic Sub-Category"

    name = models.CharField(max_length=50, blank=False,)
    def __str__(self):
        return self.name



class Plastic_Product(models.Model):

    class Meta:
        verbose_name_plural = "Plastic Products"
        verbose_name = "Plastic Product item"
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    sub_category = models.ForeignKey(Plast_Cat, null=True, on_delete=models.CASCADE)
    used_for = models.CharField(max_length=200, null=True, blank=False)
    material = models.CharField(max_length=200, null=True, blank=False)
    thumbnail_image = models.ImageField(null=True, blank=True, default="product-placeholder.jpg")
    product_image_1 = models.ImageField(null=True, blank=True, default="product-placeholder.jpg")
    product_image_2 = models.ImageField(null=True, blank=True,)
    product_image_3 = models.ImageField(null=True, blank=True,)
    product_image_4 = models.ImageField(null=True, blank=True,)
    product_image_5 = models.ImageField(null=True, blank=True,)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
  


    def __str__(self):
        return self.title

