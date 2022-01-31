
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('team.urls')),
    path('', include('cncgallery.urls')),
    path('', include('fabrication_gallery.urls')),
    path('', include('plastic_gallery.urls')),
    path('', include('fabrication_products.urls')),
    path('', include('cnc_products.urls')),
    path('', include('plastic_products.urls')),
    path('', include('contact.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
