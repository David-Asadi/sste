from fabrication_products.models import Fabrication_Product

def product_list(request):
    products = Fabrication_Product.objects.all()
    return{
        'fablist': products
    }