from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    file_number = models.IntegerField(unique=True, verbose_name="File Number")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    email = models.EmailField(max_length=254, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    

    def __str__(self):
        return f"{self.last_name}, {self.first_name} - File Number: {self.file_number}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['last_name', 'first_name']
