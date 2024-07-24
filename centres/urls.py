from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('centres/', views.centre_formation_list, name='centre_list'),
    path('centres/<int:pk>/', views.centre_formation_detail, name='centre_detail'),
    path('personnes/', views.personne_list, name='personne_list'),
    path('personnes/<int:pk>/', views.personne_detail, name='personne_detail'),
    path('formations/', views.formation_list, name='formation_list'),
    path('formations/<int:pk>/', views.formation_detail, name='formation_detail'),
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/<int:pk>/', views.session_detail, name='session_detail'),
    path('commentaires/', views.commentaire_list, name='commentaire_list'),
    path('commentaires/<int:pk>/', views.commentaire_detail, name='commentaire_detail'),
    path('register/', views.register, name='register'),  # Pour l'inscription
]
