from django.urls import path
from . import  views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.Registration,name='register'),
    path('login/',views.UserLogin,name='login'),
]