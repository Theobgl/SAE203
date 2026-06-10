"""
Formulaires pour l'app Drive Alimentaire.
"""
from django import forms
from datetime import date


class CategorieForm(forms.Form):
    """
    Formulaire pour créer/modifier une catégorie.
    """
    nom = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la catégorie'})
    )
    descriptif = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriptif', 'rows': 3})
    )


class ProduitForm(forms.Form):
    """
    Formulaire pour créer/modifier un produit.
    """
    nom = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du produit'})
    )
    prix = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix', 'step': '0.01'})
    )
    marque = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marque'})
    )
    date_peremption = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    photo = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    categorie = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Catégorie'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Charger les catégories dynamiquement si nécessaire
        try:
            from app.models_adapter import Categorie
            categories = [(c.id, c.nom) for c in Categorie.objects.all()]
            self.fields['categorie'] = forms.ChoiceField(
                choices=categories,
                widget=forms.Select(attrs={'class': 'form-control'})
            )
        except:
            # Si pas de connexion à MongoDB, garder le formulaire simple
            pass


class ClientForm(forms.Form):
    """
    Formulaire pour créer/modifier un client.
    """
    nom = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'})
    )
    prenom = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'})
    )
    adresse = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'})
    )
    date_inscription = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )


class CommandeForm(forms.Form):
    """
    Formulaire pour créer/modifier une commande.
    """
    client = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            from app.models_adapter import Client
            clients = [(c.id, f"{c.numero_client} - {c.nom_complet()}") for c in Client.objects.all()]
            self.fields['client'] = forms.ChoiceField(
                choices=clients,
                widget=forms.Select(attrs={'class': 'form-control'})
            )
        except:
            pass


class LigneCommandeForm(forms.Form):
    """
    Formulaire pour créer/modifier une ligne de commande.
    """
    produit = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    quantite = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            from app.models_adapter import Produit
            produits = [(p.id, f"{p.nom} - {p.prix}€") for p in Produit.objects.all()]
            self.fields['produit'] = forms.ChoiceField(
                choices=produits,
                widget=forms.Select(attrs={'class': 'form-control'})
            )
        except:
            pass


class ImportCSVForm(forms.Form):
    """
    Formulaire pour importer des produits depuis un CSV.
    """
    fichier = forms.FileField(
        label='Fichier CSV',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'})
    )


class RechercheForm(forms.Form):
    """
    Formulaire de recherche.
    """
    q = forms.CharField(
        label='Rechercher',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rechercher...'})
    )

