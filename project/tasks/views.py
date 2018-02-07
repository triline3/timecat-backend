# from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from project.tasks.models import Task, Tag, Account, Plan
from project.tasks.serializers import UserSerializer, TaskSerializer, TagSerializer
from project.tasks.serializers import AccountSerializer, PlanSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'
    lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

    def perform_create(self, serializer):
        if 'password' in serializer.validated_data.keys():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        if 'username' not in serializer.validated_data.keys():
            serializer.save(username=serializer.validated_data['email'])

    def perform_update(self, serializer):
        if 'password' in serializer.validated_data.keys():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        # serializer.save(username=serializer.validated_data['email'])


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
