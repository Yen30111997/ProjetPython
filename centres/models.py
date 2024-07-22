
from django.db import models


class CentreFormation(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255, default='Adresse par défaut')  # Valeur par défaut ajoutée
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=20, default='00000')  # Valeur par défaut ajoutée ici
    pays = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom



class Personne(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255, blank=True, null=True)
    centre_formation = models.ForeignKey(CentreFormation, on_delete=models.SET_NULL, null=True, blank=True, related_name='personnes')

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Formation(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    centre_formation = models.ForeignKey(CentreFormation, on_delete=models.CASCADE, related_name='formations')
    date_debut = models.DateField()
    date_fin = models.DateField()
    niveau = models.CharField(max_length=100)  # Par exemple: Débutant, Intermédiaire, Avancé

    def __str__(self):
        return self.titre

    def duree(self):
        return (self.date_fin - self.date_debut).days

class SessionFormation(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name='sessions')
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    formateur = models.ForeignKey(Personne, on_delete=models.SET_NULL, null=True, blank=True, related_name='sessions')

    def __str__(self):
        return f"{self.formation.titre} - {self.date_debut.strftime('%d/%m/%Y')}"


class Commentaire(models.Model):
    session_formation = models.ForeignKey(SessionFormation, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='commentaires')
    texte = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.session_formation}"

