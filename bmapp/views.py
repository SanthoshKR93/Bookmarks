from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Link
from .serializers import LinkSerializer,LoginSerializer,UserSerializer
from rest_framework import status
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.contrib.auth.models import User

class Get_Link_List(APIView):
   def get(self, request):
      author = request.user.id

      links = Link.objects.all()
      #links = Link.objects.filter(author=self.request.user)
      serializer = LinkSerializer(links, many=True)
      return Response(serializer.data)

   def post(self, request):
      serialized = LinkSerializer(data=request.data)
      if serialized.is_valid():
         serialized.save()
         return Response(serialized.data, status=status.HTTP_201_CREATED)
      return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)   

class LoginView(APIView):
   model = User
   def post(self,request):
      serializer = LoginSerializer(data = request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data["user"]
      django_login(request, user)
      token, created = Token.objects.  get_or_create(user=user)    # created boolean true or false
      return Response({"token":token.key,"author":request.user.id}, status=200)



class LogoutView(APIView):
   authentication_classes = (TokenAuthentication, )
   def post(self, request):
      django_logout(request)
      return Response(status=204)

class UserCreate(generics.CreateAPIView):
    """
    Create a User
    """
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()
