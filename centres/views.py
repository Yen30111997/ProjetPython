from django.shortcuts import render, get_object_or_404, redirect
from .models import CentreFormation, Personne, Formation, SessionFormation, Commentaire
from .forms import CentreFormationForm, PersonneForm, FormationForm, SessionFormationForm, CommentaireForm


def home(request):
    return render(request, 'centres/home.html')

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
