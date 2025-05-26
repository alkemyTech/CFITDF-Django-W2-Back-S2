from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm

# Crear
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_app:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees_app/employee_form.html', {'form': form})

# Listar
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees_app/employee_list.html', {'employees': employees})

# Editar
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees_app:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees_app/employee_form.html', {'form': form})
