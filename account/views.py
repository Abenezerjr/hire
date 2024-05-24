from django.shortcuts import render

from .forms import CreatUserForm

# Create your views here.





def home(request):
    return render(request,'account/home.html')

def RegistrationForm(request):


    return render(request,'account/register.html',context)