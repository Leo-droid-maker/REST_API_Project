from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from userapp.models import User
from userapp.serializers import UserModelSerializer, UserModelSerializerWithStaffInformation


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializerWithStaffInformation
        return UserModelSerializer
