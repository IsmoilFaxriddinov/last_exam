from django.contrib import admin

from teachers.models import HomeworkModel, TeacherModel

admin.site.register(TeacherModel)
admin.site.register(HomeworkModel)
