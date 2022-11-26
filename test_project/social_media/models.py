from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_body = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post_title)

    def get_absolute_url(self):
        return reverse('id', kwargs={'id':self.id})

class PostComment(models.Model):
    post = models.ForeignKey(Post, related_name='user_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    comment_body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_reply = models.ForeignKey('self',related_name='comment_replies', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.comment_body)
