from django.urls import path
from . import views

# app_name = 'pages'  
urlpatterns = [
    # Standalone Web Pages
    path('', views.home, name='home'),
    path('ajouter_auteur', views.ajouter_auteur, name = 'ajouter_auteur'),
    path('affichage', views.affichage, name ='affichage'),
    path('modifier_auteur/<int:id_auteur>/', views.modifier_auteur, name = 'modifier_auteur'),
    path('supprime_auteur/<int:id_auteur>/', views.supprime_auteur, name = 'supprime_auteur'),
    path('formulaire', views.formulaire, name='formulaire'),
    path('categories', views.categories, name='categories'),
    path('livres', views.livres, name ='livres'),
    path('penses', views.penses, name ='penses'),
    path('pub', views.publication, name ='pub'),
    path('article', views.articles, name='article'),
    path('about', views.about, name='about'),
   
]