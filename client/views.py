from django.shortcuts import render , redirect , HttpResponse

from . forms import ClinentForm

# Create  your views here.


def client_home(request):
    form=ClinentForm()
    if request.method=='POST':
        form=ClinentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('choose_step_2')
        else:
            print('error occure')

    context={
        'form':form
    }
    return render(request,'client/client_home.html',context)

def choose_developer(request):
    return render(request,'client/choose.html')

def choose_step_2(request):
    return render(request,'client/choose-step2.html')

def thinkYou(request):
    return render(request,'client/thankYoupage.html')