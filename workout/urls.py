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
    # Route for the home page, which serves as the entry point for the application
    path('', HomePage.as_view(), name='home'),

    # Route to display a list of all workouts for the logged-in user
    path(
        'workouts/',
        workout_list,
        name='workout-list'
    ),

    # Route to create a new workout, accessible only to logged-in users
    path(
        'workouts/new/',
        workout_create,
        name='workout-create'
    ),

    # Route to update an existing workout by its primary key (pk), for authorized users
    path(
        'workouts/<int:pk>/edit/',
        workout_update,
        name='workout-update'
    ),

    # Route to delete a workout by its primary key (pk), ensuring only the owner can delete
    path(
        'workouts/<int:pk>/delete/',
        workout_delete,
        name='workout-delete'
    ),

    # Route for the login page, allowing users to authenticate
    path(
        'my-login/',
        my_login,
        name='my-login'
    ),

    # Route for the registration page, enabling new users to sign up
    path(
        'register/',
        register,
        name='register'
    ),

    # Route for logging out the user and redirecting them to the homepage
    path(
        'user-logout/',
        user_logout,
        name='user-logout'
    ),

    # Route for viewing the logged-in user's personal workout dashboard
    path(
        'myworkouts/',
        myworkouts,
        name='myworkouts'
    ),
]
