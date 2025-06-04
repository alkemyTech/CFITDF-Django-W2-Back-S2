from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Reservation
from .forms import ReservationForm


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'app_reservation/reservation_form.html'
    success_url = reverse_lazy('app_reservation:reservation_list')


class ReservationListView(ListView):
    model = Reservation
    template_name = 'app_reservation/reservation_list.html'
    context_object_name = 'reservations'
    ordering = ['-service_date']
    paginate_by = 10


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'app_reservation/reservation_detail.html'
    context_object_name = 'reservation'


class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'app_reservation/reservation_form.html'
    success_url = reverse_lazy('app_reservation:reservation_list')

    def get_object(self, queryset=None):
        return super().get_object(queryset=queryset)


class ReservationDeleteView(UpdateView):
    model = Reservation
    template_name = 'app_reservation/reservation_confirm_delete.html'
    success_url = reverse_lazy('app_reservation:reservation_list')

    def get_object(self, form):
        form.instance.active = False
        form.instance.save()
        return super().form_valid(form)
