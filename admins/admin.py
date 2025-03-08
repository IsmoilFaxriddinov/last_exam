from django.contrib import admin

from admins.models import AdminModel, GroupModel, SuperAdminModel

admin.site.register(SuperAdminModel)
admin.site.register(AdminModel)
admin.site.register(GroupModel)