from django.db import models
from django.contrib.auth.models import User
from admins.models import AdminModel

class StudentModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    managed_by = models.ForeignKey(AdminModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name