from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),  # Home page URL
    path('register/', views.register, name='register'),  # Fixed URL and name
    path('my-login/', views.my_login, name='my-login'),
    path('user-logout/', views.user_logout, name='user-logout'),




    path('myworkouts/', views.myworkouts, name='myworkouts'),



]
