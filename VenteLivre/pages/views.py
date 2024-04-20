from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import auteurForm
from .models import auteur
from .import models
from django import forms 

def ajouter_auteur(request):
  submitted = False
  if request.method == "POST":
    form = auteurForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/categories') 
  else: 
    form = auteurForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, "pages/ajouter_auteur.html", {'form': form})

def affichage(request, id_auteur):
  auteurs  = auteur.objects.get(id=id_auteur)
              # auteur.objects.get(id = post_id)
              # .filter(is_published=True)
              # .order_by('num_tel')[:5])
  data =  {'auteurs': auteurs}
  
  return render(request, 'pages/affichage.html', data) 

def home(request):  
    return render(request, 'pages/home.html')

def articles(request):
    return render(request, 'pages/articles.html' )

def formulaire(request):
    return render(request, 'pages/formulaire.html')

def categories(request):
  return render(request, 'pages/categories.html')

def livres(request):
  return render(request, 'pages/livres.html')

def penses(request):
  return render(request, 'pages/pensesPositives.html')

def publication(request):
  return render(request, 'pages/publication.html')

def about(request):
  return render(request, 'pages/about.html')

def  contact(request):
  return render(request, 'pages/contact.html')
