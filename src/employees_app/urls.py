from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeactivateView,
    EmployeeDetailView,
    EmployeeListActiveView
)

app_name = 'employees_app'

urlpatterns = [
    
    path('', EmployeeListView.as_view(), name='employee_list'), 
    path('activos/', EmployeeListActiveView.as_view(), name='employee_list_activo'),
    path('create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/deactivate/', EmployeeDeactivateView.as_view(), name='employee_deactivate'),
    path('detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),

]

