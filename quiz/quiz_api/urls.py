from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/list/', UserListView.as_view()),
    path('profile/create/', UserCreateView.as_view()),
    path('profile/clean', clean_all),
]
