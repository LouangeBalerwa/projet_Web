from django.db import models
from django.utils import timezone


# ================== classe Auteur===================================
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
        return "affichage_auteur"
    
# ================== classe Compte===================================
class creationCompte(models.Model):
    matricule = models.IntegerField(unique=True, default=0)
    type_compte = models.CharField(max_length=32)
    balance = models.IntegerField(default=0)
    
    def __str__(self):
        return self.type_compte
    def get_absolute_url(self):
        return "affichage_compte"

# ================== classe Livre===================================
class livre(models.Model):
    Titre = models.CharField(unique=True, max_length=200)
    photo = models.ImageField(upload_to='images', blank=True )
    fichier_pdf = models.FileField(upload_to='documents_pdf', blank=True)
    prix = models.IntegerField(default=0)
    date_pub = models.DateField(default=timezone.now)
    auteur = models.ForeignKey(auteur, on_delete= models.DO_NOTHING, default=1)
    
    def __str__(self):
        return self.Titre
    def get_absolute_url(self):
        return "affichage_livre"
    
# ================== classe carnet parole===================================
class pensesPositives(models.Model):
    TitreP = models.CharField(unique=True, max_length=200)
    contenus = models.TextField(blank=False)
    nom_auteur = models.CharField(max_length=100)
    date= models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.TitreP
    def get_absolute_url(self):
        return "affichage_penses"
    
# ================== classe carnet Image===================================
class messageImage(models.Model):
    nom_auteur = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank= False)
    date_mes = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nom_auteur
    def get_absolute_url(self):
        return "image_list"
    
# ================== classe faire Achats=================================== 
class achat(models.Model):
    nom_livre = models.ForeignKey(livre, on_delete= models.DO_NOTHING, default=1)
    nombre_piece = models.IntegerField(default=1)
    matricule = models.ForeignKey(creationCompte, on_delete= models.DO_NOTHING, default=0)
    Nom = models.CharField(max_length=90)
    email = models.EmailField()
    telephone = models.IntegerField(default=0)
    pays = models.CharField(max_length=90, blank=True)
    date_achat = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.Nom  
    def get_absolute_url(self):
        return "affichage_achat"
    
