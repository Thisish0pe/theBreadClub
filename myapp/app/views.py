from django.shortcuts import render, redirect
from django.views import View
from blog.models import Post


class IndexMain(View):

    def get(self, request):
        posts = Post.objects.all()
        context = {
            "title": "Blog",
            "posts": posts
        }
        return render(request, 'index.html', context)