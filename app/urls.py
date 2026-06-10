"""
URL Configuration for the app
"""
from django.urls import path
from app import views

urlpatterns = [
    # Accueil
    path('', views.accueil, name='accueil'),
    path('initialize/', views.initialize_data, name='initialize_data'),

    # Catégories
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/creer/', views.creer_categorie, name='creer_categorie'),
    path('categories/<id>/modifier/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/<id>/supprimer/', views.supprimer_categorie, name='supprimer_categorie'),
    path('categories/<id>/', views.voir_categorie, name='voir_categorie'),

    # Produits
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/creer/', views.creer_produit, name='creer_produit'),
    path('produits/<id>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('produits/<id>/supprimer/', views.supprimer_produit, name='supprimer_produit'),
    path('produits/<id>/', views.voir_produit, name='voir_produit'),

    # Clients
    path('clients/', views.liste_clients, name='liste_clients'),
    path('clients/creer/', views.creer_client, name='creer_client'),
    path('clients/<id>/modifier/', views.modifier_client, name='modifier_client'),
    path('clients/<id>/supprimer/', views.supprimer_client, name='supprimer_client'),
    path('clients/<id>/', views.voir_client, name='voir_client'),

    # Commandes
    path('commandes/', views.liste_commandes, name='liste_commandes'),
    path('commandes/creer/', views.creer_commande, name='creer_commande'),
    path('commandes/<id>/modifier/', views.modifier_commande, name='modifier_commande'),
    path('commandes/<id>/supprimer/', views.supprimer_commande, name='supprimer_commande'),
    path('commandes/<id>/', views.voir_commande, name='voir_commande'),
    path('commandes/<commande_id>/ajouter_ligne/', views.ajouter_ligne_commande, name='ajouter_ligne_commande'),
    path('lignes/<ligne_id>/supprimer/', views.supprimer_ligne_commande, name='supprimer_ligne_commande'),

    # Import CSV
    path('importer/', views.importer_produits, name='importer_produits'),
]

