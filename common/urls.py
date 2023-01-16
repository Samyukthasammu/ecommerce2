from django.urls import path
from . import views

app_name='common'
urlpatterns=[
    path('',views.common_home,name='prohome'),
    path('customer_reg',views.common_cus_reg,name='cusreg'),
    path('customer_login',views.common__cus_login,name='cuslogin'),
    path('seller_reg',views.common_sell_reg,name='sellreg'),
    path('seller_login',views.common__sell_login,name='selllogin'),
    path('check_email',views.check_email,name='check_email')
]
