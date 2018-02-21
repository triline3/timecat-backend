from project.tasks.models import Task, Tag, Plan, Note
from project.tasks.serializers import TaskSerializer
from project.tasks.serializers import TagSerializer
from project.tasks.serializers import PlanSerializer
from project.tasks.serializers import NoteSerializer

from rest_framework import viewsets
from rest_framework import permissions


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
