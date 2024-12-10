from django.urls import path
from .views import (
    HomePage,
    workout_list,
    workout_create,
    workout_update,
    workout_delete,
    my_login,
    register,
    user_logout,
    myworkouts,
    ExerciseListView,
    custom_404_view,
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),  # Home page URL
    path('workouts/', workout_list, name='workout-list'),  # List workouts
    path('workouts/new/', workout_create, name='workout-create'),  # Create workout
    path('workouts/<int:pk>/edit/', workout_update, name='workout-update'),  # Update workout

    # You mentioned this path is not needed, so remove if confirmed
    path('workouts/<int:pk>/delete/', workout_delete, name='workout-delete'),  # Delete workout

    path('my-login/', my_login, name='my-login'),  # Login page
    path('register/', register, name='register'),  # Register page
    path('user-logout/', user_logout, name='user-logout'),  # Logout page
    path('myworkouts/', myworkouts, name='myworkouts'),  # User-specific workouts
]


