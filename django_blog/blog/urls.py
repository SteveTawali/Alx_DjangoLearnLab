from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", profile, name="profile"),
]


from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Add this line for creating new posts
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),  # Add this line for editing posts
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Add this line for deleting posts
]