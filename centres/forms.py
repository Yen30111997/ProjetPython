from django import forms
from .models import Commentaire, Formation, SessionFormation, Personne
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
