from django.urls import path
from . import views


urlpatterns=[
 path('',views.client_home,name='client_home'),
 path('choose/',views.choose_developer,name='choose'),
 path('choose-step-2/',views.choose_step_2,name='choose_step_2'),
]