"""
Modèles Django pour SQLite (fallback)
Utilisés quand MongoDB n'est pas disponible
"""

from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    """Catégorie de produits (modèle SQLite)"""
    nom = models.CharField(max_length=200, unique=True)
    descriptif = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Catégories'
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Produit(models.Model):
    """Produit du drive (modèle SQLite)"""
    nom = models.CharField(max_length=200)
    prix = models.FloatField()
    marque = models.CharField(max_length=100, blank=True)
    date_peremption = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='produits/', blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'produits'
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.nom} ({self.marque})"


class Client(models.Model):
    """Client du drive (modèle SQLite)"""
    numero_client = models.IntegerField(unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    date_inscription = models.DateField()
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clients'
        ordering = ['numero_client']

    def __str__(self):
        return f"{self.numero_client} - {self.prenom} {self.nom}"

    def nom_complet(self):
        return f"{self.prenom} {self.nom}"


class Commande(models.Model):
    """Commande du client (modèle SQLite)"""
    numero_commande = models.IntegerField(unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commandes')
    date_commande = models.DateTimeField(auto_now_add=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'commandes'
        ordering = ['-date_commande']

    def __str__(self):
        return f"Commande #{self.numero_commande}"

    def total(self):
        """Calcule le total de la commande"""
        return sum(ligne.montant_total() for ligne in self.lignes.all())


class LigneCommande(models.Model):
    """Ligne d'une commande (modèle SQLite)"""
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    quantite = models.IntegerField(default=1)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'lignes_commande'
        unique_together = ('commande', 'produit')

    def __str__(self):
        return f"{self.quantite}x {self.produit.nom}"

    def montant_total(self):
        """Calcule le montant total de la ligne"""
        return self.produit.prix * self.quantite

