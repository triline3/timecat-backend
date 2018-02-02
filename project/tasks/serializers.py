from rest_framework import serializers
from project.tasks.models import Task, Account, Plan, Task, Tag

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    account = serializers.HyperlinkedIdentityField(read_only=True, view_name='account-detail')
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ('url', 'account', 'username', 'email', 'password', 'is_staff', 'plans', 'tags', 'tasks')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Account
        fields = ('url', 'user', 'nickname')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(
            username=user_data['email'],
            password=make_password(user_data['password']),
            email=user_data['email'],
            is_staff=user_data['is_staff']
        )
        account = Account.objects.create(user=user, **validated_data)
        return account
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        if user.email != user_data['email']:
            user.username = user_data['email']
            user.save()
        userSerializer = UserSerializer(instance=instance.user, data=user_data)
        assert userSerializer.is_valid()
        userSerializer.save()
        return super(AccountSerializer, self).update(instance, validated_data)


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('url', 'owner', 'created', 'name', 'detail', 'tasks')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'owner', 'created', 'name', 'tasks')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = (
            'url', 'owner', 'created',
            'plan', 'title', 'content', 'label', 'tags',
            'is_finish', 'finished',
            'is_all_day', 'begin', 'end',
        )
