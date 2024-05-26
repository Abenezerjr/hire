from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CreatUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'firstName', 'lastName', 'password1', 'password2', 'is_developer']
        labels = {
            'email':'Email address',
            'firstName':'First Name',
            'lastName':'Last Name',
            'is_developer': 'Are You a Developer? ',

        }

    def __init__(self, *args, **kwargs):
        super(CreatUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6','placeholder': 'you@example.com',})
        self.fields['firstName'].widget.attrs.update({'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6','placeholder': 'First Name'})
        self.fields['lastName'].widget.attrs.update({'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6','placeholder': 'Last Name'})
        self.fields['password1'].widget.attrs.update({'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6','placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6','placeholder': 'Confirm Password'})
        self.fields['is_developer'].widget.attrs.update({'class':'h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600','label': 'Are You a Developer?'})
