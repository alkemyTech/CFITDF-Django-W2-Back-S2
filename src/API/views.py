from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClientSerializer, CoordinatorSerializer, ReservationSerializer, ServiceSerializer, EmployeeSerializer 
from app_clients.models import Clients
from app_coordinators.models import Coordinator
from app_reservation.models import Reservation
from app_services.models import Service
from employees_app.models import Employee
