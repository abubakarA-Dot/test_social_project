from rest_framework import serializers
import requests
from django.contrib.auth.models import User
from .models import *


class UserPostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ['post_title', 'post_body', 'created_at', 'updated_at']

class PostCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostComment
        fields = ['id','post','user','comment_body', 'created_at', 'updated_at']

class UserPostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['post_title', 'post_body', 'created_at', 'updated_at']

class UserPostListSerializer(serializers.ModelSerializer):
    user_comment = PostCommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id','user_comment','post_title', 'post_body', 'created_at', 'updated_at']
        lookup_field = 'post_id'

    def create(self, validated_data):
        user_comment = validated_data.pop('user_comment')
        post_instance = Post.objects.create(**validated_data)
        for comment in user_comment:
            PostComment.objects.create(user=post_instance,**comment)
        return post_instance

    # def update(self, instance, validated_data):
    #     user = validated_data.pop('user')
    #     user_data = instance.user

    #     instance.id = validated_data.get(
    #         'id', instance.id)
    #     instance.save()

        # post= validated_data.pop('post')
        # post_data = instance.user

        # instance.id = validated_data.get(
        #     'id', instance.id)
        # instance.save()

        # return instance

class UserPostCommentsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostComment
        fields = ['id','post', 'user', 'comment_body', 'comment_reply', 'created_at', 'updated_at']
        # lookup_field = 'comment_id'