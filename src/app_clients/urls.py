from django.urls import path
from .views import (ClientsCreateView, ClientsListView,
                    ClientsDetailView, ClientsUpdateView, delete_client)

app_name = 'app_clients'

urlpatterns = [
    path('', ClientsListView.as_view(), name='clients_list'),
    path('create/', ClientsCreateView.as_view(), name='clients_create'),
    path('detail/<int:pk>/', ClientsDetailView.as_view(), name='clients_detail'),
    path('update/<int:pk>/', ClientsUpdateView.as_view(), name='clients_update'),
    path('delete/<int:pk>/', delete_client, name='clients_delete'),
]
