from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control bg-dark text-light', 'placeholder': 'Email'}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-light', 'placeholder': 'Password'}),
    )
