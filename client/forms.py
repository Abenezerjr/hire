from django import forms

from  django.forms import ModelForm
from .models import Client,OCCUPATIONS,HireNeed

class ClinentForm(ModelForm):
    class Meta:
        model=Client
        fields=['fullname','email','phonenumber',]
        labels={
            'fullname':'Full Name',
            'email':'Email',
            'phonenumber':'PhoneNumber'
        }


    def __init__(self,*args,**kwargs):
        super( ClinentForm,self).__init__(*args,**kwargs)
        self.fields['fullname'].widget.attrs.update({'class':'appearance-none block w-full bg-black text-white border border-gray-200 rounded py-3 px-4 mb-2 leading-tight focus:outline-none focus:bg-gray-900 focus:border-gray-500 italic','placeholder':'FullName'})
        self.fields['email'].widget.attrs.update({'class':'appearance-none block w-full bg-black text-white border border-gray-200 rounded py-3 px-4 mb-2 leading-tight focus:outline-none focus:bg-gray-900 focus:border-gray-500 italic','placeholder':'Your work email'})
        self.fields['phonenumber'].widget.attrs.update({'class':'appearance-none block w-full bg-black text-white border border-gray-200 rounded py-3 px-4 mb-2 leading-tight focus:outline-none focus:bg-gray-900 focus:border-gray-500 italic','placeholder':'Phone number'})