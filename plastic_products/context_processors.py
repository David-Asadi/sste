from plastic_products.models import Plastic_Product

def product_list(request):
    products = Plastic_Product.objects.all()
    return{
        'plastlist': products
    }