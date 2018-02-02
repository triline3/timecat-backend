from django.urls import path, include
from rest_framework import routers
from project.tasks import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'plans', views.PlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
