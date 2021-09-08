from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer
from todoapp.models import Project, ToDo
from userapp.serializers import UserModelSerializer


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'repo_url', 'users')
        # fields = ('__all__')


class ToDoModelSerializer(ModelSerializer):
    user = UserModelSerializer

    class Meta:
        model = ToDo
        fields = '__all__'
