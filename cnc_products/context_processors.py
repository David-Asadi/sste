from cnc_products.models import Cnc_Product

def product_list(request):
    products = Cnc_Product.objects.all()
    return{
        'cnclist': products
    }