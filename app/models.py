"""
Models for the Drive Alimentaire app using MongoEngine.
"""
from mongoengine import Document, StringField, FloatField, DateTimeField, ReferenceField, ListField, IntField, DateField, FileField
from datetime import datetime


class Categorie(Document):
    """
    Catégorie de produits.
    """
    nom = StringField(required=True, unique=True)
    descriptif = StringField()
    
    meta = {
        'collection': 'categories',
        'ordering': ['nom']
    }
    
    def __str__(self):
        return self.nom


class Produit(Document):
    """
    Produit du Drive.
    """
    nom = StringField(required=True)
    prix = FloatField(required=True)
    marque = StringField()
    date_peremption = DateField()
    photo = FileField()
    categorie = ReferenceField(Categorie, required=True)
    date_creation = DateTimeField(default=datetime.now)
    
    meta = {
        'collection': 'produits',
        'ordering': ['-date_creation']
    }
    
    def __str__(self):
        return f"{self.nom} ({self.marque})"


class Client(Document):
    """
    Client du Drive.
    """
    numero_client = IntField(unique=True)
    nom = StringField(required=True)
    prenom = StringField(required=True)
    adresse = StringField(required=True)
    date_inscription = DateField(default=datetime.now().date)
    
    meta = {
        'collection': 'clients',
        'ordering': ['numero_client']
    }
    
    def __str__(self):
        return f"{self.numero_client} - {self.prenom} {self.nom}"
    
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"


class Commande(Document):
    """
    Commande du client.
    """
    numero_commande = IntField(unique=True)
    client = ReferenceField(Client, required=True)
    date_commande = DateTimeField(default=datetime.now)
    
    meta = {
        'collection': 'commandes',
        'ordering': ['-date_commande']
    }
    
    def __str__(self):
        return f"Commande #{self.numero_commande}"
    
    def total(self):
        """
        Calcule le total de la commande.
        """
        total = 0
        for ligne in LigneCommande.objects(commande=self):
            total += ligne.montant_total()
        return total


class LigneCommande(Document):
    """
    Ligne d'une commande.
    """
    commande = ReferenceField(Commande, required=True)
    produit = ReferenceField(Produit, required=True)
    quantite = IntField(required=True, min_value=1)
    
    meta = {
        'collection': 'lignes_commande',
        'ordering': ['commande']
    }
    
    def __str__(self):
        return f"{self.quantite}x {self.produit.nom}"
    
    def montant_total(self):
        """
        Calcule le montant total de la ligne.
        """
        return self.produit.prix * self.quantite

