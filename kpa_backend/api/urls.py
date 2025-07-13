from django.urls import path
from . import views

urlpatterns = [
    path('kpa-form/', views.create_kpa_form),
    path('kpa-form/<int:pk>/', views.get_kpa_form),
]
