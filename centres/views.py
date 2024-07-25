from django.shortcuts import render, get_object_or_404, redirect
from .models import CentreFormation, Personne, Formation, SessionFormation, Commentaire
from .forms import CentreFormationForm, PersonneForm, FormationForm, SessionFormationForm, CommentaireForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    commentaires = Commentaire.objects.all()  # Récupère tous les commentaires
    return render(request, 'centres/home.html', {'commentaires': commentaires})


def centre_list(request):
    centres = CentreFormation.objects.all()
    return render(request, 'centres/centre_list.html', {'centres': centres})

def centre_detail(request, pk):
    centre = get_object_or_404(CentreFormation, pk=pk)
    return render(request, 'centres/centre_detail.html', {'centre': centre})

def personne_create(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centres:centre_list')
    else:
        form = PersonneForm()
    return render(request, 'centres/personne_form.html', {'form': form})

def formation_create(request):
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centres:formation_list')
    else:
        form = FormationForm()
    return render(request, 'centres/formation_form.html', {'form': form})

def session_create(request):
    if request.method == 'POST':
        form = SessionFormationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centres:session_list')
    else:
        form = SessionFormationForm()
    return render(request, 'centres/session_form.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('centres:home')
    else:
        form = UserCreationForm()
    return render(request, 'centres/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('centres:home')
    else:
        form = AuthenticationForm()
    return render(request, 'centres/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('centres:home')
@login_required
def commentaire_create(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centres:commentaire_list')
    else:
        form = CommentaireForm()
    return render(request, 'centres/commentaire_form.html', {'form': form})

def formation_list(request):
    formations = Formation.objects.all()
    return render(request, 'centres/formation_list.html', {'formations': formations})

def session_list(request):
    sessions = SessionFormation.objects.all()
    return render(request, 'centres/session_list.html', {'sessions': sessions})

def commentaire_list(request):
    commentaires = Commentaire.objects.all()
    return render(request, 'centres/commentaire_list.html', {'commentaires': commentaires})
