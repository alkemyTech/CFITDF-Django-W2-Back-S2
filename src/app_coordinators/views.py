from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Coordinator
from .forms import CoordinatorsForm


class CoordinatorListView(ListView):
    model = Coordinator
    template_name = 'app_coordinators/coordinators_list.html'
    context_object_name = 'coordinators'
    paginate_by = 10
    ordering = ['last_name', 'first_name']


class CoordinatorDetailView(DetailView):
    model = Coordinator
    template_name = 'app_coordinators/coordinator_detail.html'
    context_object_name = 'coordinator'


class CoordinatorCreateView(CreateView):
    model = Coordinator
    form_class = CoordinatorsForm
    template_name = 'app_coordinators/coordinators_form.html'
    success_url = reverse_lazy('app_coordinators:coordinators_list')


class CoordinatorUpdateView(UpdateView):
    model = Coordinator
    form_class = CoordinatorsForm
    template_name = 'app_coordinators/coordinators_form.html'
    success_url = reverse_lazy('app_coordinators:coordinators_list')


class CoordinatorDeactivateView(UpdateView):
    model = Coordinator
    fields = []
    template_name = 'app_coordinators/coordinator_deactivate.html'
    success_url = reverse_lazy('app_coordinators:coordinators_list')

    def form_valid(self, form):
        form.instance.is_active = False
        form.instance.save()
        return super().form_valid(form)
