from django.shortcuts import render

from .forms import CreatUserForm

# Create your views here.





def home(request):
    return render(request,'account/home.html')

def Registration(request):
    form=CreatUserForm()

    if request.method == 'POST':
        form=CreatUserForm(request.POST)
        if form.is_valid():
            form.save()

    context={
        'form':form
    }

    return render(request,'account/register.html',context)