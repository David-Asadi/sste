from django.urls import path
from . import views


urlpatterns = [
    path('plastic-products/', views.plastproPage, name="plastic-products"),
    path('plastic-product-detail/<str:pk>/', views.product, name="plastic-product-detail"),

]