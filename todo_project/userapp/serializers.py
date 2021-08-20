from django.db.models import fields
from rest_framework.serializers import HyperlinkedModelSerializer
from userapp.models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
