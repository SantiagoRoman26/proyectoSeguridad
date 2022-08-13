from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm

class FormularioRegistrar(forms.Form):
    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput(),help_text=password_validation.password_validators_help_text_html())
    email = forms.EmailField(max_length = 105)
    first_name= forms.CharField(max_length = 70)
    last_name= forms.CharField(max_length = 70)

    def clean(self):
        password_validation.validate_password(self.cleaned_data.get('password'), None)
        return self.cleaned_data


class FormularioLogin(forms.Form):
    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput()) 

class CambiarPassword(forms.Form):
    oldPassword = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords are not equal')
        password_validation.validate_password(self.cleaned_data.get('password'), None)
        return self.cleaned_data