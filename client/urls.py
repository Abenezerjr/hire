from django.urls import path
from . import views


urlpatterns=[
 path('',views.client_home,name='client_home')
]