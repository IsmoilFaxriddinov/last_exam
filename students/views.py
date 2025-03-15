from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action

from students.models import SubmissionModel, StudentModel
from students.serializers import StudentSerializer, SubmissionSrializer
from teachers.models import HomeworkModel

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response(serializer.data, status=201)
    
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = SubmissionModel.objects.all()
    serializer_class = SubmissionSrializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        try:
            student = self.request.user.studentmodel
        except StudentModel.DoesNotExist:
            student = StudentModel.objects.create(
                user=self.request.user,
                name=self.request.user.username
            )
        homework_id = self.request.data.get('homework')
        try:
            homework = HomeworkModel.objects.get(id=homework_id)
        except HomeworkModel.DoesNotExist:
            raise SubmissionSrializer.ValidationError("Bunday uy vazifasi mavjud emas.")
        serializer.save(student=student, homework=homework)