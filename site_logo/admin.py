from django.contrib import admin
from.models import Change_Logo
# Register your models here.



class logo_permission(admin.ModelAdmin):

    def has_add_permission(self, request):
        # Disable add
        return False

    def has_delete_permission(self, request, objt=None):
        # Disable add
        return False

    



admin.site.register(Change_Logo, logo_permission)