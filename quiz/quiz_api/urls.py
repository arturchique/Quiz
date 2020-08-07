from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('profile/list/', UserListView.as_view()),
    path('profile/clean/', clean_all),
    path('profile/<int:user_id>/', ProfileIdView.as_view()),
    path('hello_world/', csrf_exempt(HelloView.as_view()))
]
