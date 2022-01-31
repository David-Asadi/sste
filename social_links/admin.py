from django.contrib import admin

# Register your models here.
from .models import SocialCat, SocialMedia

admin.site.register(SocialMedia)
admin.site.register(SocialCat)