from django.contrib import admin

# Register your models here.

from .models import Fabrication_Product, Fab_Cat

admin.site.register(Fabrication_Product)
admin.site.register(Fab_Cat)