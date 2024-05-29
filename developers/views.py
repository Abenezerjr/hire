from django.shortcuts import render

# Create your views here.


def developer_home(request):
    return render(request,'developers/developers_home.html')

