from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, HomeworkViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'homeworks', HomeworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]