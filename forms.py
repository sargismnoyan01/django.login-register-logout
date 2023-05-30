from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *



class Create(UserCreationForm):
    class Meta:
        model=User
        fields=('username',"email",'password1','password2')


class ConForm(forms.ModelForm):
    class Meta:
        model=ContactForm
        fields='__all__'