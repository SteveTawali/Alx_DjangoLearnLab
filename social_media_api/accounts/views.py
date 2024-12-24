from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserSerializer

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