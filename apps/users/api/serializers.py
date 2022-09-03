from pyexpat import model
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    #encrypt password new user
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password']) #encrypt
        user.save()
        return user

    #encrypt password update user
    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    # serializer representation
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'password': instance.password

        }