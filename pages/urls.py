from django.urls import path
from . import views

app_name = 'pages'  

urlpatterns = [
    #PATH
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    
    # =============Path about Auteurs====================================
    path('ajouter_auteur', views.ajouter_auteur, name = 'ajouter_auteur'),
    path('modifier_auteur/<int:id_auteur>/', views.modifier_auteur, name = 'modifier_auteur'),
    path('supprime_auteur/<int:id_auteur>/', views.supprime_auteur, name = 'supprime_auteur'),
    path('affichage_auteur', views.affichage_auteur, name ='affichage_auteur'),
    # =============Path Fin Auteurs======================================
    
    # =============Path about Comptes ==========================================
    path('compte', views.creation_compte, name = 'compte'),
    path('affichage_compte', views.affichage_compte, name ='affichage_compte'),
    path('modifier_compte/<int:id_compte>/', views.modifier_compte, name = 'modifier_compte'),
    path('supprime_compte/<int:id_compte>/', views.supprime_compte, name = 'supprime_compte'),
    # =============Path Fin Comptes ==========================================
    
    # =============Path about penses_Positives ==========================================
    path('pense_positives', views.pense_positive, name = 'pense_positives'),
    path('affichage_penses', views.affichage_penses, name ='affichage_penses'),
    
    path('messageImg', views.message_image, name = 'messageImg'),
    path('image_list', views.image_list, name ='image_list'),
    # =============Path Fin  penses_Positives ==========================================
    
    # =============Path about livre ==========================================
    path('mesLivres', views.mes_livres, name = 'mesLivres'),
    path('affichage_livre', views.affichage_livre, name = 'affichage_livre'),
    # =============Path fin livre ==========================================
    
   
    # =============Path about Faire un ACHAT ==========================================
    path('formulaire', views.formulaire, name='formulaire'),
    path('affichage_achat', views.affichage_achat, name = 'affichage_achat'),
    # =============Path fin Faire un ACHAT ==========================================
    
    # =============Path  telechargement PDF ========================
    # path('telecharger_pdf/<int:livre_id>', views.telecharger_pdf, name='telecharger_pdf'),
    path('telecharger_pdf', views.telecharger_pdf, name='telecharger_pdf'),
    # =============Path about  A propos ==========================================
    path('about', views.about, name='about'),

    

]