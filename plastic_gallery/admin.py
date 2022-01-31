from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import PlastGal

admin.site.register(PlastGal)
admin.site.unregister(Group)
