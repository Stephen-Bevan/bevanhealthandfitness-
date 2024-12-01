from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# - Create user registration form
class CustomUserCreationForm(UserCreationForm):  # Renamed for clarity
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Corrected field names

# - Create login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))  # Optional placeholder
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))  # Optional placeholder









