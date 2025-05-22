from django.urls import path
from .views import (ServiceCreateView, ServiceDetailView, 
                    ServiceListView, ServiceUpdateView, ServiceDesactivateView)

app_name = 'app_services'

urlpatterns = [
    path('', ServiceListView.as_view(), name='services_list'),
    path('create/', ServiceCreateView.as_view(), name='service_create'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('update/<int:pk>/', ServiceUpdateView.as_view(), name='service_update'),
    path('<int:pk>/deactivate/', ServiceDesactivateView.as_view(), name='service_desactivate'),
]