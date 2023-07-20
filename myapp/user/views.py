from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .fomrs import RegisterForm, LoginForm, ProfileForm
from .models import Profile

User = get_user_model()

### Registration
class Registration(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        
        form = RegisterForm()
        context = {
            "title": "Register",
            "form": form
        }
        return render(request, 'user/user_register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('/')
        context = {
            "title": "Register",
            "form": form
        }
        return render(request, 'user/user_register.html', context)


### Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            
            if user:
                login(request, user)
                return redirect('/')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)
        

### Logout
class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')
        pass

### Profile
class ProfileView(LoginRequiredMixin, View):

    def get (self, request):
        profile = Profile.objects.get(user=request.user.pk)
        context = {
            "title": "Profile",
            "profile": profile
        }
        return render(request, 'user/user_profile.html', context)


class ProfileWrite(View):
    
    def get (self, request):
        form = ProfileForm()
        context = {
            "title":"ProfileWrite",
            "form":form
        }
        return render(request, 'user/post_profile_write.html', context)
    
    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save()
            profile.save()
            return redirect('user:pf-write')
        
        context = {
            "form": form
        }
        return render(request, 'user/post_profile_write.html', context)