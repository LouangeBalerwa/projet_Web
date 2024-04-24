from django.db import models

class livre(models.Model):
    Titre = models.CharField(unique=True, max_length=200)
    date_pub = models.DateField(null=True, blank=True)
    contenus = models.TextField(blank=True)
    prix = models.IntegerField(default=0)
    commentaire = models.TextField(blank=True)
    nom_auteur = models.CharField(unique=True, max_length=100)
    
class auteur(models.Model):
    nom_auteur = models.CharField(max_length=255, help_text="")
    email = models.EmailField()
    num_tel = models.IntegerField(default=0)
    pays = models.CharField(max_length=200, blank=True, help_text="")
    
    def __str__(self):
        return self.nom_auteur
    def get_absolute_url(self):
        return "affichage"

    
class pensesPositives(models.Model):
    TitreP = models.CharField(unique=True, max_length=200)
    contenus = models.TextField(blank=True)
    nom_auteur = models.CharField(max_length=255, help_text="Entrez votre nom")
    
    def __str__(self):
        return self.Titre