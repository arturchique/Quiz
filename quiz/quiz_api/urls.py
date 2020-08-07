from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/list/', UserListView.as_view()),
    path('profile/clean/', clean_all),
    path('profile/<int:user_id>/', ProfileIdView.as_view()),
    path('hello_world/', HelloView.as_view())
]
