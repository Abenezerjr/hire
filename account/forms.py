from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CreatUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'firstName', 'lastName', 'password1', 'password2', 'is_developer']
        labels = {
            'email':'Email',
            'firstName':'First Name',
            'lastName':'Last Name',
            'is_developer': 'Are You a Developer? ',

        }

    def __init__(self, *args, **kwargs):
        super(CreatUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'placeholder': 'you@example.com'})
        self.fields['firstName'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['lastName'].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
        self.fields['is_developer'].widget.attrs.update({'label': 'Are You a Developer?'})
