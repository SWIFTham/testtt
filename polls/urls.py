from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('connection.html', views.connection),
    path('register.html', views.register),   
]

