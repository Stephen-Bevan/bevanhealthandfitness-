from django.urls import path
from . import views
from .views import (
    HomePage, 
    WorkoutListView, 
    WorkoutCreateView, 
    WorkoutUpdateView, 
    WorkoutDeleteView
)

urlpatterns = [
    # General app routes
    path('', HomePage.as_view(), name='home'),  # Home page URL
    path('register/', views.register, name='register'),  # Register page
    path('my-login/', views.my_login, name='my-login'),  # Login page
    path('user-logout/', views.user_logout, name='user-logout'),  # Logout page

    # Workout-related routes
    path('workouts/', WorkoutListView.as_view(), name='workout-list'),  # List of workouts
    path('workouts/new/', WorkoutCreateView.as_view(), name='workout-create'),  # Create a new workout
    path('workouts/<int:pk>/edit/', WorkoutUpdateView.as_view(), name='workout-update'),  # Edit a workout
    path('workouts/<int:pk>/delete/', WorkoutDeleteView.as_view(), name='workout-delete'),  # Delete a workout
    path('myworkouts/', views.myworkouts, name='myworkouts'),  # User-specific workouts
]
