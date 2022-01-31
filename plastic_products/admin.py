from django.contrib import admin

# Register your models here.

from .models import Plastic_Product, Plast_Cat

admin.site.register(Plastic_Product)
admin.site.register(Plast_Cat)