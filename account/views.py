from django.shortcuts import render

from .forms import CreatUserForm

# Create your views here.


def RegistrationForm(request):
    form=CreatUserForm()

    context={
        'form':form
    }

    return render(request,'account/register.html',context)