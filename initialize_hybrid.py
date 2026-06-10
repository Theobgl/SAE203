#!/usr/bin/env python
"""
Script d'initialisation hybride MongoDB/SQLite
Crée les migrations et les données initiales selon la DB disponible
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.conf import settings
from datetime import date

def initialize_sqlite():
    """Initialiser SQLite"""
    print("\n" + "="*60)
    print("🔄 Initialisation SQLite...")
    print("="*60 + "\n")

    # Créer les migrations
    print("📝 Création des migrations SQLite...")
    execute_from_command_line(['manage.py', 'makemigrations', 'app'])

    # Appliquer les migrations
    print("\n📝 Application des migrations...")
    execute_from_command_line(['manage.py', 'migrate'])

    # Importer les modèles SQLite
    from app.models_sqlite import Categorie, Produit, Client, Commande, LigneCommande

    # Créer les données initiales
    print("\n📂 Création des catégories...")
    categories = {
        'Boissons': Categorie.objects.create(nom='Boissons', descriptif='Boissons fraîches et sodas'),
        'Fruits': Categorie.objects.create(nom='Fruits', descriptif='Fruits frais de saison'),
        'Snacks': Categorie.objects.create(nom='Snacks', descriptif='Snacks et gâteaux'),
    }
    print(f"   ✅ {len(categories)} catégories créées")

    print("\n📦 Création des produits...")
    produits_data = [
        {'nom': 'Coca Cola 1L', 'prix': 2.50, 'marque': 'Coca Cola', 'date_peremption': '2026-12-31', 'categorie': 'Boissons'},
        {'nom': 'Jus Orange 1L', 'prix': 3.20, 'marque': 'Tropicana', 'date_peremption': '2026-10-15', 'categorie': 'Boissons'},
        {'nom': 'Pommes Gala kg', 'prix': 4.50, 'marque': 'Bio', 'date_peremption': '2026-06-25', 'categorie': 'Fruits'},
        {'nom': 'Chips Salée 200g', 'prix': 1.99, 'marque': "Lay's", 'date_peremption': '2026-12-01', 'categorie': 'Snacks'},
    ]

    for prod in produits_data:
        try:
            date_perm = prod['date_peremption']
            if isinstance(date_perm, str):
                from datetime import datetime
                date_perm = datetime.strptime(date_perm, '%Y-%m-%d').date()

            Produit.objects.get_or_create(
                nom=prod['nom'],
                defaults={
                    'prix': prod['prix'],
                    'marque': prod['marque'],
                    'date_peremption': date_perm,
                    'categorie': categories[prod['categorie']],
                }
            )
            print(f"   ✅ {prod['nom']}")
        except Exception as e:
            print(f"   ⚠️  {prod['nom']}: {e}")

    print("\n👥 Création des clients...")
    clients_data = [
        {'numero_client': 1, 'nom': 'Dupont', 'prenom': 'Jean', 'adresse': '12 rue des Fleurs'},
        {'numero_client': 2, 'nom': 'Martin', 'prenom': 'Claire', 'adresse': '45 avenue Principale'},
        {'numero_client': 3, 'nom': 'Bernard', 'prenom': 'Lucas', 'adresse': '78 route de Paris'},
    ]

    for client in clients_data:
        try:
            Client.objects.get_or_create(
                numero_client=client['numero_client'],
                defaults={
                    'nom': client['nom'],
                    'prenom': client['prenom'],
                    'adresse': client['adresse'],
                    'date_inscription': date.today(),
                }
            )
            print(f"   ✅ {client['prenom']} {client['nom']}")
        except Exception as e:
            print(f"   ⚠️  {client['prenom']} {client['nom']}: {e}")


def initialize_mongodb():
    """Initialiser MongoDB"""
    print("\n" + "="*60)
    print("🔄 Initialisation MongoDB...")
    print("="*60 + "\n")

    from app.models import Categorie, Produit, Client, Commande, LigneCommande

    # Créer les données initiales
    print("📂 Création des catégories...")
    categories = {}
    for cat_data in [
        {'nom': 'Boissons', 'descriptif': 'Boissons fraîches et sodas'},
        {'nom': 'Fruits', 'descriptif': 'Fruits frais de saison'},
        {'nom': 'Snacks', 'descriptif': 'Snacks et gâteaux'},
    ]:
        try:
            c = Categorie.objects.get(nom=cat_data['nom'])
        except:
            c = Categorie(nom=cat_data['nom'], descriptif=cat_data['descriptif'])
            c.save()
        categories[cat_data['nom']] = c
        print(f"   ✅ {cat_data['nom']}")

    print("\n📦 Création des produits...")
    for prod in [
        {'nom': 'Coca Cola 1L', 'prix': 2.50, 'marque': 'Coca Cola', 'date_peremption': '2026-12-31', 'categorie': 'Boissons'},
        {'nom': 'Jus Orange 1L', 'prix': 3.20, 'marque': 'Tropicana', 'date_peremption': '2026-10-15', 'categorie': 'Boissons'},
        {'nom': 'Pommes Gala kg', 'prix': 4.50, 'marque': 'Bio', 'date_peremption': '2026-06-25', 'categorie': 'Fruits'},
        {'nom': 'Chips Salée 200g', 'prix': 1.99, 'marque': "Lay's", 'date_peremption': '2026-12-01', 'categorie': 'Snacks'},
    ]:
        try:
            from datetime import datetime
            date_perm = datetime.strptime(prod['date_peremption'], '%Y-%m-%d').date()

            try:
                Produit.objects.get(nom=prod['nom'])
            except:
                p = Produit(
                    nom=prod['nom'],
                    prix=prod['prix'],
                    marque=prod['marque'],
                    date_peremption=date_perm,
                    categorie=categories[prod['categorie']]
                )
                p.save()
            print(f"   ✅ {prod['nom']}")
        except Exception as e:
            print(f"   ⚠️  {prod['nom']}: {e}")

    print("\n👥 Création des clients...")
    for client in [
        {'numero_client': 1, 'nom': 'Dupont', 'prenom': 'Jean', 'adresse': '12 rue des Fleurs'},
        {'numero_client': 2, 'nom': 'Martin', 'prenom': 'Claire', 'adresse': '45 avenue Principale'},
        {'numero_client': 3, 'nom': 'Bernard', 'prenom': 'Lucas', 'adresse': '78 route de Paris'},
    ]:
        try:
            Client.objects.get(numero_client=client['numero_client'])
        except:
            c = Client(
                numero_client=client['numero_client'],
                nom=client['nom'],
                prenom=client['prenom'],
                adresse=client['adresse'],
                date_inscription=date.today()
            )
            c.save()
        print(f"   ✅ {client['prenom']} {client['nom']}")


def main():
    """Fonction principale"""
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║   🚀 INITIALISATION HYBRIDE MONGODB/SQLITE                ║")
    print("╚════════════════════════════════════════════════════════════╝\n")

    if settings.MONGODB_ENABLED:
        print("📊 Base de données: MongoDB")
        initialize_mongodb()
    else:
        print("📊 Base de données: SQLite")
        initialize_sqlite()

    print("\n" + "="*60)
    print("✅ Initialisation réussie!")
    print("="*60)
    print("\nDémarrez maintenant:")
    print("  python manage.py runserver")
    print("\nOu sur un autre port:")
    print("  python manage.py runserver 8001\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Arrêt par l'utilisateur\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erreur: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)

