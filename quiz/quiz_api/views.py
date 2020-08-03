from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer

