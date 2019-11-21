from django import forms
from .models import Comment

"""Using a form for comments"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username', 'content', 'image', 'rate',)