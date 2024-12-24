from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    profile_view,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    # Auth-related URLs
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name='register'),


    # Blog-related URLs
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    
    # Comment-related URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

# urls.py
from blog import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, search_view, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('search/', search_view, name='search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),  # New URL for tag-based filtering
]

from django.urls import path
from .views import PostByTagListView  # Import your view

urlpatterns = [
    # Existing URL patterns
    # e.g., path('some_existing_path/', some_view, name='existing_view_name'),

    # New URL pattern for viewing posts by tag
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),
]