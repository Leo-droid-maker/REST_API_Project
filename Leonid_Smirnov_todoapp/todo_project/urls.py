from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userapp.views import UserCustomViewSet
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet


router = DefaultRouter()

router.register('projects', ProjectModelViewSet)
router.register('todos', ToDoModelViewSet, basename='todo')
router.register('users', UserCustomViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
    path('viewsets/', include(router.urls)),
    path('admin/', admin.site.urls),
]
