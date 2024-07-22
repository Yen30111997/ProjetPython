# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('centres/', views.centre_formation_list, name='centre_list'),
    path('centres/<int:pk>/', views.centre_formation_detail, name='centre_detail'),
]
