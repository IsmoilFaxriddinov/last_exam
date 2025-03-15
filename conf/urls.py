"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication

from admins.views import AdminViewSet, GroupViewSet, SuperAdminViewSet
from conf import settings
from students.views import SubmissionViewSet, StudentViewSet
from teachers.views import HomeworkViewSet, TeacherViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title="N55 medium clone API",
        default_version="v1",
        description="Class project in Ismoil",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ismoilfaxriddinov2010@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[(JWTAuthentication,)],
)

from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static

urlpatterns = [
    path('admins/', include('admins.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'superadmins', SuperAdminViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'homeworks', HomeworkViewSet)

urlpatterns += [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)