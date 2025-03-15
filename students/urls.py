from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import StudentViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'submission', SubmissionViewSet, basename='submission')
urlpatterns = [
    path('', include(router.urls)),
    ]