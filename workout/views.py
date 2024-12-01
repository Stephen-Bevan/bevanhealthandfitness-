from django.shortcuts import render, redirect
from .form import UserCreationForm, LoginForm
from django.views.generic import TemplateView

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


# Home page view
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

# Register a user
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page or another page after registration

    context = {'form': form}  # Define context here
    return render(request, 'register.html', context=context)




    # -Login a user
def my_login(request):
    form = LoginForm()  # Correct initialization of the form

    if request.method == "POST":  # Ensure the method is POST (case-sensitive)
        form = LoginForm(request, data=request.POST)  # Reinitialize form with POST data

        if form.is_valid():  # Check if the form is valid
            username = form.cleaned_data.get('username')  # Get cleaned data for 'username'
            password = form.cleaned_data.get('password')  # Get cleaned data for 'password'

            user = authenticate(request, username=username, password=password)  # Authenticate user

            if user is not None:  # Check if the user is authenticated
                auth_login(request, user)  # Log in the user using auth_login
                return redirect('home')  # Redirect to the 'home' view after successful login

    # Render the form with context if GET request or invalid form submission
    context = {'form': form}  # Updated to use the 'form' variable
    return render(request, 'my-login.html', context=context)  # Render the login page


