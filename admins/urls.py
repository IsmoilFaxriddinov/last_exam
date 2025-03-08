from django.urls import path

from admins.views import test_view

app_name = 'admins'

urlpatterns = [
    path('admin/', test_view, name='admin'),
]
