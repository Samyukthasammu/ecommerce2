from django.shortcuts import render, redirect
from .models import Customer 
from.models import Seller
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from .decorator import auth_customer
# Create your views here.

@auth_customer
def common_home(request):
    return render(request,'common/project_home.html')

def common_cus_reg(request):
    if request.method == 'POST':  # when submit button click(before the method will be get)
        
        c_name = request.POST['fname'] #to get textbox data
        c_gender = request.POST['gender']
        c_phone = request.POST['phone']
        c_email = request.POST['email']
        c_password = request.POST['psw']
        c_address = request.POST['address']
        

        # in ORM, if we want to insert a data in table,
        # 1.create an object of model class, here model class is customer
        new_customer = Customer(customer_name = c_name,email = c_email, address = c_address, phone = c_phone, 
        gender = c_gender,password = c_password)
        # call save() method
        new_customer.save()
        


    return render(request,'common/customer_reg.html')

def common__cus_login(request):
    msg =""
    if request.method == 'POST':

        email = request.POST['uname']
        password = request.POST['password']

        try:
            customer = Customer.objects.get(email = email, password = password)
            request.session['customer'] = customer.id
            return redirect('customer:cushome')
        except Exception as e:
            print(e)
            msg = "User Name or Password Incorrect"



    return render(request,'common/customer_login.html',{'message':msg})

def common_sell_reg(request):
    # by default, form method will be get

    if request.method == 'POST':  # when the submit button clicked

        s_name = request.POST['firstname'] #to get textbox data
        s_phone = request.POST['phone']
        s_email = request.POST['email']
        s_address = request.POST['addrss']
        s_comp_name = request.POST['company']
        acc_holder_name = request.POST['acname']
        s_ifsc = request.POST['ifsc']
        s_branch = request.POST['branch']
        acc_number = request.POST['acnumber']
        seller_pic = request.FILES['filename']

        user_name = random.randint(1111,9999)
        password = 'sel-' + str(user_name) + s_name # result will be sel-3456-samy

        new_seller = Seller(seller_name = s_name,
        email = s_email, 
        phone = s_phone, 
        address = s_address, 
        company_name = s_comp_name,
        acc_holder_name = acc_holder_name, 
        ifsc = s_ifsc, 
        branch = s_branch, 
        acc_number = acc_number,
        seller_pic = seller_pic,
        user_name = user_name,
        password = password
        )

        new_seller.save()

        message = 'hi your username is' + str(user_name) + 'and password is ' + password

        # send_mail function used to send mail through our application
        #1st argument -> subject
        #2nd argument -> message
        #3rd argument -> from email
        #4th argument -> recipient list, here recipient list should be in an array format
        send_mail('username and password',
            message,
            settings.EMAIL_HOST_USER,
            [s_email,]
        )


    return render(request,'common/seller_reg.html')
    
def common__sell_login(request):
    msg = ""
    if request.method == 'POST':

        user_name = request.POST['user_name']
        password = request.POST['password']

        # when we use get() to fetch data, we must use try except,
        # if the data is not found in the table, exception will be raised

        try:
            seller = Seller.objects.get(user_name = user_name, password = password)
            request.session['seller'] = seller.id
            return redirect('seller:sellhome')
        except:
            msg = "User Name or Password Incorrect"
            # data from view to html will be passed in render() as dictionary

    return render(request,'common/seller_login.html',{'message':msg})

def check_email(request):
    email = request.POST['email']

    exist = Customer.objects.filter(email = email).exists()

    return JsonResponse({'status' : exist})