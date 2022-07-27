from django import forms
from django.forms import fields
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__' 
        exclude = ['owner','owner_image','slug']