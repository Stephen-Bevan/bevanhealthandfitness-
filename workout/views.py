from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .form import UserCreationForm, LoginForm
from .models import Exercise

# Custom 404 view
def custom_404_view(request, exception):
    # Render a user-friendly 404 error page when a page is not found
    return render(request, '404.html', status=404)

# Home page view
class HomePage(TemplateView):
    # Render the homepage with a basic template
    template_name = 'index.html'

# Register a user
def register(request):
    # Handles user registration by validating form input and saving new users
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('home')
        messages.error(request, "There was an error with your registration. Please try again.")

    context = {'form': form}
    return render(request, 'register.html', context)

# Login a user
def my_login(request):
    # Authenticates and logs in a user, with error handling for invalid credentials
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')
            messages.error(request, "Invalid username or password. Please try again.")
        else:
            messages.error(request, "There was an error with your login. Please check your details.")

    context = {'form': form}
    return render(request, 'my-login.html', context)

# My workouts view
@login_required(login_url='my-login')
def myworkouts(request):
    # Display the user's workouts dashboard for logged-in users
    return render(request, 'myworkouts.html')

# User logout
def user_logout(request):
    # Logs out the current user and redirects to the homepage with a message
    logout(request)
    messages.info(request, "You have been logged out. See you next time!")
    return redirect('home')

# List workouts
@login_required
def workout_list(request):
    # Fetch and display all workouts belonging to the logged-in user
    workouts = Exercise.objects.filter(user=request.user)
    return render(request, 'workout_list.html', {'workouts': workouts})

# Create a workout
@login_required
def workout_create(request):
    # Allow users to add a new workout with input validation for numeric fields
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        day = request.POST.get('day', '').strip()
        sets = request.POST.get('sets', '').strip()
        reps = request.POST.get('reps', '').strip()
        weights = request.POST.get('weights', '').strip()

        if not all([name, day, sets, reps, weights]):
            messages.error(request, "All fields are required. Please fill in all fields.")
            return render(request, 'workout_form.html', {'error': "All fields are required."})

        try:
            sets = int(sets)
            reps = int(reps)
            weights = float(weights)

            if sets <= 0 or reps <= 0 or weights < 0:
                raise ValueError("Invalid input values.")

            Exercise.objects.create(
                user=request.user,
                name=name,
                day=day,
                sets=sets,
                reps=reps,
                weights=weights
            )
            messages.success(request, "Workout created successfully!")
            return redirect('workout-list')
        except ValueError:
            messages.error(request, "Invalid input for sets, reps, or weights. Please ensure they are positive numbers.")

    return render(request, 'workout_form.html')

# Update a workout
@login_required
def workout_update(request, pk):
    # Enable users to edit an existing workout if they own it
    workout = get_object_or_404(Exercise, pk=pk, user=request.user)

    if request.method == 'POST':
        workout.name = request.POST.get('name')
        workout.day = request.POST.get('day')
        workout.sets = request.POST.get('sets')
        workout.reps = request.POST.get('reps')
        workout.weights = request.POST.get('weights')
        workout.save()
        messages.success(request, "Workout updated successfully!")
        return redirect('workout-list')

    return render(request, 'workout_form.html', {'workout': workout})

# Delete a workout
@login_required
def workout_delete(request, pk):
    # Allow users to delete a workout they own with confirmation
    workout = get_object_or_404(Exercise, pk=pk, user=request.user)

    if request.method == 'POST':
        workout.delete()
        messages.success(request, "Workout deleted successfully!")
        return redirect('workout-list')

    return render(request, 'workout_confirm_delete.html', {'workout': workout})

# Generic view test
class ExerciseListView(LoginRequiredMixin, ListView):
    # Display a list of workouts with pagination and optional search and sorting
    model = Exercise
    template_name = 'workout_list.html'
    context_object_name = 'workout_generic'
    login_url = 'my-login'
    paginate_by = 10

    