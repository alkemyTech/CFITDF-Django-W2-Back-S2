from django.urls import path
from .views import (
    EmployeeListAPIView,
)

app_name = 'API'

urlpatterns = [
    path('employee/', EmployeeListAPIView.as_view(), name='list_employee_api'),
]
