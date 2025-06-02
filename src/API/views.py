from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import viewsets
from .serializer import (
    ClientsListSerializer, ClientsDetailSerializer, 
    CoordinatorsListSerializer, CoordinatorsDetailSerializer,
    EmployeesListSerializer, EmployeesDetailSerializer,
    ServicesListSerializer, ServicesDetailSerializer,
    ReservationListSerializer, ReservationDetailSerializer
    )
from app_clients.models import Clients
from app_coordinators.models import Coordinator
from app_reservation.models import Reservation
from app_services.models import Service
from employees_app.models import Employee


class ClientsListAPIView(ListAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsListSerializer


class ClientsDetailAPIView(RetrieveAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsDetailSerializer


class ClientsCreateAPIView(CreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsDetailSerializer


class CoordinatorsListAPIView(ListAPIView):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorsListSerializer


class CoordinatorsDetailAPIView(RetrieveAPIView):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorsDetailSerializer


class EmployeesListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesListSerializer


class EmployeesDetailAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesDetailSerializer
    lookup_field = 'pk'


class ServicesListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesListSerializer


class ServicesDetailAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesDetailSerializer
    lookup_field = 'pk'


class ReservationsListAPIView(ListAPIView):
    queryset = Reservation.objects.all().filter(active=True)
    serializer_class = ReservationListSerializer


class ReservationsDetailAPIView(RetrieveAPIView):
    queryset = Reservation.objects.all().filter(active=True)
    serializer_class = ReservationDetailSerializer
    lookup_field = 'pk'


class ReservationsCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer