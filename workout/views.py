from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .form import UserCreationForm, LoginForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Exercise

# Custom 404 view
def custom_404_view(request, exception):
    """
    Renders a custom 404 error page.
    """
    return render(request, '404.html', status=404)


# Home page view
class HomePage(TemplateView):
    """
    Displays the home page.
    """
    template_name = 'index.html'


# Register a user
def register(request):
    """
    Handles user registration and displays feedback messages.
    """
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('home')
        else:
            messages.error(request, "There was an error with your registration. Please try again.")

    context = {'form': form}
    return render(request, 'register.html', context)


# Login a user
def my_login(request):
    """
    Handles user login and provides feedback messages.
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
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            messages.error(request, "There was an error with your login. Please check your details.")

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
    Logs out the user and displays a feedback message.
    """
    logout(request)
    messages.info(request, "You have been logged out. See you next time!")
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
    Handles creating a new workout with error handling and feedback messages.
    """
    if request.method == 'POST':
        # Extract workout details from POST request
        name = request.POST.get('name', '').strip()
        day = request.POST.get('day', '').strip()
        sets = request.POST.get('sets', '').strip()
        reps = request.POST.get('reps', '').strip()
        weights = request.POST.get('weights', '').strip()

        # Validation for empty fields
        if not all([name, day, sets, reps, weights]):
            messages.error(request, "All fields are required. Please fill in all fields.")
            return render(request, 'workout_form.html', {'error': "All fields are required."})

        try:
            # Validate numeric inputs
            sets = int(sets)
            reps = int(reps)
            weights = float(weights)

            if sets <= 0 or reps <= 0 or weights < 0:
                raise ValueError("Invalid input values.")

            # Save the workout to the database
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
    """
    Handles updating an existing workout and provides feedback messages.
    """
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
    """
    Handles deleting an existing workout and provides feedback messages.
    """
    workout = get_object_or_404(Exercise, pk=pk, user=request.user)

    if request.method == 'POST':
        workout.delete()
        messages.success(request, "Workout deleted successfully!")
        return redirect('workout-list')

    return render(request, 'workout_confirm_delete.html', {'workout': workout})


# Generic view test
class ExerciseListView(LoginRequiredMixin, ListView):
    """
    Generic view to display a paginated list of workouts with search and sorting functionality.
    """
    model = Exercise
    template_name = 'workout_list.html'
    context_object_name = 'workout_genric'
    login_url = 'my-login'
    paginate_by = 10

    def get_queryset(self):
        """
        Filter workouts based on the logged-in user and optional search/sort parameters.
        """
        queryset = Exercise.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')  # Get search query
        sort = self.request.GET.get('sort', 'name')  # Default sort by name

        if query:
            queryset = queryset.filter(name__icontains=query)

        if sort in ['name', 'day', 'sets', 'reps', 'weights']:
            queryset = queryset.order_by(sort)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Add additional context for the template, including total workouts count.
        """
        context = super().get_context_data(**kwargs)
        total_workouts = Exercise.objects.filter(user=self.request.user).count()
        context['title'] = f"{self.request.user.username}'s Workout List"
        context['total_workouts'] = total_workouts
        return context
