from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),  # Home page URL
    path('register/', views.register, name='register'),  # Fixed URL and name
]
