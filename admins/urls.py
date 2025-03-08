from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuperAdminViewSet, AdminViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'superadmins', SuperAdminViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]