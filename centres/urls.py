from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'centres'

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('centres/', views.centre_list, name='centre_list'),  # Liste des centres de formation
    path('centre/<int:pk>/', views.centre_detail, name='centre_detail'),  # Détail d'un centre
    path('personne/ajouter/', views.personne_create, name='personne_create'),  # Formulaire pour ajouter une personne
    path('formation/ajouter/', views.formation_create, name='formation_create'),  # Formulaire pour ajouter une formation
    path('session/ajouter/', views.session_create, name='session_create'),  # Formulaire pour ajouter une session de formation
    path('commentaire/ajouter/', views.commentaire_create, name='commentaire_create'),  # Formulaire pour ajouter un commentaire
    path('formations/', views.formation_list, name='formation_list'),  # Liste des formations
    path('sessions/', views.session_list, name='session_list'),  # Liste des sessions de formation
    path('commentaires/', views.commentaire_list, name='commentaire_list'),  # Liste des commentaires
]

main_urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('centres.urls')),  # Inclure les URLs de l'application 'centres'
    path('accounts/', include('django.contrib.auth.urls')),  # Inclure les URLs d'authentification
]

urlpatterns += main_urlpatterns
