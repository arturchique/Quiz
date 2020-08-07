from django.shortcuts import render
from .models import *
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response({"Data": serializer.data, "status_code": 400})
    # permission_classes = [permissions.IsAdminUser]


class ProfileIdView(APIView):
    def get(self, request, user_id):
        participant = Participant.objects.filter(user=user_id)
        serializer = ParticipantSerializer(participant, many=True)
        return Response({"пользователь": serializer.data})
    def post(self, request):
        participant = request.data.get("participant")
        serializer = Participant(data=participant)
        if serializer.is_valid(raise_exception=True):
            participant_saved = serializer.save()
        return Response({"success": "Participant '{}' created successfully".format(participant_saved.nickname)})


def clean_all(request):
    User.objects.all().delete()


class HelloView(APIView):
    def get(self, request):
        return Response({'data': 'Захар Лох', 'status_code': 400})