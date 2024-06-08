from django.shortcuts import render , redirect , HttpResponse

from . forms import ClinentForm ,OCCUPATIONSForm
from .models import Client
# Create  your views here.


def client_home(request):
    form=ClinentForm()
    if request.method == 'POST':
        form = ClinentForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get('fullname')
            email = form.cleaned_data.get('email')
            phonenumber = form.cleaned_data.get('phonenumber')

            user, created = Client.objects.get_or_create(
                fullname=fullname,
                email=email if email else None,
                phonenumber=phonenumber if phonenumber else None,
            )
            request.session['client_email'] = client_email
            return redirect('choose')
    else:
        form = ClinentForm()  # Ensure form is initialized here

    context = {
        'form': form
    }
    return render(request, 'client/client_home.html', context)
    # # form=ClinentForm()
    # if request.method == 'POST':
    #     form=ClinentForm(request.POST)
    #     if form.is_valid():
    #         fullname=form.cleaned_data.get('fullname')
    #         email=form.cleaned_data.get('email')
    #         phonenumber=form.cleaned_data.get('phonenumber')
    #
    #         user,created=Client.objects.get_or_create(fullname=fullname,email=email if email else None,
    #                                                   phonenumber=phonenumber if phone_number else None, )
    #         request.session['user_id']=user.id
    #         return redirect('choose')
    # else:
    #     form = ClinentForm()
    #
    #
    # # form=ClinentForm()
    # # if request.method=='POST':
    # #     form=ClinentForm(request.POST)
    # #     if form.is_valid():
    # #         form.save()
    # #         return redirect('choose')
    # #     else:
    # #         print('error occure')
    # context={
    #         'form':form
    #     }
    # return render(request,'client/client_home.html',context)

def choose_developer(request):
    client_email=request.session.get('client_email')
    if not client_email:
        return HttpResponse('error')

    client=Client.objects.get(email=client_email)

    if request.method == 'POST':
        form = OCCUPATIONSForm(request.POST)
        if form.is_valid():
            occupations=form.save(commit=False)
            occupations.client=client
            occupations.save()
            return  redirect('choose_step_2')

    else:
        form=OCCUPATIONSForm()



    context={
        'form':form,
        'client':client
    }
    return render(request,'client/choose.html',context)

def choose_step_2(request):
    return render(request,'client/choose-step2.html')

def thinkYou(request):
    return render(request,'client/thankYoupage.html')