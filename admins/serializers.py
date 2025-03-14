from rest_framework import serializers
from django.contrib.auth.models import User

from admins.models import AdminModel, GroupModel, SuperAdminModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class SuperAdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = SuperAdminModel
        fields = ['id', 'user', 'name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        superadmin = SuperAdminModel.objects.create(user=user, **validated_data)
        return superadmin

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    created_by = SuperAdminSerializer(read_only=True)
    class Meta:
        model = AdminModel
        fields = ['id', 'user', 'name', 'created_by']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        admin = AdminModel.objects.create(user=user, **validated_data)
        return admin
    
class GroupSerializer(serializers.ModelSerializer):
    admin = AdminSerializer(read_only=True)
    teachers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = GroupModel
        fields = ['id', 'name', 'admin', 'teachers', 'students']