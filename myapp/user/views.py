from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .fomrs import RegisterForm, LoginForm


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
            "title": "Login",
            "form": form
        }
        return render(request, 'user/user_login.html', context)
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, '로그인에 실패하였습니다. 다시 시도해주시길 바랍니다.')
        else:
            messages.error(request, '입력된 정보가 올바르지 않습니다. 다시 확인해주시길 바랍니다.')

        context = {
            'form': form
        }
        return render(request, 'user/user_login.html', context)
        