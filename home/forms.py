
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'dark-input' ,'style': 'background-color: #333; color: white; border: none;'}),
            'content': forms.Textarea(attrs={'class': 'dark-textarea', 'style': 'background-color: #333; color: white; border: none;'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'dark-textarea', 'style': 'background-color: #444; color: white; border: none;', 'placeholder': 'comments here...'}),
        }
        labels = {
            'content': '',
        }

    