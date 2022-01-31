from django.contrib import admin

# Register your models here.

from .models import  Cnc_Cat, Cnc_Product

admin.site.register(Cnc_Cat)
admin.site.register(Cnc_Product)
