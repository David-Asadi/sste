from django.urls import path
from . import views


urlpatterns = [
    path('plastic/', views.plasticPage, name="supreme-plast"),

]