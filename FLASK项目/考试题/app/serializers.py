from rest_framework import serializers

from app.models import UserModel, BlockModel, CollectModel


class BlockModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlockModel
        fields = ("id", "title", "content")


class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        blocks = BlockModelSerializers(many=True, read_only=True)
        model = UserModel
        fields = ("id", "name", "password", "phone", "mail", "is_delete", "permission", 'blocks')
