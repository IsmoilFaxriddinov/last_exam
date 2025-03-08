from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StudentModel
from admins.serializers import AdminSerializer, UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    managed_by = AdminSerializer(read_only=True)

    class Meta:
        model = StudentModel
        fields = ['id', 'user', 'name', 'managed_by']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        student = StudentModel.objects.create(user=user, **validated_data)
        return student