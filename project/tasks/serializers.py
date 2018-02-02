from rest_framework import serializers
from project.tasks.models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # date = serializers.DateTimeField(allow_null=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'owner',
            'created',
            'title',
            'detail',
            'date',
            'isDone'
        )


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Task.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks')
