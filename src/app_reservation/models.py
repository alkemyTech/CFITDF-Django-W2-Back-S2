from django.db import models


class Reservation(models.Model):
    reservation_date = models.DateField(auto_now_add=True, verbose_name="Reservation Date")
    service_date = models.DateTimeField(verbose_name="Service Date")
    client = models.ForeignKey('app_clients.Clients', on_delete=models.CASCADE, verbose_name="Client")
    service = models.ForeignKey('app_services.Service', on_delete=models.CASCADE, verbose_name="Service")
    employee = models.ForeignKey('employees_app.Employee', on_delete=models.CASCADE, verbose_name="Employee", related_name='reservations_as_employee')
    coordinator = models.ForeignKey('app_coordinators.Coordinator', on_delete=models.CASCADE, verbose_name="Coordinator", related_name='reservations_as_coordinator')

    def __str__(self):
        return f"Reservation for {self.client} on {self.service_date} - Service: {self.service.name}"
    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        ordering = ['service_date']
