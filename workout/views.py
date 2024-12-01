from django.shortcuts import render, redirect
from .form import UserCreationForm, LoginForm
from django.views.generic import TemplateView

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required


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

    context = {'form': form}
    return render(request, 'register.html', context=context)


# Login a user
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Corrected function call
                return redirect('home')  # Redirect to home page after login

    context = {'form': form}
    return render(request, 'my-login.html', context=context)


# My workouts view
@login_required(login_url='my-login')
def myworkouts(request):
    return render(request, 'myworkouts.html')


# User logout
def user_logout(request):
    logout(request)  # Use the `logout` function correctly
    return redirect('home')
