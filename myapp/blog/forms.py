from django import forms
from django import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'location', 'content']