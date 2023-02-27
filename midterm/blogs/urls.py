from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('blogs', views.blogs_handler),
    path('blogs/<int:pk>', views.blog_handler)
]

urlpatterns = format_suffix_patterns(urlpatterns)
