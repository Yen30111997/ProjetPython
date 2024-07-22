# gestion_formations/urls.py

from django.contrib import admin
from django.urls import path, include
from centres import views  # Assurez-vous d'importer les vues de votre application principale

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ajoutez cette ligne pour la racine
    path('centres/', include('centres.urls')),  # Incluez les URLs de l'application 'main'
]
