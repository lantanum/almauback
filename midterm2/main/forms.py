from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ArticleForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = Article
        fields = ["topic", "text", "picture"]


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ["name", "description"]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["text"]