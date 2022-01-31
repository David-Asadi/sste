from django.urls import path
from . import views


urlpatterns = [
    path('fabrication/', views.fabPage, name="supreme-fab"),

]