from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from students.models import StudentModel
from students.serializers import StudentSerializer

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