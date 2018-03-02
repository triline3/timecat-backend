from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from project.tasks.models import Task, Account, Plan, Task, Tag, Note

from django.contrib.auth.models import User


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail',
        lookup_field='email'
    )
    nickname = serializers.CharField(required=False)
    class Meta:
        model = Account
        fields = ('user', 'nickname')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    account = AccountSerializer(required=False)
    username = serializers.CharField(required=False, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
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
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='email'
    )

    class Meta:
        model = User
        fields = ('url', 'account', 'username', 'email', 'password', 'plans', 'tags', 'tasks')

    def create(self, validated_data):
        account_data = {}
        if 'account' in validated_data.keys():
            account_data = validated_data.pop('account')
        user = User.objects.create(**validated_data)
        account = Account.objects.create(user=user, **account_data)
        user.account = account
        user.save()
        return user

    def update(self, instance, validated_data):
        account_data = {}
        if 'account' in validated_data.keys():
            account_data = validated_data.pop('account')
        account = instance.account
        serializer = AccountSerializer(account, data=account_data)
        assert serializer.is_valid()
        serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail',
        lookup_field='email'
    )
    tasks = serializers.HyperlinkedRelatedField(many=True, queryset=Task.objects.all(), required=False, view_name='task-detail')

    class Meta:
        model = Plan
        fields = ('url', 'owner', 'created_datetime', 'name', 'detail', 'tasks')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail',
        lookup_field='email'
    )
    tasks = serializers.HyperlinkedRelatedField(many=True, queryset=Task.objects.all(), required=False, view_name='task-detail')

    class Meta:
        model = Tag
        fields = ('url', 'owner', 'created_datetime', 'name', 'tasks')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    plan = serializers.HyperlinkedRelatedField(queryset=Plan.objects.all(), required=False, view_name='plan-detail')
    tags = serializers.HyperlinkedRelatedField(many=True, queryset=Tag.objects.all(), required=False, view_name='tag-detail')
    is_all_day = serializers.BooleanField(default=True)
    owner = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail',
        lookup_field='email'
    )

    class Meta:
        model = Task
        fields = (
            'url', 'owner', 'created_datetime',
            'plan', 'title', 'content', 'label', 'tags',
            'is_finished', 'finished_datetime',
            'is_all_day', 'begin_datetime', 'end_datetime',
        )


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail',
        lookup_field='email'
    )

    class Meta:
        model = Note
        fields = ('url', 'owner', 'title', 'content', 'created_datetime')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
