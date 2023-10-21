from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django import forms
class LoginForm(UserCreationForm):  
    class Meta:
         model=User
         fields=['username', 'email', 'password1', 'password2']
         widgets={
            'email':forms.EmailInput(attrs={'required':'required'}),
            'username': forms.TextInput(attrs={'autocomplete': 'off'}),
         }