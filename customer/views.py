from django.shortcuts import render,redirect
from seller.models import Product
from customer.models import Customer
from . models import Cart
from . decorator import auth_customer

# Create your views here.

@auth_customer
def customer_home(request):
    # if 'customer' in request.session :

        products = Product.objects.all() # select * from product\
        
    # products = [
    # {
      #  seller:2,
      #  product_name:'laptop'
      #  description :'dwdw'
      # -----------
    # },
    #{
    #  seller:2,
      #  product_name:'laptop'
      #  description :'dwdw'
      # ----------- 
    # }
    # ]
    # we pass data from view to html in dictionary format
        return render(request,'customer/customer_home.html',{'product_list': products})

    # else:
    #     return redirect('common:cuslogin')


def cus_change_password(request):
    msg = ''
    if request.method == 'POST' :
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['current_pass']
        new_pass = request.POST['new_pass']
        confirm_pass = request.POST['confirm_pass']

        if customer.password == current_pass : 

            if new_pass == confirm_pass :
                customer.password = new_pass
                customer.save()
                msg = 'password change'
            else :
                msg = 'password does not match'
        
        else :
            msg = 'incorrect password'

    return render(request,'customer/cus_change_password.html',{'msg':msg})

def cus_profile(request):
    return render(request,'customer/cus_profile.html')

@auth_customer
def my_cart(request):
    product_cart = Cart.objects.filter(customer_id = request.session['customer'])
    return render(request,'customer/my_cart.html', {'cart_list':product_cart})

def my_order(request):
    return render(request,'customer/my_order.html')

@auth_customer
def product_details(request,pid):
    msg = ''
    product_data = Product.objects.get(id = pid) # fetching single data from table
    

    if request.method == 'POST' :
        product_id = request.POST['pid']

        item_exist = Cart.objects.filter(product_id = product_id, customer_id = request.session['customer']).exists()
        if not item_exist : # if itam_exist == false
            cart_item =Cart(product_id = product_id, customer_id = request.session['customer'])
            cart_item.save()
            return redirect('customer:mycart')

        else :
            msg = 'item already in cart'
    return render(request,'customer/product_details.html',{'product': product_data,'msg': msg})


def cus_pro_edit(request):
    return render(request,'customer/cus_pro_edit.html')

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:cuslogin')

@auth_customer
def cus_delete_item(request,id):
    cart_item = Cart.objects.get(product = id, customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:mycart')

