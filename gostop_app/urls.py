from django.urls import path
from . import views

urlpatterns = [
    path('', views.setup_view, name='setup'),
    path('calculate/', views.calculate_view, name='calculate'),
]