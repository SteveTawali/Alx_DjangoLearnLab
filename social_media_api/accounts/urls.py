from django.urls import path
from .views import RegisterView
from .views import LoginView
from .views import ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),  # Add the login route here
    path('profile/', ProfileView.as_view(), name='profile'),
]

from .views import follow_user, unfollow_user

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]

from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]