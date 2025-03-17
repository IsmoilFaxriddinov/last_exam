from django.db import models
from django.contrib.auth.models import User
from admins.models import AdminModel
from teachers.models import HomeworkModel

class StudentModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    managed_by = models.ForeignKey(AdminModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class SubmissionModel(models.Model):
    homework = models.ForeignKey(HomeworkModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    file = models.FileField(upload_to='submissions/', null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.homework.title}"