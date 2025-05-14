from django.db import models
from employees_app.models import Employee
# Create your models here.


class Coordinator(Employee):
    document_number = models.IntegerField(unique=True)
    discharge_date = models.DateTimeField(auto_now_add=True)
