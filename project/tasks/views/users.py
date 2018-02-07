from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets

from project.tasks.serializers import UserSerializer
from project.tasks.serializers import AccountSerializer
from project.tasks.models import Account


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'
    lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

    def perform_create(self, serializer):
        if 'password' in serializer.validated_data.keys():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        if 'username' not in serializer.validated_data.keys():
            serializer.validated_data['username'] = serializer.validated_data['email']
        serializer.save()

    def perform_update(self, serializer):
        if 'password' in serializer.validated_data.keys():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        serializer.save()


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
