from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from userapp.models import User
from userapp.serializers import UserModelSerializer


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
