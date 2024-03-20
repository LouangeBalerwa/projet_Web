from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'pages/home.html',)

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


def contact_submit(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      # Traiter les données du formulaire
      # Enregistrer le message, envoyer un email, etc.
      return HttpResponseRedirect('/')
  else:
    form = ContactForm()

  context = {'form': form}
  return render(request, 'contact.html', context)
