from django.db import models
from django.contrib.auth.models import User  # Importer le modèle User

class MotsCles(models.Model):
    mot = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.mot

class CentreFormation(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255, default='Adresse par défaut')
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=20, default='00000')
    pays = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mots_cles = models.ManyToManyField(MotsCles, related_name='centres_formation', blank=True)

    def __str__(self):
        return self.nom

class Personne(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Lier avec le modèle User
    telephone = models.CharField(max_length=20, blank=True, null=True)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255, blank=True, null=True)
    attentes = models.ManyToManyField(MotsCles, related_name='personnes', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Formation(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    centre_formation = models.ForeignKey(CentreFormation, on_delete=models.CASCADE, related_name='formations')
    date_debut = models.DateField()
    date_fin = models.DateField()
    niveau = models.CharField(max_length=100)

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

class Actualite(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Temoinage(models.Model):
    auteur = models.CharField(max_length=255)
    texte = models.TextField()
    date_temoinage = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Témoignage de {self.auteur}"

class Partenaire(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    description = models.TextField()
    site_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nom
