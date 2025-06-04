from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Clients
from .forms import ClientsForm


class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientsForm
    template_name = 'app_clients/clients_form.html'
    success_url = reverse_lazy('app_clients:clients_list')


class ClientsDetailView(DetailView):
    model = Clients
    template_name = 'app_clients/clients_detail.html'
    context_object_name = 'client'


class ClientsListView(ListView):
    queryset = Clients.objects.all().filter(active=True)
    template_name = 'app_clients/clients_list.html'
    context_object_name = 'clients'
    ordering = ['first_name', 'last_name']


class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = ClientsForm
    template_name = 'app_clients/clients_form.html'
    success_url = reverse_lazy('app_clients:clients_list')


def delete_client(request, pk):
    client_to_delete = get_object_or_404(Clients, pk=pk)

    if request.method == 'POST':
        client_to_delete.active = not client_to_delete.active
        client_to_delete.save()
        return HttpResponseRedirect(reverse('app_clients:clients_list'))

    return render(request, 'app_clients/clients_confirm_delete.html', {'client': client_to_delete})
