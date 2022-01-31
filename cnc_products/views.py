from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import Cnc_Cat, Cnc_Product


# Create your views here.


def cncproPage(request):
    subcat = Cnc_Cat.objects.all()
    cproducts = Cnc_Product.objects.all()
    context = {'cproducts': cproducts, 'subcat': subcat}
    return render(request, 'cnc_products/cnc-products.html', context)

def product(request, pk):
    subCategory = Cnc_Product.sub_category.get_object
    productObj = Cnc_Product.objects.get(id=pk)
    return  render(request, 'cnc_products/cnc-product-detail.html', {'cncproduct': productObj})

