from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .fomrs import RegisterForm, LoginForm
from .models import Profile


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
            user = authenticate(username=email, password=password) # True, False
            
            if user:
                login(request, user)
                return redirect('/')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)
        

### Logout


### Profile
class ProfileView(View):
    
    def get (self, request):
        profile = Profile.objects.get(user=request.user)
        context = {
            "title": "Profile",
            "profile": profile
        }
        return render(request, 'user/user_profile.html', context)
