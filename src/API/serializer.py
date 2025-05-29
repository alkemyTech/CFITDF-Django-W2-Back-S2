from app_clients.models import Clients
from app_coordinators.models import Coordinator
from app_reservation.models import Reservation
from app_services.models import Service
from employees_app.models import Employee
from rest_framework.serializers import ModelSerializer


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class CoordinatorSerializer(ModelSerializer):
    class Meta:
        model = Coordinator
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    client = ClientSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)
    coordinator = CoordinatorSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'