
from rest_framework import serializers

from movie_user.models import UserModel, Letter


class UserModelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ("url","id","username","password","phone","is_delete","permission")


class LetterSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Letter
        fields = ("url","id","letter")

