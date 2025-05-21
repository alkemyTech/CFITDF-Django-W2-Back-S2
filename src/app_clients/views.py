from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Clients


class ClientsCreateView(CreateView):
    model = Clients
    template_name = 'app_clients/clients_form.html'
    fields = '__all__'
    success_url = reverse_lazy('app_clients:clients_list')


class ClientsDetailView(DetailView):
    model = Clients
    template_name = 'app_clients/clients_detail.html'
    context_object_name = 'client'


class ClientsListView(ListView):
    model = Clients
    template_name = 'app_clients/clients_list.html'
    context_object_name = 'clients'
    ordering = ['first_name', 'last_name']


class ClientsUpdateView(UpdateView):
    model = Clients
    template_name = 'app_clients/clients_form.html'
    fields = '__all__'
    success_url = reverse_lazy('app_clients:clients_list')
