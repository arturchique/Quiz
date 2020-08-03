from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/list', UserListView.as_view()),
    path('user/create', UserCreateView.as_view()),
]