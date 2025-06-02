from django.urls import path
from .views import home

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    # You can add more paths here if needed
]