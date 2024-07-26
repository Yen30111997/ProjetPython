from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CommentaireForm, FormationForm, SessionFormationForm, PersonneForm
from .models import Commentaire, Formation, SessionFormation, Personne
from .forms import CustomUserCreationForm
from django.db.models import Q
from .models import CentreFormation


def home(request):
    return render(request, 'centres/home.html')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('centres:home')
    else:
        form = AuthenticationForm()
    return render(request, 'centres/login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('centres:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('centres:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'centres/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('centres:home')

def commentaire_create(request, session_id):
    session = SessionFormation.objects.get(pk=session_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.session_formation = session
            commentaire.auteur = request.user.personne
            commentaire.save()
            return redirect('centres:session_detail', session_id=session.id)
    else:
        form = CommentaireForm()
    return render(request, 'centres/commentaire_form.html', {'form': form})
def commentaire_list(request):
    commentaires = Commentaire.objects.all()
    return render(request, 'centres/commentaire_list.html', {'commentaires': commentaires})
def centre_list(request):
    centres = CentreFormation.objects.all()
    return render(request, 'centres/centre_list.html', {'centres': centres})
def centre_detail(request, pk):
    centre = get_object_or_404(CentreFormation, pk=pk)
    return render(request, 'centres/centre_detail.html', {'centre': centre})
def formation_list(request):
    query = request.GET.get('q')
    if query:
        formations = Formation.objects.filter(titre__icontains=query)
    else:
        formations = Formation.objects.all()
    return render(request, 'centres/formation_list.html', {'formations': formations})
    
    return render(request, 'centres/formation_list.html', {'formations': formations})
def formation_create(request):
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centres:formation_list')
    else:
        form = FormationForm()
    return render(request, 'centres/formation_form.html', {'form': form})
def session_list(request):
    sessions = SessionFormation.objects.all()
    return render(request, 'centres/session_list.html', {'sessions': sessions})

def session_create(request):
    if request.method == 'POST':
        form = SessionFormationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centres:session_list')
    else:
        form = SessionFormationForm()
    return render(request, 'centres/session_form.html', {'form': form})
def personne_create(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centres:home')  # Redirige vers la page d'accueil ou une autre page appropriée
    else:
        form = PersonneForm()
    return render(request, 'centres/personne_form.html', {'form': form})
