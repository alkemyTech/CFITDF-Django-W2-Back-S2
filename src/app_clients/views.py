from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Clients


class ClientsCreateView(CreateView):
    model = Clients
    template_name = 'app_clients/clients_form.html'
    fields = '__all__'
    # success_url = reverse_lazy('app_clients:clients_list')
