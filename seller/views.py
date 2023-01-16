from django.shortcuts import render
from .models import Product
from common.models import Seller

# Create your views here.


def seller_home(request):
    profile = Seller.objects.get(id = request.session['seller'])

    return render(request,'seller/seller_home.html',{'seller_prof': profile})

def add_product(request):
    if request.method == 'POST':  # when submit button click(before the method will be get)
        
        p_name = request.POST['pname']
        description = request.POST['desc']
        p_number = request.POST['pnumber']
        p_image = request.FILES['filename']
        p_price = request.POST['price']
        stock = request.POST['stock']

        new_product = Product(product_name = p_name,
        description = description,
        product_number = p_number,
        product_image = p_image,
        product_price = p_price,
        stock = stock,
        seller_id = request.session['seller']
        )

        new_product.save()

    seller = Seller.objects.get(id = request.session['seller'])








    return render(request,'seller/add_product.html',{'seller':seller,'seller_prof': seller})

def order_history(request):
    seller = Seller.objects.get(id = request.session['seller'])
    return render(request,'seller/order_history.html',{'seller_prof':seller})

def product_catalogue(request):
    
    product = Product.objects.filter(seller_id = request.session['seller'])
    seller = Seller.objects.get(id = request.session['seller'])
    

    return render(request,'seller/product_catalogue.html',{'products':product,'seller':seller,'seller_prof':seller})

def recent_order(request):

    msg = ''
    if request.method == 'POST' :

        current_pass = request.POST['current_pass']
        new_pass = request.POST['new_pass']
        confirm_pass = request.POST['confirm_pass']

        seller = Seller.objects.get(id = request.session['seller'])

        if seller.password == current_pass :
            if new_pass == confirm_pass :
                seller = Seller.objects.get(id = request.session['seller'])

    return render(request,'seller/recent_order.html',{'seller':seller,'seller_prof':seller})

def sell_changepassword(request):
    seller = Seller.objects.get(id = request.session['seller'])
    return render(request,'seller/sell_changepassword.html',{'seller':seller,'seller_prof':seller})

def sell_profile(request):
    seller = Seller.objects.get(id = request.session['seller'])
    return render(request,'seller/sell_profile.html',{'seller':seller,'seller_prof':seller})

def update_stock(request):
    seller = Seller.objects.get(id = request.session['seller'])
    return render(request,'seller/update_stock.html',{'seller':seller,'seller_prof':seller})

def edit_profile(request):
    return render(request,'seller/edit_profile.html')