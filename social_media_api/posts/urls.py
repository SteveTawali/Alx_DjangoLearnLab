from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import user_feed

urlpatterns = [
    path('feed/', user_feed, name='user-feed'),
]

from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]

urlpatterns = [
    path('like/<int:pk>/', LikePostView.as_view(), name='like-post'),
    path('unlike/<int:pk>/', UnlikePostView.as_view(), name='unlike-post'),
]