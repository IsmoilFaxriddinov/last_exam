from django.db import models
from django.contrib.auth.models import User
from admins.models import AdminModel

class TeacherModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    managed_by = models.ForeignKey(AdminModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class HomeworkModel(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    group = models.ForeignKey('admins.GroupModel', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
