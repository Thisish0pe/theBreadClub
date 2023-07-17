from django.shortcuts import render, redirect
from django.views import View
from .models import Location, Post
from .forms import PostForm


### Post
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
            return redirect('index.html')
        
        context = {
            "form": form
        }
        return render(request, 'blog/post_form.html', context)



class Update(View):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'location': post.location, 'photo':post.photo,'content':post.content})
        context = {
            "title": "PostEdit",
            "form": form,
            "post": post
        }
        return render(request, 'blog/post_edit.html', context)
    
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.location = form.cleaned_data['location']
            post.photo = form.cleaned_data['photo']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)
        context = {
            "title": "PostEdit",
            "form": form
        }
        return render(request, 'blog/post_edit.html', context)


class Delete(View):
    
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('index.html')


class DetailView(View):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {
            "title": "Post",
            "post": post
        }
        return render(request, 'blog/post_detail.html', context)