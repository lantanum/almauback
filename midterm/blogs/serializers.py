from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    owner = serializers.CharField(max_length=255)
    class Meta:
        model = Blog
        fields = ['title', 'description', 'owner']