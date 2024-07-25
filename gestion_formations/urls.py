from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from centres import views  # Importez les vues de l'application `centres`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('', include('centres.urls')),  # Inclure les URLs de l'application `centres`
    path('register/', views.register_view, name='register'),  # Correction ici
]
