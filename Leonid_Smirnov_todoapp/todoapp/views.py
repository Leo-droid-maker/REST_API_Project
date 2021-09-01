from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, ToDoModelSerializer
from todoapp.filters import ProjectFilter, TodoFilter
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class ProjectLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffSetPagination


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = TodoFilter
    pagination_class = ToDoLimitOffSetPagination

    def destroy(self, request, pk=None):
        context = {'request': request}
        queryset = ToDo.objects.all()
        # todo_item = self.queryset.get(pk=kwargs.get("pk"))
        # if todo_item.is_active:
        #     todo_item.is_active = False
        # else:
        #     todo_item.is_active = True
        # todo_item.save()
        todo_item = get_object_or_404(queryset, pk=pk)
        if todo_item.is_active:
            todo_item.is_active = False
        else:
            todo_item.is_active = True
        todo_item.save()

        # queryset = ToDo.objects.all()
        serializer = ToDoModelSerializer(todo_item, context)
        serializer.is_valid()
        return Response(serializer.validated_data)
