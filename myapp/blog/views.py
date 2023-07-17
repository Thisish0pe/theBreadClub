from django.shortcuts import render, redirect
from django.views import View
from .models import Location, Post
from .forms import PostForm

class Write(View):
    
    def get(self, request):
        form = PostForm()
        context = {
            "title": "PostWrite",
            "form": form
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            # writer 추후 변경 
            post.save()
            return redirect('index')