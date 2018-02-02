from rest_framework import serializers
from project.tasks.models import Task, Account, Plan, Task, Tag

from django.contrib.auth.models import User


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = Account
        fields = ('id', 'url', 'user', 'nickname')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    account = AccountSerializer()
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True, required=False)
    plans = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='plan-detail'
    )
    tags = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tag-detail'
    )
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-detail'
    )

    class Meta:
        model = User
        fields = ('id', 'url', 'account', 'username', 'email', 'password', 'is_staff', 'plans', 'tags', 'tasks')

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        print(validated_data)
        user = User.objects.create(**validated_data)
        account = Account.objects.create(user=user, **account_data)
        user.account = account
        user.save()
        return user

    def update(self, instance, validated_data):
        account_data = validated_data.pop('account')
        account = instance.account
        serializer = AccountSerializer(account, data=account_data)
        assert serializer.is_valid()
        serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'url', 'owner', 'created', 'name', 'detail', 'tasks')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'url', 'owner', 'created', 'name', 'tasks')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    plan = serializers.HyperlinkedRelatedField(queryset=Plan.objects.all(), required=False, view_name='plan-detail')
    tags = serializers.HyperlinkedRelatedField(many=True, queryset=Tag.objects.all(), required=False, view_name='tag-detail')
    is_all_day = serializers.BooleanField(default=True)

    class Meta:
        model = Task
        fields = (
            'id', 'url', 'owner', 'created',
            'plan', 'title', 'content', 'label', 'tags',
            'is_finish', 'finished',
            'is_all_day', 'begin', 'end',
        )
