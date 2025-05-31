from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees_app/employee_list.html'
    context_object_name = 'employees'

def get_queryset(self):
        return Employee.objects.filter(activo=True)

class EmployeeListActiveView(ListView):
    model = Employee
    template_name = "employee_app/employees_list_activo.html"
    context_object_name = "employees"

    def get_queryset(self):
        return Employee.objects.filter(is_active=True)


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees_app/employee_form.html'
    success_url = reverse_lazy('employees_app:employee_list')


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees_app/employee_form.html'
    success_url = reverse_lazy('employees_app:employee_list_activo')

class EmployeeDeactivateView(UpdateView):
    model = Employee
    fields = [] 
    template_name = 'employees_app/employee_desactivate.html'
    success_url = reverse_lazy('employees_app:employee_list_activo')

    def form_valid(self, form):
        form.instance.active = False
        return super().form_valid(form)

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees_app/employee_detail.html'
    context_object_name = 'employee'
