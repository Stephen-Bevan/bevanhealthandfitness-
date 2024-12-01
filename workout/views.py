from django.shortcuts import render, redirect
from .form import UserCreationForm, LoginForm
from django.views.generic import TemplateView

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
