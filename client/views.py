from django.shortcuts import render

# Create your views here.


def client_home(request):
    return render(request,'client/client_home.html')

def choose_developer(request):
    return render(request,'client/choose.html')
