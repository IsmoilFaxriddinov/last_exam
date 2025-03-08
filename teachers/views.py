from rest_framework import viewsets, permissions

from teachers.models import HomeworkModel, TeacherModel
from teachers.serializers import HomeworkSerializer, TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(managed_by=self.request.user.adminmodel)

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = HomeworkModel.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.teachermodel)