from django.forms import ModelForm
from django import forms
from . import models
from .models import auteur

class auteurForm(ModelForm):
    class Meta:
        model = auteur
        fields =('nom_auteur', 'email','num_tel', 'pays', )