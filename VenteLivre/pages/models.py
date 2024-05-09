from django.db import models


class auteur(models.Model):
    nom_auteur = models.CharField(max_length=100, unique = True)
    email = models.EmailField()
    num_tel = models.IntegerField(default=0)
    pays = models.CharField(max_length=64, blank=True)
    ville = models.CharField(max_length=64, blank=True)
    matricule = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nom_auteur
    def get_absolute_url(self):
        return "affichage"


class livre(models.Model):
    Titre = models.CharField(unique=True, max_length=200)
    photo = models.ImageField(upload_to='images', blank=True)
    contenus = models.TextField(blank=True)
    prix = models.IntegerField(default=0)
    date_pub = models.DateField(null=True, blank=True)
    auteur = models.ForeignKey(auteur, on_delete= models.CASCADE, default=1)
    
class pensesPositives(models.Model):
    TitreP = models.CharField(unique=True, max_length=200)
    contenus = models.TextField(blank=True)
    nom_auteur = models.CharField(max_length=100, help_text="Entrez votre nom")
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.Titre
    
class messageImage(models.Model):
    nom_auteur = models.CharField(max_length=100, help_text="Entrez votre nom")
    image = models.ImageField(upload_to='images', blank=True)
    
class creationCompte(models.Model):
    
    matricule = models.IntegerField(default=0)
    type_compte = models.CharField(unique=True, max_length=64)
    balance = models.IntegerField(default=0)