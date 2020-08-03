from rest_framework import serializers
from .models import *


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'groups', 'user_permissions']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_active', 'groups', 'rating', 'user_permissions', 'last_login', 'is_superuser']