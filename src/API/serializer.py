from app_clients.models import Clients
from app_coordinators.models import Coordinator
from app_reservation.models import Reservation
from app_services.models import Service
from employees_app.models import Employee
from rest_framework.serializers import ModelSerializer


class ClientsListSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'first_name', 'last_name']


class ClientsDetailSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'active']


class CoordinatorsListSerializer(ModelSerializer):
    class Meta:
        model = Coordinator
        fields = ['id', 'first_name', 'last_name']


class CoordinatorsDetailSerializer(ModelSerializer):
    class Meta:
        model = Coordinator
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'is_active']


class EmployeesListSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['pk', 'first_name', 'last_name']


class EmployeesDetailSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['pk', 'first_name', 'last_name', 'is_active', 'email', 'phone']


class ServicesListSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['pk', 'name']


class ServicesDetailSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['pk', 'name', 'description', 'price', 'active']


class ReservationListSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'client', 'service', 'employee', 'coordinator', 'reservation_date', 'service_date']


class ReservationDetailSerializer(ModelSerializer):
    client = ClientsListSerializer(read_only=True)
    service = ServicesListSerializer(read_only=True)
    employee = EmployeesListSerializer(read_only=True)
    coordinator = CoordinatorsListSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'