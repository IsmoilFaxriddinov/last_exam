from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SuperAdminModel, AdminModel, GroupModel
from .serializers import SuperAdminSerializer, AdminSerializer, GroupSerializer
from rest_framework import status

class SuperAdminViewSet(viewsets.ModelViewSet):
    queryset = SuperAdminModel.objects.all()
    serializer_class = SuperAdminSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class AdminViewSet(viewsets.ModelViewSet):
    queryset = AdminModel.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()
        
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print("Authenticated User:", self.request.user)
        print("Is Authenticated:", self.request.user.is_authenticated)
        
        admin = AdminModel.objects.filter(user=self.request.user).first()
        if not admin:
            return Response({"error": "User is not associated with an AdminModel"},status=status.HTTP_403_FORBIDDEN)
        group = serializer.save(admin=admin)
        return Response(
            {"success": True, "message": "Group created successfully!", "group_id": group.id, "group_name": group.name,},status=status.HTTP_201_CREATED
        )

