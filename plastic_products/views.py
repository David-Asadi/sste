from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import Plastic_Product, Plast_Cat


# Create your views here.


def plastproPage(request):
    subcat = Plast_Cat.objects.all()
    pproducts = Plastic_Product.objects.all()
    context = {'pproducts': pproducts, 'subcat': subcat}
    return render(request, 'plastic_products/plastic-products.html', context)

def product(request, pk):
    subCategory = Plastic_Product.sub_category.get_object
    productObj = Plastic_Product.objects.get(id=pk)
    return  render(request, 'plastic_products/plastic-product-detail.html', {'plasticproduct': productObj})

