# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views

# app_name = 'centres'

# urlpatterns = [
#     path('', views.home, name='home'),  # Page d'accueil
#     path('centres/', views.centre_list, name='centre_list'),  # Liste des centres de formation
#     path('centre/<int:pk>/', views.centre_detail, name='centre_detail'),  # Détail d'un centre
#     path('personne/ajouter/', views.personne_create, name='personne_create'),  # Formulaire pour ajouter une personne
#     path('formation/ajouter/', views.formation_create, name='formation_create'),  # Formulaire pour ajouter une formation
#     path('session/ajouter/', views.session_create, name='session_create'),  # Formulaire pour ajouter une session de formation
#     # path('commentaire/ajouter/', views.commentaire_create, name='commentaire_create'),  # Formulaire pour ajouter un commentaire
#     path('commentaires/ajouter/<int:session_id>/', views.commentaire_create, name='commentaire_create'),
#     path('formations/', views.formation_list, name='formation_list'),  # Liste des formations
#     path('sessions/', views.session_list, name='session_list'),  # Liste des sessions de formation
#     path('commentaires/', views.commentaire_list, name='commentaire_list'),  # Liste des commentaires
#     path('register/', views.register, name='register'),  # Page d'inscription
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Pour la déconnexion
#     # path('sessions/<int:session_id>/commentaire/ajouter/', views.commentaire_create, name='ajouter_commentaire'),
#     path('sessions/<int:session_id>/commentaire/ajouter/', views.commentaire_create, name='ajouter_commentaire'),
#     path('sessions/<int:pk>/', views.session_detail, name='session_detail'),
#     path('formation/<int:pk>/', views.formation_detail, name='formation_detail'),  # Assurez-vous que cette ligne existe
# ]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'centres'

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil

    # Routes pour les Centres de Formation
    path('centres/', views.centre_list, name='centre_list'),  # Liste des centres de formation
    path('centre/<int:pk>/', views.centre_detail, name='centre_detail'),  # Détail d'un centre

    # Routes pour les Personnes
    path('personne/ajouter/', views.personne_create, name='personne_create'),  # Formulaire pour ajouter une personne

    # Routes pour les Formations
    path('formations/', views.formation_list, name='formation_list'),  # Liste des formations
    path('formation/<int:pk>/', views.formation_detail, name='formation_detail'),  # Détail d'une formation
    path('formation/ajouter/', views.formation_create, name='formation_create'),  # Formulaire pour ajouter une formation

    # Routes pour les Sessions de Formation
    path('sessions/', views.session_list, name='session_list'),  # Liste des sessions de formation
    path('sessions/<int:pk>/', views.session_detail, name='session_detail'),  # Détail d'une session
    path('session/ajouter/', views.session_create, name='session_create'),  # Formulaire pour ajouter une session de formation
    path('sessions/<int:session_id>/commentaires/', views.commentaire_list, name='commentaire_list'),

    # Routes pour les Commentaires
    path('commentaires/', views.commentaire_list, name='commentaire_list'),  # Liste des commentaires
    path('sessions/<int:session_id>/commentaire/ajouter/', views.commentaire_create, name='ajouter_commentaire'),  # Formulaire pour ajouter un commentaire

    # Routes pour l'Authentification
    path('register/', views.register, name='register'),  # Page d'inscription
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Pour la déconnexion
]
