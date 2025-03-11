from django.urls import path, include
from dotenv import load_dotenv
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from admins.views import SuperAdminViewSet, AdminViewSet, GroupViewSet
from students.views import StudentViewSet
from teachers.views import TeacherViewSet, HomeworkViewSet

router = DefaultRouter()
router.register(r'superadmins', SuperAdminViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'homeworks', HomeworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]