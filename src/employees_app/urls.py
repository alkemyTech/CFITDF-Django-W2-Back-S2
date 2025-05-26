from django.urls import path
from . import views

app_name = 'employees_app'

urlpatterns = [
    path('listar/', views.employee_list, name='employee_list'),
    path('crear/', views.employee_create, name='employee_create'),
    path('editar/<int:pk>/', views.employee_update, name='employee_update'),
]
