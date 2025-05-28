from django.urls import path
from .views import (
    EmployeeListAPIView,
    ServiceListAPIView,
    ServiceDetailAPIView,
)

app_name = 'API'

urlpatterns = [
    path('employee/', EmployeeListAPIView.as_view(), name='list_employee_api'),
    path('service/', ServiceListAPIView.as_view(), name='list_service_api'),
    path('service/<int:pk>/', ServiceDetailAPIView.as_view(), name='detail_service_api'),
]