from django.contrib import admin
admin.site.site_header = ' SUPREME ADMINISTRATION PANEL V1.0'
# Register your models here.
from .models import Member

admin.site.register(Member)
