from django.db import models
from app_clients.models import Clients
from app_services.models import Service
from employees_app.models import Employee
from app_coordinators.models import Coordinator


class Reservation(models.Model):
    reservation_date = models.DateField(auto_now_add=True, verbose_name="Reservation Date")
    service_date = models.DateTimeField(verbose_name="Service Date")
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name="Client")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Service")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Employee", related_name='reservations_as_employee')
    coordinator = models.ForeignKey(Coordinator, on_delete=models.CASCADE, verbose_name="Coordinator", related_name='reservations_as_coordinator')
    active = models.BooleanField(default=True, verbose_name="Active")
    def __str__(self):
        return f"Reservation for {self.client} on {self.service_date} - Service: {self.service.name}"
    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        ordering = ['service_date']
