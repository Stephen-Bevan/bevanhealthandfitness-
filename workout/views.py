from django.shortcuts import render, redirect, get_object_or_404
from .form import UserCreationForm, LoginForm
from django.views import generic, View 
from django.views.generic import TemplateView, ListView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Exercise

# Home page view
class HomePage(TemplateView):
    """
    Displays home page.
    """
    template_name = 'index.html'


# Register a user
def register(request):
    """
    Handles user registration.
    """
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after registration

    context = {'form': form}
    return render(request, 'register.html', context)


# Login a user
def my_login(request):
    """
    Handles user login.
    """
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login

    context = {'form': form}
    return render(request, 'my-login.html', context)


# My workouts view
@login_required(login_url='my-login')
def myworkouts(request):
    """
    Displays the user's workouts.
    """
    return render(request, 'myworkouts.html')


# User logout
def user_logout(request):
    """
    Logs out the user.
    """
    logout(request)
    return redirect('home')


# List workouts
@login_required
def workout_list(request):
    """
    Displays a list of workouts created by the logged-in user.
    """
    workouts = Exercise.objects.filter(user=request.user)
    return render(request, 'workout_list.html', {'workouts': workouts})


# Create a workout
@login_required
def workout_create(request):
    """
    Handles creating a new workout.
    """
    if request.method == 'POST':
        # Fetch data from the form
        name = request.POST.get('name')
        day = request.POST.get('day')
        sets = request.POST.get('sets')
        reps = request.POST.get('reps')
        weights = request.POST.get('weights')

        # Create a new workout and associate it with the logged-in user
        Exercise.objects.create(
            user=request.user,
            name=name,
            day=day,
            sets=sets,
            reps=reps,
            weights=weights
        )
        return redirect('workout-list')

    return render(request, 'workout_form.html')


# Update a workout
@login_required
def workout_update(request, pk):
    """
    Handles updating an existing workout.
    """
    workout = get_object_or_404(Exercise, pk=pk, user=request.user)

    if request.method == 'POST':
        # Update workout fields
        workout.name = request.POST.get('name')
        workout.day = request.POST.get('day')
        workout.sets = request.POST.get('sets')
        workout.reps = request.POST.get('reps')
        workout.weights = request.POST.get('weights')
        workout.save()
        return redirect('workout-list')

    return render(request, 'workout_form.html', {'workout': workout})


# Delete a workout
@login_required
def workout_delete(request, pk):
    """
    Handles deleting an existing workout.
    """
    workout = get_object_or_404(Exercise, pk=pk, user=request.user)

    if request.method == 'POST':
        # Delete the workout
        workout.delete()
        return redirect('workout-list')

    return render(request, 'workout_confirm_delete.html', {'workout': workout})

# genric veiw test 

class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'all_workouts.html'  # Specify your template name
    context_object_name = 'workout_genric'  # Name for the list in the template (optional)
    login_url = 'my-login'

    def get_queryset(self):
        """
        Return workouts linked to the logged-in user.
        """
        return Exercise.objects.filter(user=self.request.user)