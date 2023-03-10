# capitals/views.py

from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def blogs_handler(request):
    if request.method == 'GET':
        categories = Blog.objects.all()
        serializer = BlogSerializer(categories, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data)
        categories = Blog.objects.all()
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)

def get_blog(iid):
    try:
        blog = Blog.objects.get(id=iid)
        return {
            'blog': blog,
            'status': 200
        }
    except Blog.DoesNotExist as e:
        return {
            'blog': None,
            'status': 404
        }

@csrf_exempt
def blog_handler(request, pk):
    result = get_blog(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'blog not found'}, status=404)

    blog = result['blog']

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data, instance=blog)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, 400)
    if request.method == 'DELETE':
        blog = Blog.objects.get(id=pk)
        blog.delete()
        serializer = BlogSerializer(blog)
        return JsonResponse({'message': 'blog successfully deleted'}, status=200)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)
