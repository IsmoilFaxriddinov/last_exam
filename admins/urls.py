from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from admins.views import SuperAdminViewSet, AdminViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'superadmins', SuperAdminViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]