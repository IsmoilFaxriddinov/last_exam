from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from teachers.models import HomeworkModel, TeacherModel
from teachers.serializers import HomeworkSerializer, TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        return Response(serializer.data, status=201)

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = HomeworkModel.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.teachermodel)