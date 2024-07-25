from django import forms
from .models import Commentaire, Formation, SessionFormation, Personne

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['texte']

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['titre', 'description', 'centre_formation', 'date_debut', 'date_fin', 'niveau']

class SessionFormationForm(forms.ModelForm):
    class Meta:
        model = SessionFormation
        fields = ['formation', 'date_debut', 'date_fin', 'lieu', 'formateur']

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['telephone', 'date_naissance', 'adresse', 'attentes']
