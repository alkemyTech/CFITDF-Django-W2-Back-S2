from django.urls import path
from .views import (ReservationCreateView, ReservationListView,
                    ReservationUpdateView, ReservationDeleteView, ReservationDetailView)
app_name = 'app_reservation'
urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation_list'),
    path('create/', ReservationCreateView.as_view(), name='reservation_create'),
    path('detail/<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    path('update/<int:pk>/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('delete/<int:pk>/', ReservationDeleteView.as_view(), name='reservation_delete'),
]