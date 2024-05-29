from  django.urls import path

from . import views

urlpatterns=[
    path('',views.developer_home,name='developer_home')
]