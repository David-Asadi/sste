from django.urls import path
from . import views


urlpatterns = [
    path('cnc/', views.cncPage, name="supreme-cnc"),

]