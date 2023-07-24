from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Location, Post, Comment
from .forms import PostForm, CommentForm


### Post
class Write(LoginRequiredMixin, View):
    
    def get(self, request):
        form = PostForm()
        locations = Location.objects.all()
        context = {
            "title": "PostWrite",
            "form": form,
            "locations": locations
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self, request):
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('/')
        
        context = {
            "form": form
        }
        return render(request, 'blog/post_form.html', context)



class Update(View):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'photo':post.photo,'content':post.content})
        locations = Location.objects.all()
        context = {
            "title": "PostEdit",
            "form": form,
            "locations": locations,
            "post": post
        }
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.location = form.cleaned_data['location']
            post.content = form.cleaned_data['content']
            if form.cleaned_data['photo']:
                post.photo = form.cleaned_data['photo']
            # if 'clear_photo' in request.POST:
            #     post.photo.delete()
            # else: print('----------이미지 삭제 구현X---------')
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
        return redirect('/')


class DetailView(View):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        comment_form = CommentForm()
        context = {
            "title": "Post",
            "post": post,
            "comments": comments,
            "comment_form": comment_form
        }
        return render(request, 'blog/post_detail.html', context)


### Search
class Search(View):
    def get(self, request):
        query = request.GET.get('search')
        posts = []
        if query:
            posts = Post.objects.filter(
                Q(title__icontains=query) |
                Q(location__name__icontains=query) |
                Q(writer__email__icontains=query)
            )
        return render(request, 'blog/post_search.html', {'posts': posts})


### Comment
class CommentWrite(LoginRequiredMixin, View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user
            comment = Comment.objects.create(post=post, content=content, writer=writer)
            return redirect('blog:detail', pk=post.pk)
        context = {
            "title": "CommentWrite",
            "post": post,
            "form": form
        }
        return render(request, 'blog/post_detail.html', context)
    

class CommentUpdate(View):

    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('blog:detail', pk=comment.post.pk)

        post = comment.post
        comments = Comment.objects.filter(post=post)
        context = {
            "title": "Post",
            "post": post,
            "comments": comments,
            "comment_form": form
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(View):

    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        post_id = comment.post.id
        comment.delete()
        return redirect('blog:detail', pk=post_id)


### Like
class LikeToggle(LoginRequiredMixin, View):
    def post(self, request, pk):
        pass