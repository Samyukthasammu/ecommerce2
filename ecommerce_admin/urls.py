from django.urls import path
from . import views

app_name='ecommerce_admin'
urlpatterns=[
    path('admin_home',views.ecommerce_admin_home,name='adminhome'),
    path('approve_seller',views.approve_seller,name='approveseller'),
    path('view_customer',views.view_customer,name='viewcustomer'),
    path('view_seller',views.view_seller,name='viewseller')
]