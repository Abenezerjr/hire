from django.urls import path
from . import views


urlpatterns=[
 path('',views.client_home,name='client'),
 path('choose_step_1/',views.choose_developer,name='choose_step_1'),
 path('choose-step-2/',views.choose_step_2,name='choose_step_2'),
 path('thinkYou/',views.thinkYou,name='thinkYou'),
 path('commingSoon',views.commingSoon(),name='comming_soon'),
]