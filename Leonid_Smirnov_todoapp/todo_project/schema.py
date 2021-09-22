from graphene import (
    ObjectType,
    Schema,
    List,
    Field,
    Int,
    String,
    Mutation as GrapheneMutation,
    ID as GrapheneID
)
from graphene_django import DjangoObjectType
from todoapp.models import ToDo, Project
from userapp.models import User


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class UserMutation(GrapheneMutation):
    class Arguments:
        first_name = String(required=True)
        id = GrapheneID()

    user = Field(UserType)

    @classmethod
    def mutate(cls, root, info, first_name, id):
        user = User.objects.get(pk=id)
        user.first_name = first_name
        user.save()
        return UserMutation(user=user)


class Mutation(ObjectType):
    update_user = UserMutation.Field()


class Query(ObjectType):
    all_todos = List(ToDoType)
    all_projects = List(ProjectType)
    all_users = List(UserType)
    user_by_id = Field(UserType, id=Int(required=True))
    projects_by_username = List(ProjectType, name=String(required=False))

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_projects_by_username(root, info, name=None):
        projects = Project.objects.all()

        if name:
            return projects.filter(users__username=name)


schema = Schema(query=Query, mutation=Mutation)
