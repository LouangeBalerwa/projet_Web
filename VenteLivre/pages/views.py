from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from .forms import auteurForm
from .models import auteur
from .import models
from django import forms 


def home(request):  
    return render(request, 'pages/home.html')

def ajouter_auteur(request):
  submitted = False
  if request.method == "POST":
    form = auteurForm(request.POST)
    if form.is_valid():
      auteurS = form.save()
      return redirect(auteurS) 
  else: 
    form = auteurForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, "pages/ajouter_auteur.html", {'form': form})

def affichage(request):
  try:
    auteurs  = auteur.objects.all()
              # auteur.objects.get(id = post_id)
              # .filter(is_published=True)
              # .order_by('num_tel')[:5])
  except:
    raise Http404("Cette page n'exciste pas!!!")
  
  data =  {'auteurs': auteurs}
  
  return render(request, 'pages/affichage.html', data) 

def modifier_auteur(request, id_auteur):
  data = get_object_or_404(auteur, id=id_auteur)
  # data = auteur.objects.get(id=id_auteur)
  if request.method == "POST":
    form = auteurForm(request.POST, instance=data)
    if form.is_valid():
      form.save() 
      return HttpResponseRedirect('/affichage') 
    
  else: 
    form = auteurForm(instance=data)
  return render(request, "pages/modifier_auteur.html", {'form': form, 'data': data})

def supprime_auteur(request, id_auteur):
  data = get_object_or_404(auteur, id=id_auteur)
  # data = auteur.objects.get(id=id_auteur)
  if request.method == "POST":
    data.delete()
    return HttpResponseRedirect('/affichage')   
  return render(request, "pages/supprime_auteur.html", {'data': data})

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
