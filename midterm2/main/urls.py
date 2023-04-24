from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-article', views.create_article, name='create_article'),
    path('create-category', views.create_category, name='create_category'),
    path('article-detail/<int:pk>/', views.article_detail, name = 'article_detail'),
]

