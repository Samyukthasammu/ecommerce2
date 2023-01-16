from django.urls import path
from . import views

app_name='seller'
urlpatterns=[
    path('seller_home',views.seller_home,name='sellhome'),
    path('add_product',views.add_product,name='addprod'),
    path('order_history',views.order_history,name='ordrhist'),
    path('product_catalogue',views.product_catalogue,name='prodcata'),
    path('recent_order',views.recent_order,name='recent'),
    path('sell_changepassword',views.sell_changepassword,name='sellchange'),
    path('sell_profile',views.sell_profile,name='sellpro'),
    path('update_stock',views.update_stock,name='updatestock'),
    path('edit_profile',views.edit_profile,name='editprof')
]