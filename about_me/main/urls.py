from django.urls import path, include

from .views import index, employee

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('employee/<int:employee_id>/', employee, name='employee'),
]
