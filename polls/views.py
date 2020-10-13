from django.shortcuts import render, redirect
from.models.product import Product
from.models.category import Category
from.models.customer import Customer

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
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    else:
        postData = request.POST
        fname = postData.get('fname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        #validating
        error_message = None
        if(not fname):
            error_message = "Name Required !!!"
        elif len(fname)<4:
            error_message = "Must be 4 Characters and more !!!"
            
        #saving
        if not error_message:
            customer = Customer(fname=fname, phone=phone, email=email, password=password)
            customer.register()
            return redirect('index')
        else:
            return render(request, 'signup.html', {'error':error_message})
        
    