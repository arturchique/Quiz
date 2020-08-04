from django.shortcuts import render
from .models import *
from rest_framework import generics, permissions
from .serializers import *


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserListSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


def clean_all(request):
    User.objects.all().delete()