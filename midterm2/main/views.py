from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import *
import json


@login_required(login_url="/login")
def home(request):
    articles = Article.objects.all()
    
    if request.method == "POST":
        article_id = request.POST.get("article-id")
        user_id = request.POST.get("user-id")

        if article_id:
            article = Article.objects.filter(id=article_id).first()
            if article and (article.author == request.user):
                article.delete()

    return render(request, 'main/home.html', {"articles": articles})










@login_required(login_url="/login")
def create_article(request):
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            categoryId = request.POST.get('category')
            category = Category.objects.get(id = categoryId)
            picture = form.files.get('picture', None)
            article.picture = picture
            article.category = category
            article.author = request.user
            article.save()
            return redirect("/home")
    else:
        form = ArticleForm()
        
    categories = Category.objects.all()
    return render(request, 'main/create_article.html', {"form": form, "categories": categories})










def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})




@login_required(login_url="/login")
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect("/home")
    else:
        form = CategoryForm()
    return render(request, 'main/create_category.html', {"form": form})


    

@login_required(login_url="/login")
def article_detail(request, pk):
    article = Article.objects.get(id = pk)
    comments = article.comments.filter()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment = form.save()
            return redirect("/home")
    else:
        form = CommentForm()
    return render(request, 'main/article_detail.html', {"form": form, "comments": comments, "article": article})


