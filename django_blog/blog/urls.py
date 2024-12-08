from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    profile_view,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Auth-related URLs
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", profile_view, name="profile"),
    
    # Blog-related URLs
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]

from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]