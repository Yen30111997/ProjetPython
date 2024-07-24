from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import CentreFormation, Personne, Formation, SessionFormation, Commentaire

# Vues pour les centres de formation
def centre_formation_list(request):
    centres = CentreFormation.objects.all()
    return render(request, 'centres/centres.html', {'centres': centres})

def centre_formation_detail(request, pk):
    centre = get_object_or_404(CentreFormation, pk=pk)
    return render(request, 'centres/centre_detail.html', {'centre': centre})

# Vues pour l'inscription et la connexion
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'centres/register.html', {'form': form})

def home(request):
    return render(request, 'centres/home.html')

# Autres vues
def personne_list(request):
    personnes = Personne.objects.all()
    return render(request, 'centres/personnes.html', {'personnes': personnes})

def personne_detail(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    return render(request, 'centres/personne_detail.html', {'personne': personne})

def formation_list(request):
    formations = Formation.objects.all()
    return render(request, 'centres/formations.html', {'formations': formations})

def formation_detail(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    return render(request, 'centres/formation_detail.html', {'formation': formation})

def session_list(request):
    sessions = SessionFormation.objects.all()
    return render(request, 'centres/sessions.html', {'sessions': sessions})

def session_detail(request, pk):
    session = get_object_or_404(SessionFormation, pk=pk)
    return render(request, 'centres/session_detail.html', {'session': session})

def commentaire_list(request):
    commentaires = Commentaire.objects.all()
    return render(request, 'centres/commentaires.html', {'commentaires': commentaires})

def commentaire_detail(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    return render(request, 'centres/commentaire_detail.html', {'commentaire': commentaire})
