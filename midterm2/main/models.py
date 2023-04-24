from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField()



class Article(models.Model):
    topic = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)




