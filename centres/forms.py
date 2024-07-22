from django import forms
from .models import Personne

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'email', 'telephone', 'date_naissance', 'adresse', 'centre_formation']  # Ajoutez les champs que vous avez dans le modèle Personne
