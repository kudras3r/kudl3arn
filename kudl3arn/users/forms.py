from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'text-field_login_input',
        'name': 'login',
        'id': 'login',
        'placeholder': 'Username or Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'text-field_pwd_input',
        'name': 'password',
        'id': 'password',
        'placeholder': 'Password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'login',
        'id': 'login',
        'placeholder': 'Username or Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password1',
        'id': 'password1',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'password2',
        'id': 'password2',
        'placeholder': 'Retype Password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
