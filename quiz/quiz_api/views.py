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
        return Response({"Data": serializer.data, "status_code": 200})
    # permission_classes = [permissions.IsAdminUser]


class ProfileIdView(APIView):
    def get(self, request, user_id):
        participant = Participant.objects.filter(user=user_id)
        serializer = ParticipantsViewSerializer(participant, many=True)
        return Response({"пользователь": serializer.data})
    def post(self, request, user_id):
        if request.user.id != user_id:
            participant = request.data
            serializer = ParticipantsSerializer(data=participant)
            if serializer.is_valid(raise_exception=True):
                nickname = serializer.data["nickname"]
                rating = serializer.data["rating"]
                bio = serializer.data["bio"]
                avatar = serializer.data["avatar"]

                new_participant = Participant.objects.create(nickname=nickname, rating=rating, bio=bio, avatar=avatar)
                user = User.objects.get(id=user_id)
                user.participant_set.add(new_participant)
            return Response({'success': f"user {user.id} created"})
        else:
            return Response({'unsuccessful': 'данный пользователь не имеет доступа к этому методу'})

        # if serializer.is_valid(raise_exception=False):
        #     # participant_saved = serializer.save()
        #     nickname = serializer.data['nickname']
        #     rating = serializer.data['rating']
        #     bio = serializer.data['bio']
        #     avatar = serializer.data['avatar']
        #
        #     new_participant = Participant.objects.create(nickname=nickname, rating=rating, bio=bio, avatar=avatar)
        #     user = User.objects.get(id=user_id)
        #     user.participant_set.add(new_participant)
        #
        #     # return Response({"success": "Participant '{}' created successfully".format(nickname)})
        # return Response({'data': serializer.data})
        # return Response({"success": f"Participant {serializer.data} created"})


def clean_all(request):
    return Response({Participant.objects.all()})


class HelloView(APIView):
    def get(self, request):
        participant = Participant.objects.all()
        serializer = ParticipantsViewSerializer(participant, many=True)
        return Response({'data': serializer.data})