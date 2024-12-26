from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserSerializer

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

# Create your views here.