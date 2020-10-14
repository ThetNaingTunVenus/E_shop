from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from polls.models.product import Product
from polls.models.category import Category
from polls.models.customer import Customer
from django.views import View





class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
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

