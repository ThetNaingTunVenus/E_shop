from django.shortcuts import render
from.models.product import Product

# Create your views here.
def index(request):
    products = Product.get_all_products()
    print(products)
    return render(request, 'index.html', {'products':products})