from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .serializers import (
    UserPostSerializer, UserPostListSerializer, \
        UserPostDetailSerializer, PostCommentSerializer 
    )
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view

from .models import *
import requests

# Create your views here.

class UserPostListAPI(viewsets.ModelViewSet):    
        queryset = Post.objects.all()
        serializer_class = UserPostListSerializer
        lookup_field = 'post_id'

def postsList(request):
    response = requests.get('http://localhost:8000/user-post-list/')
    user_posts = response.json()
    context = {
        'posts': user_posts
    }
    return render(request, 'post_list.html', context)


class UserPostAPI(viewsets.ViewSet):
    def create(self, request):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'post_title':serializer.validated_data['post_title'],
                'post_body': serializer.validated_data['post_body'],
                # 'created_at': serializer.validated_data['created_at'],
                # 'updated_at': serializer.validated_data['updated_at'],
                'message': 'Post Created Successfully !'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def newPost(request):
    response = requests.get('http://localhost:8000/create-post/')
    create_post = response.json()
    if 'add_post' in request.POST:
        if request.method == 'POST':
            
            title = request.POST.get('title')
            post_body = request.POST.get('post_body')
            if title and post_body:
                post_created = Post.objects.create(post_title = title, post_body = post_body)
    context = {
        'create_post': create_post
    }
    return render(request, 'create_post.html', context)


class UserPostDetailAPI(viewsets.ModelViewSet):    
        queryset = Post.objects.all()
        serializer_class = UserPostListSerializer

@api_view(['GET'])
def userPostDetailAPI(request, pk):
    """
    Retrieve a post instance.
    """
    try:
        post_obj = Post.objects.get(pk=pk)
        serializer = UserPostDetailSerializer(post_obj, many=False, context = {'request':request})
        return Response(serializer.data)
    except Post.DoesNotExist:
        raise Http404

def getPost(request, id):
    response = requests.get(f'http://localhost:8000/post-detail/{id}/')
    post_detail = response.json()
    context = {
        'post_detail': post_detail,
    }
    return render(request, 'post_detail.html', context)


@api_view(['POST'])
def userPostCommentAPI(request, pk):
    """
    Retrieve a post instance.
    """
    try:
        post_obj = Post.objects.get(pk=pk)
        serializer = PostCommentSerializer(post_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Post.DoesNotExist:
        raise Http404


