from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form with username validation.
    """

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        # Retrieve the username from the cleaned data.
        username = self.cleaned_data.get('username')

        # Check if the username already exists in the database.
        if User.objects.filter(username=username).exists():
            # Raise a ValidationError if the username is taken.
            raise ValidationError(
                "This username is already taken. Pick a different one."
            )

        # Return the validated username.
        return username


class LoginForm(AuthenticationForm):
    """
    Custom login form with placeholders and error handling.
    """

    # Add placeholders to enhance the user interface for input fields.
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        )
    )

    def confirm_login_allowed(self, user):
        # Check if the user account is active.
        if not user.is_active:
            # Raise a ValidationError if the account is inactive.
            raise ValidationError(
                "This account is inactive. Please contact support."
            )
