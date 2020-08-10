from rest_framework import serializers
from .models import *


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # ['password', 'username', 'email', ]


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        exclude = ('user', )


class ParticipantsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'