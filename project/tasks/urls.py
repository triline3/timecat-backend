from django.urls import path, include
from rest_framework import routers
from project.tasks.views.tasks import TaskViewSet
from project.tasks.views.tasks import TagViewSet
from project.tasks.views.tasks import PlanViewSet
from project.tasks.views.tasks import NoteViewSet
from project.tasks.views.users import UserViewSet
from project.tasks.views.users import AccountViewSet
from project.tasks.views.auth import LoginView, LogoutView, ExampleView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'tags', TagViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('auth_test/', ExampleView.as_view()),
]
