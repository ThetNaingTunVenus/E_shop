from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
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

def validateCustomer(customer):
    error_message = None
    if(not customer.fname):
        error_message = "Name Required !!!"
    elif len(customer.fname)<4:
        error_message = "Must be 4 Characters and more !!!"
    elif customer.isExist():
        error_message = 'Email Address Allready Used'
    

    return error_message


def registerUser(request):
    postData = request.POST
    fname = postData.get('fname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')
    #validating
    error_message = None
    customer = Customer(fname=fname, phone=phone, email=email, password=password)
    
    error_message = validateCustomer(customer)
    #saving
    if not error_message:
        # customer = Customer(fname=fname, phone=phone, email=email, password=password)
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('index')
    else:
        return render(request, 'signup.html', {'error':error_message})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    else:
        return registerUser(request)
        

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('index')
            else:
                error_message = 'Password Invaild !!!'
        else:
            error_message = 'Login Invalid !!!'
        print(email, password)
        return render(request, 'index.html', {'error':error_message})