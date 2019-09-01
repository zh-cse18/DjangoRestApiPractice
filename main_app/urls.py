
from django.urls import path

from main_app import views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]