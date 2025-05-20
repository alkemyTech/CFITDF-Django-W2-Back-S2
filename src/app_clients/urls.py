from django.urls import path
from .views import (ClientsCreateView, )

app_name = 'app_clients'

urlpatterns = [
    path('create/', ClientsCreateView.as_view(), name='clients_create'),
]
