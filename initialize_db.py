#!/usr/bin/env python
"""
Script d'initialisation du projet Drive Alimentaire
Crée les catégories, produits et clients de base
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from app.models import Categorie, Produit, Client, Commande, LigneCommande
from datetime import date, datetime

def initialize_database():
    """Initialise la base de données avec les données de base"""

    print("=" * 60)
    print("🚀 Initialisation de la base de données MongoDB")
    print("=" * 60)

    try:
        # 1. Créer les catégories
        print("\n📂 Création des catégories...")
        categories = [
            {'nom': 'Boissons', 'descriptif': 'Boissons fraîches et sodas'},
            {'nom': 'Fruits', 'descriptif': 'Fruits frais de saison'},
            {'nom': 'Snacks', 'descriptif': 'Snacks et gâteaux'},
        ]

        cat_dict = {}
        for cat_data in categories:
            try:
                c = Categorie.objects.get(nom=cat_data['nom'])
                print(f"  ✓ Catégorie '{cat_data['nom']}' déjà existante")
            except Categorie.DoesNotExist:
                c = Categorie(
                    nom=cat_data['nom'],
                    descriptif=cat_data['descriptif']
                )
                c.save()
                print(f"  ✅ Catégorie '{cat_data['nom']}' créée")

            cat_dict[cat_data['nom']] = c

        # 2. Créer les produits
        print("\n📦 Création des produits...")
        produits = [
            {
                'nom': 'Coca Cola 1L',
                'prix': 2.50,
                'marque': 'Coca Cola',
                'date_peremption': '2026-12-31',
                'categorie': 'Boissons'
            },
            {
                'nom': 'Jus Orange 1L',
                'prix': 3.20,
                'marque': 'Tropicana',
                'date_peremption': '2026-10-15',
                'categorie': 'Boissons'
            },
            {
                'nom': 'Pommes Gala kg',
                'prix': 4.50,
                'marque': 'Bio',
                'date_peremption': '2026-06-25',
                'categorie': 'Fruits'
            },
            {
                'nom': 'Chips Salée 200g',
                'prix': 1.99,
                'marque': "Lay's",
                'date_peremption': '2026-12-01',
                'categorie': 'Snacks'
            },
        ]

        for prod_data in produits:
            try:
                # Chercher par nom
                p = Produit.objects.get(nom=prod_data['nom'])
                print(f"  ✓ Produit '{prod_data['nom']}' déjà existant")
            except Produit.DoesNotExist:
                try:
                    date_perm = datetime.strptime(
                        prod_data['date_peremption'],
                        '%Y-%m-%d'
                    ).date()
                except ValueError:
                    date_perm = None

                p = Produit(
                    nom=prod_data['nom'],
                    prix=prod_data['prix'],
                    marque=prod_data['marque'],
                    date_peremption=date_perm,
                    categorie=cat_dict[prod_data['categorie']]
                )
                p.save()
                print(f"  ✅ Produit '{prod_data['nom']}' créé")

        # 3. Créer les clients
        print("\n👥 Création des clients...")
        clients = [
            {
                'numero_client': 1,
                'nom': 'Dupont',
                'prenom': 'Jean',
                'adresse': '12 rue des Fleurs'
            },
            {
                'numero_client': 2,
                'nom': 'Martin',
                'prenom': 'Claire',
                'adresse': '45 avenue Principale'
            },
            {
                'numero_client': 3,
                'nom': 'Bernard',
                'prenom': 'Lucas',
                'adresse': '78 route de Paris'
            },
        ]

        for client_data in clients:
            try:
                c = Client.objects.get(numero_client=client_data['numero_client'])
                print(f"  ✓ Client {client_data['numero_client']} ({client_data['prenom']} {client_data['nom']}) déjà existant")
            except Client.DoesNotExist:
                c = Client(
                    numero_client=client_data['numero_client'],
                    nom=client_data['nom'],
                    prenom=client_data['prenom'],
                    adresse=client_data['adresse'],
                    date_inscription=date.today()
                )
                c.save()
                print(f"  ✅ Client {client_data['numero_client']} ({client_data['prenom']} {client_data['nom']}) créé")

        print("\n" + "=" * 60)
        print("✅ Initialisation réussie!")
        print("=" * 60)
        print("\n📊 Résumé:")
        print(f"  • Catégories: {Categorie.objects.count()}")
        print(f"  • Produits: {Produit.objects.count()}")
        print(f"  • Clients: {Client.objects.count()}")
        print(f"  • Commandes: {Commande.objects.count()}")
        print(f"  • Lignes de commande: {LigneCommande.objects.count()}")

        print("\n🎉 L'application est prête à être utilisée!")
        print("   Lancez: python manage.py runserver")
        print("   Accédez à: http://localhost:8000")

    except Exception as e:
        print(f"\n❌ Erreur lors de l'initialisation: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    initialize_database()

