# employees_app/urls.py

from django.urls import path
from . import views


app_name = 'employees'

urlpatterns = [
    # Vista de lista de empleados
    path('employees/', views.employee_list, name='employee_list'),
    
    # Puedes agregar más URLs según necesites
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:employee_id>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),
    
    # URL para la página principal (opcional)
    path('', views.index, name='index'),
]