from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import Service


class ServiceCreateView(CreateView):
    model = Service
    template_name = 'app_services/service_form.html'
    fields = ['name', 'description', 'price']
    # success_url = reverse_lazy('app_services:service_list') 


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'app_services/service_detail.html'
    context_object_name = 'service'