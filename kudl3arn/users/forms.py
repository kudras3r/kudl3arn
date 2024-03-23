from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from users.models import Profile


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


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=128, required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    tg_link = forms.CharField(widget=forms.TextInput())
    vk_link = forms.CharField(widget=forms.TextInput())
    git_link = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Profile
        fields = ['image', 'tg_link', 'vk_link', 'git_link'] #'image',

    def clean_password(self):
        return self.clean_password
