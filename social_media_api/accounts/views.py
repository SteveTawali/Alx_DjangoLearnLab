from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ProfileView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }, status=status.HTTP_200_OK)
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    """
    Handles user registration and token generation.
    """
    def post(self, request):
        # Debug: Print incoming data
        print("Request data:", request.data)
        
        serializer = UserSerializer(data=request.data)
        
        # Validate serializer data
        if serializer.is_valid():
            # Save user and generate token
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            
            # Debug: Print token for the user
            print("Generated Token:", token.key)
            
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        
        # Debug: Print serializer errors
        print("Serializer Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if user_to_follow == request.user:
        return Response({"error": "You cannot follow yourself."}, status=400)

    request.user.following.add(user_to_follow)
    return Response({"message": f"You are now following {user_to_follow.username}."})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if user_to_unfollow == request.user:
        return Response({"error": "You cannot unfollow yourself."}, status=400)

    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}."})
# Create your views here.

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response

CustomUser = get_user_model()

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user_to_follow = get_object_or_404(CustomUser, username=username)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user_to_unfollow = get_object_or_404(CustomUser, username=username)
        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {username}."}, status=status.HTTP_200_OK)