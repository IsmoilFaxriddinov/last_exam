from rest_framework import serializers

from .models import TeacherModel, HomeworkModel
from admins.serializers import AdminSerializer, GroupSerializer, UserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    managed_by = AdminSerializer(read_only=True)

    class Meta:
        model = TeacherModel
        fields = ['id', 'user', 'name', 'managed_by']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(user_data)
        teacher = TeacherModel.objects.create(user=user, **validated_data)
        return teacher

class HomeworkSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = HomeworkModel
        fields = ['id', 'title', 'teacher', 'group', 'created_at']