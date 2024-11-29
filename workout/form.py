from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from.django.forms.widgets import PasswordInput, TextInput

#- Make user 

class UserCreationForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','pasword','password2']

   #- Login user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())








