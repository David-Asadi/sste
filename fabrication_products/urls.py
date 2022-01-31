from django.urls import path
from . import views


urlpatterns = [
    path('fabrication-products/', views.fabproPage, name="fabrication-products"),
    path('fab-product-detail/<str:pk>/', views.product, name="fab-product-detail"),

]