from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .models import Post, Comment
from .forms import PostForm, CommentForm


User = get_user_model()


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
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save()
            # writer 추후 변경 
            post.save()
            return redirect('/')
        
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
    
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.location = form.cleaned_data['location']
            post.content = form.cleaned_data['content']
            if form.cleaned_data['photo']:
                post.photo = form.cleaned_data['photo']
            if 'clear_photo' in request.POST:
                post.photo.delete()
            else: print('----------이미지 삭제 구현X---------')
            form.save()
            print('-----------save---------------')
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


### Comment
class CommentWrite(View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            # writer 추후 추가
            comment = Comment.objects.create(post=post, content=content)
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