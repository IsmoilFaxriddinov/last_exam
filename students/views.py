from rest_framework import viewsets, permissions

from students.models import StudentModel
from students.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(managed_by=self.request.user.adminmodel)