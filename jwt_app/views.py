from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


from .serializers import *
from .models import *

class Register(APIView):
    def post(self,request):
        serializer = UserSerialzier(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                "status":1,
                "message":"User register succesfully",
                "data":serializer.data,
                "tokens": {
                    "refresh": str(refresh),
                    "access": access_token
                }
            })
        else:
            return Response({
                "status":0,
                "message":"An error Ocurred",
                "data":serializer.errors
            })
        
            
class LoginCheck(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("USER IS ", request.user.name)
        return Response({"message": "You are authenticated!"})
    
    

class LogoutView(APIView):
    def post(self, request):
        try:
            # Get the refresh token from the request
            refresh_token = request.data.get("refresh")
            
            if not refresh_token:
                return Response({"detail": "Refresh token is required"})

            # Validate and blacklist the refresh token
            token = RefreshToken(refresh_token)
            token.blacklist()

            print("Refresh token blacklisted successfully.")
            return Response({"detail": "Successfully logged out"})

        except Exception as e:
            # Log the exception to understand the issue
            print("Error during logout:", str(e))
            return Response({"detail": str(e)})
    def get(self,request):
        return Response("Hello")
    

            
