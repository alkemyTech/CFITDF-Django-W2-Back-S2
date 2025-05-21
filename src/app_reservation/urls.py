from django.urls import path
from .views import (ReservationCreateView, ReservationListView,
                    ReservationUpdateView, ReservationDeleteView)
app_name = 'app_reservation'
urlpatterns = [
    path('create/', ReservationCreateView.as_view(), name='reservation_create'),
    path('list/', ReservationListView.as_view(), name='reservation_list'),
    path('update/<int:pk>/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('delete/<int:pk>/', ReservationDeleteView.as_view(), name='reservation_delete'),
]