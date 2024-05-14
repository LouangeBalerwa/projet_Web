from django.urls import path
from . import views

app_name = 'pages'  

urlpatterns = [
    #PATH
    path('', views.home, name='home'),
    
    # =============Path about Auteurs====================================
    path('ajouter_auteur', views.ajouter_auteur, name = 'ajouter_auteur'),
    path('modifier_auteur/<int:id_auteur>/', views.modifier_auteur, name = 'modifier_auteur'),
    path('supprime_auteur/<int:id_auteur>/', views.supprime_auteur, name = 'supprime_auteur'),
    path('affichage_auteur', views.affichage_auteur, name ='affichage_auteur'),
    # =============Path Fin Auteurs======================================
    
    # =============Path Comptes ==========================================
    path('compte', views.creation_compte, name = 'compte'),
    path('affichage_compte', views.affichage_compte, name ='affichage_compte'),
    path('modifier_compte/<int:id_compte>/', views.modifier_compte, name = 'modifier_compte'),
    path('supprime_compte/<int:id_compte>/', views.supprime_compte, name = 'supprime_compte'),
    # =============Path Fin Comptes ==========================================
    
    # =============Path penses_Positives ==========================================
    path('pense_positives', views.pense_positive, name = 'pense_positives'),
    path('affichage_penses', views.affichage_penses, name ='affichage_penses'),
    # =============Path Fin  penses_Positives ==========================================
    path('mesLivres', views.mes_livres, name = 'mesLivres'),
    path('messageImg', views.message_image, name = 'messageImg'),
    path('image_list', views.image_list, name ='image_list'),
    
    path('formulaire', views.formulaire, name='formulaire'),
    path('categories', views.categories, name='categories'),
    # path('livres', views.livres, name ='livres'),
    path('penses', views.penses, name ='penses'),
    path('pub', views.publication, name ='pub'),
    path('article', views.articles, name='article'),
    path('about', views.about, name='about'),
   
]