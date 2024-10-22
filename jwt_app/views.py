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
            serializer.save()
            return Response({
                "status":1,
                "message":"User register succesfully",
                "data":{serializer.data}
            })
        else:
            return Response({
                "status":0,
                "message":"An error Ocurred",
                "data":serializer.errors
            })
        
class Login(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        
        user = authenticate(email=email,password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            serializer = UserSerialzier(user)
        
            return Response({
                "status":1,
                "message":"success",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user":serializer.data
            })
        else:
            return Response({
                "status":0,
                "message":"invalid credentials"
            })
            
            
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"})
            
