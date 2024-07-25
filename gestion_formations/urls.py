# gestion_formations/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Pour la déconnexion
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Pour réinitialiser le mot de passe
    path('', include('centres.urls')),  # Inclure les URLs de l'application `centres`
]
