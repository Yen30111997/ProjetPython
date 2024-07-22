# main/views.py

from django.shortcuts import render, get_object_or_404
from .models import CentreFormation, Personne, Formation, SessionFormation, Commentaire

def centre_formation_list(request):
    centres = CentreFormation.objects.all()
    return render(request, 'centres.html', {'centres': centres})

def centre_formation_detail(request, pk):
    centre = get_object_or_404(CentreFormation, pk=pk)
    return render(request, 'centre_detail.html', {'centre': centre})
def personne_list(request):
    personnes = Personne.objects.all()
    return render(request, 'personnes.html', {'personnes': personnes})

def personne_detail(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    return render(request, 'personne_detail.html', {'personne': personne})
def formation_list(request):
    formations = Formation.objects.all()
    return render(request, 'formations.html', {'formations': formations})

def formation_detail(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    return render(request, 'formation_detail.html', {'formation': formation})
def session_list(request):
    sessions = SessionFormation.objects.all()
    return render(request, 'sessions.html', {'sessions': sessions})

def session_detail(request, pk):
    session = get_object_or_404(SessionFormation, pk=pk)
    return render(request, 'session_detail.html', {'session': session})
def commentaire_list(request):
    commentaires = Commentaire.objects.all()
    return render(request, 'commentaires.html', {'commentaires': commentaires})

def commentaire_detail(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    return render(request, 'commentaire_detail.html', {'commentaire': commentaire})

def home(request):
    return render(request, 'centres/home.html') 
