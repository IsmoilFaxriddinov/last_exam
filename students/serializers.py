from rest_framework import serializers
from django.contrib.auth.models import User

from teachers.models import HomeworkModel
from students.models import StudentModel, SubmissionModel
from admins.serializers import AdminSerializer, UserSerializer
from students.models import SubmissionModel

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

class SubmissionSrializer(serializers.ModelSerializer):
    homework = serializers.PrimaryKeyRelatedField(queryset=HomeworkModel.objects.all())
    file = serializers.FileField(required=False)

    class Meta:
        model = SubmissionModel
        fields = ['homework', 'content', 'file', 'student', 'submitted_at']
        read_only_fields = ['student', 'submitted_at']