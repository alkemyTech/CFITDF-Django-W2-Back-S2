from django.urls import path
from .views import (
    ClientsListAPIView,
    ClientsDetailAPIView,
    ClientsCreateAPIView,
    EmployeesListAPIView,
    EmployeesDetailAPIView,
    CoordinatorsListAPIView,
    CoordinatorsDetailAPIView,
    ServicesListAPIView,
    ServicesDetailAPIView,
    ReservationsListAPIView,
    ReservationsDetailAPIView,
    ReservationsCreateAPIView,
)


app_name = 'API'


urlpatterns = [
    path('clients/', ClientsListAPIView.as_view(), name='list_client_api'),
    path('clients/<int:pk>/', ClientsDetailAPIView.as_view(), name='detail_client_api'),
    path('clients/create/', ClientsCreateAPIView.as_view(), name='create_client_api'),
    path('coordinators/', CoordinatorsListAPIView.as_view(), name='list_coordinator_api'),
    path('coordinators/<int:pk>/', CoordinatorsDetailAPIView.as_view(), name='detail_coordinator_api'),
    path('employees/', EmployeesListAPIView.as_view(), name='list_employee_api'),
    path('employees/<int:pk>/', EmployeesDetailAPIView.as_view(), name='detail_employee_api'),
    path('services/', ServicesListAPIView.as_view(), name='list_service_api'),
    path('services/<int:pk>/', ServicesDetailAPIView.as_view(), name='detail_service_api'),
    path('reservations/', ReservationsListAPIView.as_view(), name='list_reservation_api'),
    path('reservations/<int:pk>/', ReservationsDetailAPIView.as_view(), name='detail_reservation_api'),
    path('reservations/create/', ReservationsCreateAPIView.as_view(), name='create_reservation_api'),
]