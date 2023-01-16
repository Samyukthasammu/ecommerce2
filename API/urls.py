from django.urls import path
from . import views

app_name='api'
urlpatterns=[

    path('add_student',views.add_student),
    path('list_student',views.list_student),
    path('delete_student/<int:sid>',views.delete_student),
    path('update_student/<int:sid>',views.update_student),
    path('index',views.index,name='index'),
    path('home',views.home,name='home')
]