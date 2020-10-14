from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from polls.models.product import Product
from polls.models.category import Category
from polls.models.customer import Customer
from django.views import View


        
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        fname = postData.get('fname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        #validating
        error_message = None
        customer = Customer(fname=fname, phone=phone, email=email, password=password)

        if(not customer.fname):
            error_message = "Name Required !!!"
        elif len(customer.fname)<4:
            error_message = "Must be 4 Characters and more !!!"
        elif customer.isExist():
            error_message = 'Email Address Allready Used'
    
            return error_message
        
        # error_message = self.validateCustomer(customer)
        #saving
        if not error_message:
            # customer = Customer(fname=fname, phone=phone, email=email, password=password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            return render(request, 'signup.html', {'error':error_message})
