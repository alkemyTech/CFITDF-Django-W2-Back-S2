from django.urls import path
from .views import (ServiceCreateView, ServiceDetailView)

app_name = 'app_services'

urlpatterns = [
    path('create/', ServiceCreateView.as_view(), name='service_create'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
]