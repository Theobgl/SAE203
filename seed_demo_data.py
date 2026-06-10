#!/usr/bin/env python
"""
Seed de donnees de demonstration pour Drive Alimentaire.
Creuse des categories, produits, clients et commandes factices.
Le script est idempotent: il peut etre relance sans dupliquer les donnees.
"""

import os
import sys
from datetime import date, datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

from app.models_adapter import Categorie, Produit, Client, Commande, LigneCommande


def ensure_category(name, description):
    category, _ = Categorie.objects.get_or_create(
        nom=name,
        defaults={"descriptif": description},
    )
    if not category.descriptif:
        category.descriptif = description
        category.save()
    return category


def ensure_product(data, category):
    produit, _ = Produit.objects.get_or_create(
        nom=data["nom"],
        defaults={
            "prix": data["prix"],
            "marque": data["marque"],
            "date_peremption": data["date_peremption"],
            "categorie": category,
        },
    )
    if produit.categorie != category:
        produit.categorie = category
    produit.prix = data["prix"]
    produit.marque = data["marque"]
    produit.date_peremption = data["date_peremption"]
    produit.save()
    return produit


def ensure_client(data):
    client, _ = Client.objects.get_or_create(
        numero_client=data["numero_client"],
        defaults={
            "nom": data["nom"],
            "prenom": data["prenom"],
            "adresse": data["adresse"],
            "date_inscription": data["date_inscription"],
        },
    )
    client.nom = data["nom"]
    client.prenom = data["prenom"]
    client.adresse = data["adresse"]
    client.date_inscription = data["date_inscription"]
    client.save()
    return client


def ensure_order(data, client_by_numero, product_by_name):
    commande, _ = Commande.objects.get_or_create(
        numero_commande=data["numero_commande"],
        defaults={
            "client": client_by_numero[data["client"]],
            "date_commande": data["date_commande"],
        },
    )
    if commande.client != client_by_numero[data["client"]]:
        commande.client = client_by_numero[data["client"]]
        commande.save()

    for line in data["lines"]:
        produit = product_by_name[line["produit"]]
        ligne, _ = LigneCommande.objects.get_or_create(
            commande=commande,
            produit=produit,
            defaults={"quantite": line["quantite"]},
        )
        ligne.quantite = line["quantite"]
        ligne.save()


def main():
    categories_data = [
        ("Boissons", "Boissons fraiches, jus et sodas"),
        ("Fruits et Legumes", "Produits frais de saison"),
        ("Epicerie", "Produits secs et conserves"),
        ("Snacks", "Encas et petites faim"),
    ]

    products_data = [
        {
            "nom": "Eau minerale 1.5L",
            "prix": 0.95,
            "marque": "Cristaline",
            "date_peremption": date(2027, 1, 15),
            "category": "Boissons",
        },
        {
            "nom": "Jus d'orange 1L",
            "prix": 2.85,
            "marque": "Tropicana",
            "date_peremption": date(2026, 10, 30),
            "category": "Boissons",
        },
        {
            "nom": "Pommes bio kg",
            "prix": 3.90,
            "marque": "BioVillage",
            "date_peremption": date(2026, 6, 25),
            "category": "Fruits et Legumes",
        },
        {
            "nom": "Tomates rondes kg",
            "prix": 2.40,
            "marque": "MarcheLocal",
            "date_peremption": date(2026, 6, 18),
            "category": "Fruits et Legumes",
        },
        {
            "nom": "Pates coquillettes 500g",
            "prix": 1.20,
            "marque": "Panzani",
            "date_peremption": date(2027, 2, 1),
            "category": "Epicerie",
        },
        {
            "nom": "Chocolat au lait 100g",
            "prix": 1.60,
            "marque": "Milka",
            "date_peremption": date(2026, 12, 20),
            "category": "Snacks",
        },
        {
            "nom": "Chips nature 150g",
            "prix": 1.99,
            "marque": "Lay's",
            "date_peremption": date(2026, 11, 10),
            "category": "Snacks",
        },
    ]

    clients_data = [
        {
            "numero_client": 1,
            "nom": "Dupont",
            "prenom": "Jean",
            "adresse": "12 rue des Fleurs, Lyon",
            "date_inscription": date(2026, 5, 12),
        },
        {
            "numero_client": 2,
            "nom": "Martin",
            "prenom": "Claire",
            "adresse": "45 avenue Principale, Villeurbanne",
            "date_inscription": date(2026, 5, 18),
        },
        {
            "numero_client": 3,
            "nom": "Bernard",
            "prenom": "Lucas",
            "adresse": "78 route de Paris, Bron",
            "date_inscription": date(2026, 5, 23),
        },
        {
            "numero_client": 4,
            "nom": "Petit",
            "prenom": "Sarah",
            "adresse": "9 place Bellecour, Lyon",
            "date_inscription": date(2026, 6, 1),
        },
    ]

    orders_data = [
        {
            "numero_commande": 1001,
            "client": 1,
            "date_commande": datetime(2026, 6, 2, 9, 15),
            "lines": [
                {"produit": "Eau minerale 1.5L", "quantite": 6},
                {"produit": "Pates coquillettes 500g", "quantite": 4},
                {"produit": "Chocolat au lait 100g", "quantite": 3},
            ],
        },
        {
            "numero_commande": 1002,
            "client": 2,
            "date_commande": datetime(2026, 6, 3, 11, 40),
            "lines": [
                {"produit": "Jus d'orange 1L", "quantite": 2},
                {"produit": "Pommes bio kg", "quantite": 5},
                {"produit": "Tomates rondes kg", "quantite": 2},
            ],
        },
        {
            "numero_commande": 1003,
            "client": 3,
            "date_commande": datetime(2026, 6, 4, 16, 5),
            "lines": [
                {"produit": "Chips nature 150g", "quantite": 8},
                {"produit": "Chocolat au lait 100g", "quantite": 6},
            ],
        },
        {
            "numero_commande": 1004,
            "client": 4,
            "date_commande": datetime(2026, 6, 5, 8, 50),
            "lines": [
                {"produit": "Eau minerale 1.5L", "quantite": 12},
                {"produit": "Jus d'orange 1L", "quantite": 3},
                {"produit": "Pommes bio kg", "quantite": 2},
            ],
        },
    ]

    categories = {name: ensure_category(name, desc) for name, desc in categories_data}
    products = {}
    for product in products_data:
        products[product["nom"]] = ensure_product(product, categories[product["category"]])

    clients = {}
    for client in clients_data:
        clients[client["numero_client"]] = ensure_client(client)

    for order in orders_data:
        ensure_order(order, clients, products)

    print("Seed termine.")
    print(f"Categories: {Categorie.objects.count()}")
    print(f"Produits: {Produit.objects.count()}")
    print(f"Clients: {Client.objects.count()}")
    print(f"Commandes: {Commande.objects.count()}")
    print(f"Lignes: {LigneCommande.objects.count()}")


if __name__ == "__main__":
    main()
