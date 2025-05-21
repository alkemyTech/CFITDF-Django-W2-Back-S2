from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Service


class ServiceCreateView(CreateView):
    model = Service
    template_name = 'app_services/service_form.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('app_services:services_list') 


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'app_services/service_detail.html'
    context_object_name = 'service'


class ServiceListView(ListView):
    model = Service
    template_name = 'app_services/services_list.html'
    context_object_name = 'services'
    paginate_by = 10 # Number of services per page
    ordering = ['name']


class ServiceUpdateView(UpdateView):
    model = Service
    template_name = 'app_services/service_form.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('app_services:services_list') 
    context_object_name = 'service'