from django.urls import path
from . import views


urlpatterns = [
    path('cnc-products/', views.cncproPage, name="cnc-products"),
    path('cnc-product-detail/<str:pk>/', views.product, name="cnc-product-detail"),

]