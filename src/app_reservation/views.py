from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Reservation

class CreateReservationView(CreateView):
    model = Reservation
    template_name = 'app_reservation/reservation_form.html'
    fields = '__all__'
    success_url = reverse_lazy('app_reservation:reservation_list')

class ListReservationView(ListView):
    model = Reservation
    template_name = 'app_reservation/reservation_list.html'
    context_object_name = 'reservations'
    ordering = ['-date']
    paginate_by = 10

class UpdateReservationView(UpdateView):
    model = Reservation
    template_name = 'app_reservation/reservation_form.html'
    fields = '__all__'
    success_url = reverse_lazy('app_reservation:reservation_list')
    def get_object(self, queryset=None):
        return super().get_object(queryset=queryset)
    
class DeleteReservationView(UpdateView):
    model = Reservation
    template_name = 'app_reservation/reservation_confirm_delete.html'
    success_url = reverse_lazy('app_reservation:reservation_list')
    
    def get_object(self, form):
        form.instance.active = False
        form.instance.save()
        return super().form_valid(form)
