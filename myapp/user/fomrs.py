from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email']


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        field = ['email', 'password']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['nickname', 'photo', 'blog_url']
