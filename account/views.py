from django.shortcuts import render , HttpResponse ,redirect

from .forms import CreatUserForm ,StyledAuthenticationForm
from django.contrib.auth import logout ,login,authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request,'account/home.html')

def Registration(request):
    form=CreatUserForm()

    if request.method == 'POST':
        form=CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context={
        'form':form
    }

    return render(request,'account/register.html',context)

def UserLogin(request):
    form = StyledAuthenticationForm()

    if request.method == 'POST':
        form = StyledAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and user. is_developer == True:
                login(request, user)
                return redirect('developer_home')
            if user is not None and user. is_developer == False:
                login(request, user)
                return redirect('client_home')
    context = {
        'loginForm': form
    }

    return render(request, 'account/login.html', context)

def userLogout(request):
    logout(request)
    return redirect('login')