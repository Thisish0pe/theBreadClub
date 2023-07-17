from django.shortcuts import render, redirect
from django.views import View


### 회원가입
class Registration(View):
    
    def get(self, reqeust):
        
