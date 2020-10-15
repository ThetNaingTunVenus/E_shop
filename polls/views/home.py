from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from polls.models.product import Product
from polls.models.category import Category
from polls.models.customer import Customer
from django.views import View



# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    print(request.session.get('email'))
    return render(request, 'index.html', data)

