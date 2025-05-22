from django.urls import path
from .views import (CoordinatorListView, CoordinatorDetailView,
                    CoordinatorCreateView, CoordinatorUpdateView, CoordinatorDeactivateView)

app_name = 'app_coordinators'

urlpatterns = [
    path('', CoordinatorListView.as_view(), name='coordinators_list'),
    path('create/', CoordinatorCreateView.as_view(), name='coordinator_create'),
    path('<int:pk>/', CoordinatorDetailView.as_view(), name='coordinator_detail'),
    path('<int:pk>/update/', CoordinatorUpdateView.as_view(),
         name='coordinator_update'),
    path('<int:pk>/deactivate/', CoordinatorDeactivateView.as_view(),
         name='coordinator_deactivate'),
]
