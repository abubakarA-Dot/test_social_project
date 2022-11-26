
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()

router.register('user-post-list', views.UserPostListAPI, basename='userPostList')
# router.register('user-post-list/pk/post_id', views.UserPostListAPI, basename='userPostDetail')
router.register('create-post', views.UserPostAPI, basename='createPost')


app_name = 'social_media'

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    # MVT url
    path('post-list/', views.postsList, name='posts_list'),
    # MVT urls
    path('new-post/', views.newPost, name= 'new_post'),
    # API
    path('post-detail/<str:pk>/', views.userPostDetailAPI),
    #MVT url
    path('post/detail/<str:id>/', views.getPost, name='getPost'),

    path('comment/<str:pk>/', views.userPostCommentAPI),
]
