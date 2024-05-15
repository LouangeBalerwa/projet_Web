from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from .forms import auteurForm, compteForm, pensesForm, livreForm, messageImgForm, achatForm
from .models import auteur, creationCompte,pensesPositives, messageImage,livre, achat
from django import forms 

# ========================Page d'accueille=================
def home(request):  
    return render(request, 'pages/home.html')
# ======================Views pour les Auteurs ======================

#  ------------------add auteur -----------------------------
def ajouter_auteur(request):
  if request.method == "POST":
    form = auteurForm(request.POST)
    if form.is_valid():
      mes_auteurs = form.save()
      return redirect(mes_auteurs) # redirects get_absolute_url()
    
  else: 
    form = auteurForm()
  return render(request, "pages/ajouter_auteur.html", {'form': form})

#  ------------------Show auteur -----------------------------
def affichage_auteur(request):
  try:
    auteurs  = auteur.objects.all()
  except:
    raise Http404("Cette page n'exciste pas!!!")
  
  data =  {'auteurs': auteurs}
  
  return render(request, 'pages/affichage_auteur.html', data) 

#  ------------------Edit auteur -----------------------------
def modifier_auteur(request, id_auteur):
  # recuperation de donnee pour un auteur specifique
  data = get_object_or_404(auteur, id=id_auteur)
  # data = auteur.objects.get(id=id_auteur)
  if request.method == "POST":
    form = auteurForm(request.POST, instance=data)
    if form.is_valid():
      form.save() 
      return redirect('/affichage_auteur')   
    
  else: 
    form = auteurForm(instance=data)
  return render(request, "pages/modifier_auteur.html", {'form': form, 'data': data})

#  ------------------Delete auteur -----------------------------
def supprime_auteur(request, id_auteur):
  data = get_object_or_404(auteur, id=id_auteur)
  # data = auteur.objects.get(id=id_auteur)
  if request.method == "POST":
    data.delete()
    return redirect('/affichage_auteur')   
  
  return render(request, "pages/supprime_auteur.html", {'data': data})

# ======================FIN Auteurs ======================

# =======================lES COMPTES ==================
# ----------------------Add compte---------------------
def creation_compte(request):
  if request.method == "POST":
    form = compteForm(request.POST)
    if form.is_valid():
      comptes = form.save()
      return redirect(comptes) 
    
  else: 
    form = compteForm()
  return render(request, "pages/compte.html", {'form': form})

#  ------------------Show compte -----------------------------
def affichage_compte(request):
  try:
    comptes = creationCompte.objects.all()
  except:
    raise Http404("Cette page n'exciste pas!!!")
  
  data =  {'comptes': comptes}
  
  return render(request, 'pages/affichage_compte.html', data) 
  
  #  ------------------Edit Compte -----------------------------
def modifier_compte(request, id_compte):
  # recuperation de donnee pour un compte specifique
  data = get_object_or_404(creationCompte, id=id_compte)
  if request.method == "POST":
    form = compteForm(request.POST, instance=data)
    if form.is_valid():
      form.save() 
      return redirect('/affichage_compte')   
    
  else: 
    form = compteForm(instance=data)
  return render(request, "pages/modifier_compte.html", {'form': form, 'data': data})

#  ------------------Delete Compte -----------------------------
def supprime_compte(request, id_compte):
  data = get_object_or_404(creationCompte, id=id_compte)
  if request.method == "POST":
    data.delete()
    return redirect('/affichage_compte')   
  
  return render(request, "pages/supprime_compte.html", {'data': data})
# =======================FIN COMPTES ==================

# =======================View Penses Positives ==================
def pense_positive(request):
  if request.method == "POST":
    form = pensesForm(request.POST)
    if form.is_valid():
      pensess = form.save()
      return redirect(pensess) 
    
  else: 
    form = pensesForm()
  return render(request, "pages/pense_positives.html", {'form': form})

#  ------------------Show penses du jours -----------------------------
def affichage_penses(request):
  try:
    pense = pensesPositives.objects.all()
  except:
    raise Http404("Cette page n'exciste pas!!!")
  
  data =  {'penses':pense}
  
  return render(request, 'pages/affichage_penses.html', data) 

#  ------------------Add penses du jours image-----------------------------
def message_image(request):
    if request.method == 'POST':
      form = messageImgForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        messageImage = form.save()
        return redirect(messageImage) 
    else:
        form = messageImgForm()
    return render(request, 'pages/messageImg.html.',{'form': form})

# ------------------Show penses du jours image -----------------------------
def image_list(request):
  try:
    messages = messageImage.objects.all()
  except:
    raise Http404("Cette page n'exciste pas!!!")
  
  data =  {'messages': messages}
  
  return render(request, 'pages/image_list.html', data)

# =======================FIN PENSES POSITIVES ==================

# =======================view LIVRE ===================
#  ------------------Add livre -----------------------------
def mes_livres(request):
  
  if request.method == "POST":
    
    # try:
    
      print("=======>",request.POST)
      print("=======>",request.FILES)
      auteur_obj=auteur.objects.get(pk=2)
      
      data = livre(
          Titre=request.POST["Titre"],
          auteur=auteur_obj,
          photo=request.POST["photo"] ,
          fichier_pdf=request.POST['fichier_pdf'], 
          prix=request.POST["prix"],
         
      )
      
      data.save()
      return redirect('/affichage_livre') 
        
    # except:
    #     print("Error")
    #     return render(request, 'pages/livres.html',{'form': livreForm})
      
  else:     
    return render(request, 'pages/livres.html',{'form': livreForm})
  
#  ------------------Show Livres -----------------------------
def affichage_livre(request):
  livres = livre.objects.all()
  data = { 'livres': livres}
  return render(request, 'pages/affichage_livre.html', data)

# =======================Fin LIVRE ==================



def articles(request):
    return render(request, 'pages/articles.html' )

def formulaire(request):
    if request.method == "POST":
      form = achatForm(request.POST)
      if form.is_valid():
        achat = form.save()
      return redirect(achat)  
    else: 
      form = achatForm()
    return render(request, 'pages/formulaire.html',{'form': form})

def affichage_achat(request):
  n_achats = achat.objects.all()
  data = { 'n_achats': n_achats}
  return render(request, 'pages/affichage_achat.html')

def categories(request):
  return render(request, 'pages/categories.html')


def penses(request):
  return render(request, 'pages/pensesPositives.html')

def publication(request):
  return render(request, 'pages/publication.html')

def about(request):
  return render(request, 'pages/about.html')

def  contact(request):
  return render(request, 'pages/contact.html')
