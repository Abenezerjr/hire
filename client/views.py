from django.shortcuts import render , redirect , HttpResponse

from . forms import ClinentForm ,OCCUPATIONSForm ,HireNeedForm
from .models import Client
# Create  your views here.

def client_home(request):
    if request.method == 'POST':
        form = ClinentForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get('fullname')
            email = form.cleaned_data.get('email')
            phonenumber = form.cleaned_data.get('phonenumber')

            client, created = Client.objects.get_or_create(
                fullname=fullname,
                email=email if email else None,
                phonenumber=phonenumber if phonenumber else None,
            )

            if created:
                print("New client created:", client)
            else:
                print("Client already exists:", client)

            request.session['client_email'] = client.email
            return redirect('choose_step_1')
        else:
            # Print form errors to the console for debugging
            print("Form is not valid:", form.errors)
    else:
        form = ClinentForm()

    context = {
        'form': form
    }
    return render(request, 'client/client_home.html', context)


# def choose_developer(request):
#     form=OCCUPATIONSForm()
#     context={
#         'form':form
#     }
#     return render(request,'client/choose.html',context)

# def choose_developer(request):
#     client_email=request.session.get('client_email')
#     if not client_email:
#         return HttpResponse('error  be cus we we cant reach')
#
#     client=Client.objects.get(email=client_email)
#
#     if request.method == 'POST':
#         form = OCCUPATIONSForm(request.POST)
#         if form.is_valid():
#             occupations=form.save(commit=False)
#             occupations.client=client
#             occupations.save()
#             return  redirect('choose_step_2')
#
#     else:
#         form=OCCUPATIONSForm()
#
#
#
#     context={
#         'form':form,
#         'client':client
#     }
#     return render(request,'client/choose.html',context)

def choose_developer(request):
    # form=None
    client_email = request.session.get('client_email')
    if not client_email:
        return HttpResponse('Error because we cannot reach the client.')

    try:
        client = Client.objects.get(email=client_email)
    except Client.DoesNotExist:
        return HttpResponse('Error because the client does not exist.')

    if request.method == 'POST':
        form = OCCUPATIONSForm(request.POST)
        if form.is_valid():
            occupations = form.save(commit=False)
            occupations.client = client
            occupations.save()
            return redirect('choose_step_2')
    else:
        form = OCCUPATIONSForm()

    context = {
        'form': form,
        'client': client
    }
    return render(request, 'client/choose.html', context)

def choose_step_2(request):
    # form=HireNeedForm()
    client_email = request.session.get('client_email')
    if not client_email:
        return HttpResponse('Error because we cannot reach the client.')

    try:
        client = Client.objects.get(email=client_email)
    except Client.DoesNotExist:
        return HttpResponse('Error because the client does not exist.')

    if request.method == 'POST':
        form=HireNeedForm(request.POST)
        if form.is_valid():
            hireneed=form.save(commit=False)
            hireneed.client=client
            hireneed.save()
            return redirect('thinkYou')

    else:
        form=HireNeedForm()

    context={
        'form':form,
        'client':client,
    }

    return render(request,'client/choose-step2.html',context)

def thinkYou(request):
    return render(request,'client/thankYoupage.html')


def commingSoon(request):
    return render(request,'commingSoon.html')