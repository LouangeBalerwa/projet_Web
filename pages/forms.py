from django.forms import ModelForm
from .models import auteur, creationCompte,pensesPositives, livre, messageImage, achat


class auteurForm(ModelForm):
    class Meta:
        model = auteur
        fields =['nom_auteur', 'email','num_tel', 'matricule','pays','ville',]
        
class compteForm(ModelForm):
    class Meta:
        model = creationCompte
        fields =['matricule','type_compte', 'balance',]

class pensesForm(ModelForm):
    class Meta:
        model = pensesPositives
        fields =['TitreP','contenus', 'nom_auteur', 'date',]

class livreForm(ModelForm):
    class Meta:
        model = livre
        fields = ['Titre','photo', 'fichier_pdf', 'prix', 'date_pub', 'auteur',]

class messageImgForm(ModelForm):
    class Meta:
        model = messageImage
        fields = ['nom_auteur', 'image','date_mes',]
        
class achatForm(ModelForm):
    class Meta:
        model = achat
        fields  =[ 'nom_livre', 'nombre_piece', 'matricule', 'Nom', 'email', 'telephone', 'pays', 'date_achat', ]