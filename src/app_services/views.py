from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Service
from .forms import ServicesForm


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServicesForm
    template_name = 'app_services/service_form.html'
    success_url = reverse_lazy('app_services:services_list')


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'app_services/service_detail.html'
    context_object_name = 'service'


class ServiceListView(ListView):
    model = Service
    template_name = 'app_services/services_list.html'
    context_object_name = 'services'
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        return Service.objects.filter(active=True).order_by('-created_at')


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServicesForm
    template_name = 'app_services/service_form.html'
    success_url = reverse_lazy('app_services:services_list')
    context_object_name = 'service'


class ServiceDesactivateView(UpdateView):
    model = Service
    fields = []
    template_name = 'app_services/service_desactivate.html'
    success_url = reverse_lazy('app_services:services_list')

    def form_valid(self, form):
        form.instance.active = False
        form.instance.save()
        return super().form_valid(form)
