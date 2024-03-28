from django.shortcuts import render

def home(request):
    # auteurs = auteur.objects.all()
    
    # data = {
    #   'auteurs_livres': auteurs
    # }
    
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

