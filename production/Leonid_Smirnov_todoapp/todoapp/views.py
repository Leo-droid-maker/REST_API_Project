from rest_framework.viewsets import ModelViewSet
from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, ToDoModelSerializer, ToDoSerializerBase
from todoapp.filters import ProjectFilter, TodoFilter
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status, permissions


class ProjectLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffSetPagination


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = TodoFilter
    pagination_class = ToDoLimitOffSetPagination

    # def get_serializer_class(self):
    #     if self.request.method in ['GET']:
    #         return ToDoModelSerializer
    #     return ToDoSerializerBase

    def destroy(self, request, pk=None):

        try:
            todo_item = self.get_object()
            if todo_item.is_active:
                todo_item.is_active = False

            todo_item.save()

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
