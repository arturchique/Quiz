from rest_framework import serializers
from .models import *


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # ['password', 'username', 'email', ]


class ParticipantSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nickname = models.CharField(verbose_name='username', max_length=30)
    rating = models.FloatField(verbose_name='rating', default=0.0)
    bio = models.CharField(verbose_name='about', max_length=256, blank=True)
    avatar = models.ImageField(null=True, blank=True, verbose_name='avatar')
    # user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Participant.objects.create(**validated_data)