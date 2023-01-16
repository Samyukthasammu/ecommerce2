from django.urls import path
from . import views

app_name='customer'
urlpatterns=[
    path('customer_home',views.customer_home,name='cushome'),
    path('cus_change_password',views.cus_change_password,name='cuschange'),
    path('cus_profile',views.cus_profile,name='cuspro'),
    path('my_cart',views.my_cart,name='mycart'),
    path('my_order',views.my_order,name='myorder'),
    path('product_details/<int:pid>',views.product_details,name='prodetails'),
    path('cus_pro_edit',views.cus_pro_edit,name='cusproedit'),
    path('logout',views.logout,name='logout'),
    path('delete/<int:id>',views.cus_delete_item,name='cus_delete')
    ]