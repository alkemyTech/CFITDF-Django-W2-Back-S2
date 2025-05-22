"""
URL configuration for project001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('app_services.urls', namespace='app_services')),
    path('clients/', include('app_clients.urls', namespace='app_clients')),
    path('employees/', include('employees_app.urls', namespace='employees_app')),
    path('coordinators/', include('app_coordinators.urls', namespace='app_coordinators')),
    path('reservation/', include('app_reservation.urls', namespace='app_reservation')),
]
