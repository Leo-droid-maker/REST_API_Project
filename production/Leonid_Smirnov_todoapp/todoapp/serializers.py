from django.db import models
from django.forms import fields
from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer, PrimaryKeyRelatedField
from todoapp.models import Project, ToDo
from userapp.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    # users = StringRelatedField(many=True)
    # users = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'repo_url', 'users')
        # fields = '__all__'


class ToDoSerializerBase(ModelSerializer):

    class Meta:
        model = ToDo
        fields = ('id', 'text', 'project', 'user')


class ToDoModelSerializer(ModelSerializer):
    # user = UserModelSerializer

    class Meta:
        model = ToDo
        fields = ('id', 'text', 'project', 'user')
        # fields = '__all__'
