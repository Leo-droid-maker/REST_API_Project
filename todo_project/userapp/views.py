from rest_framework.viewsets import ModelViewSet
from userapp.models import User
from userapp.serializers import UserModelSerializer

# Create your views here.


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
