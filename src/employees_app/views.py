# employees_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Employee
# from .forms import EmployeeForm  # type: ignore # Tendrás que crear este formulario


def index(request):
    """Vista para la página principal"""
    return render(request, 'employees_app/index.html')


def employee_list(request):
    """Vista para listar todos los empleados"""
    employees = Employee.objects.all()
    return render(request, 'employees_app/employee_list.html', {'employees': employees})


def employee_detail(request, employee_id):
    """Vista para ver detalles de un empleado específico"""
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employees_app/employee_detail.html', {'employee': employee})


def employee_create(request):
    """Vista para crear un nuevo empleado"""
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees_app/employee_form.html', {'form': form})


def employee_update(request, employee_id):
    """Vista para actualizar un empleado existente"""
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:employee_detail', employee_id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees_app/employee_form.html', {'form': form})


def employee_delete(request, employee_id):
    """Vista para eliminar un empleado"""
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees:employee_list')
    return render(request, 'employees_app/employee_confirm_delete.html', {'employee': employee})
