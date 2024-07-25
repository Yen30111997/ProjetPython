from django import forms
from .models import CentreFormation, Personne, Formation, SessionFormation, Commentaire

class CentreFormationForm(forms.ModelForm):
    class Meta:
        model = CentreFormation
        fields = ['nom', 'adresse', 'ville', 'code_postal', 'pays', 'telephone', 'email', 'site_web', 'description', 'mots_cles']

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'email', 'telephone', 'date_naissance', 'adresse', 'attentes']

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['titre', 'description', 'centre_formation', 'date_debut', 'date_fin', 'niveau']

class SessionFormationForm(forms.ModelForm):
    class Meta:
        model = SessionFormation
        fields = ['formation', 'date_debut', 'date_fin', 'lieu', 'formateur']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['session_formation', 'auteur', 'texte']
