from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import Fabrication_Product, Fab_Cat


# Create your views here.


def fabproPage(request):
    subcat = Fab_Cat.objects.all()
    products = Fabrication_Product.objects.all()
    context = {'products': products, 'subcat': subcat}
    return render(request, 'fabrication_products/fabrication-products.html', context)


def product(request, pk):
    subCategory = Fabrication_Product.sub_category.get_object
    productObj = Fabrication_Product.objects.get(id=pk)
    return  render(request, 'fabrication_products/fab-product-detail.html', {'fabproduct': productObj})

