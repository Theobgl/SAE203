"""
Vues pour l'app Drive Alimentaire.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.db import IntegrityError, transaction
import csv
import io
from datetime import datetime, date

from app.models_adapter import Categorie, Produit, Client, Commande, LigneCommande
from app.forms import (
    CategorieForm, ProduitForm, ClientForm, CommandeForm,
    LigneCommandeForm, ImportCSVForm, RechercheForm
)


# ==================== ACCUEIL ====================

def accueil(request):
    """
    Page d'accueil avec tableau de bord.
    """
    context = {
        'nb_categories': Categorie.objects.count(),
        'nb_produits': Produit.objects.count(),
        'nb_clients': Client.objects.count(),
        'nb_commandes': Commande.objects.count(),
    }
    return render(request, 'accueil.html', context)


# ==================== CATEGORIES ====================

def liste_categories(request):
    """
    Affiche la liste des catégories avec pagination.
    """
    categories = Categorie.objects.all()

    # Recherche
    form = RechercheForm(request.GET)
    if form.is_valid() and form.cleaned_data.get('q'):
        q = form.cleaned_data['q']
        categories = Categorie.objects.filter(nom__icontains=q)

    # Pagination
    paginator = Paginator(list(categories), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'categories/liste.html', {
        'page_obj': page_obj,
        'form': form,
    })


def creer_categorie(request):
    """
    Crée une nouvelle catégorie.
    """
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            categorie = Categorie(
                nom=form.cleaned_data['nom'],
                descriptif=form.cleaned_data['descriptif']
            )
            categorie.save()
            messages.success(request, 'Catégorie créée avec succès!')
            return redirect('liste_categories')
    else:
        form = CategorieForm()

    return render(request, 'categories/form.html', {
        'form': form,
        'titre': 'Créer une catégorie'
    })


def modifier_categorie(request, id):
    """
    Modifie une catégorie.
    """
    categorie = get_object_or_404(Categorie, id=id)

    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            categorie.nom = form.cleaned_data['nom']
            categorie.descriptif = form.cleaned_data['descriptif']
            categorie.save()
            messages.success(request, 'Catégorie modifiée avec succès!')
            return redirect('liste_categories')
    else:
        form = CategorieForm(initial={
            'nom': categorie.nom,
            'descriptif': categorie.descriptif
        })

    return render(request, 'categories/form.html', {
        'form': form,
        'titre': 'Modifier la catégorie'
    })


def supprimer_categorie(request, id):
    """
    Supprime une catégorie.
    """
    categorie = get_object_or_404(Categorie, id=id)

    if request.method == 'POST':
        categorie.delete()
        messages.success(request, 'Catégorie supprimée avec succès!')
        return redirect('liste_categories')

    return render(request, 'categories/confirmer_suppression.html', {
        'categorie': categorie
    })


def voir_categorie(request, id):
    """
    Affiche les détails d'une catégorie.
    """
    categorie = get_object_or_404(Categorie, id=id)
    produits = Produit.objects.filter(categorie=categorie)

    return render(request, 'categories/detail.html', {
        'categorie': categorie,
        'produits': produits
    })


# ==================== PRODUITS ====================

def liste_produits(request):
    """
    Affiche la liste des produits avec pagination et recherche.
    """
    produits = Produit.objects.all()

    # Recherche
    form = RechercheForm(request.GET)
    if form.is_valid() and form.cleaned_data.get('q'):
        q = form.cleaned_data['q']
        produits = Produit.objects.filter(
            Q(nom__icontains=q) | Q(marque__icontains=q)
        )

    # Pagination
    paginator = Paginator(list(produits), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'produits/liste.html', {
        'page_obj': page_obj,
        'form': form,
    })


def creer_produit(request):
    """
    Crée un nouveau produit.
    """
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            categorie_id = form.cleaned_data['categorie']
            produit = Produit(
                nom=form.cleaned_data['nom'],
                prix=form.cleaned_data['prix'],
                marque=form.cleaned_data['marque'],
                date_peremption=form.cleaned_data.get('date_peremption'),
                categorie=Categorie.objects.get(id=categorie_id)
            )
            if request.FILES.get('photo'):
                produit.photo = request.FILES['photo']
            produit.save()
            messages.success(request, 'Produit créé avec succès!')
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    
    return render(request, 'produits/form.html', {
        'form': form,
        'titre': 'Créer un produit'
    })


def modifier_produit(request, id):
    """
    Modifie un produit.
    """
    produit = get_object_or_404(Produit, id=id)
    
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            categorie_id = form.cleaned_data['categorie']
            produit.nom = form.cleaned_data['nom']
            produit.prix = form.cleaned_data['prix']
            produit.marque = form.cleaned_data['marque']
            produit.date_peremption = form.cleaned_data.get('date_peremption')
            produit.categorie = Categorie.objects.get(id=categorie_id)
            if request.FILES.get('photo'):
                produit.photo = request.FILES['photo']
            produit.save()
            messages.success(request, 'Produit modifié avec succès!')
            return redirect('liste_produits')
    else:
        form = ProduitForm(initial={
            'nom': produit.nom,
            'prix': produit.prix,
            'marque': produit.marque,
            'date_peremption': produit.date_peremption,
            'categorie': produit.categorie.id if produit.categorie else None
        })
    
    return render(request, 'produits/form.html', {
        'form': form,
        'titre': 'Modifier le produit'
    })


def supprimer_produit(request, id):
    """
    Supprime un produit.
    """
    produit = get_object_or_404(Produit, id=id)

    if request.method == 'POST':
        produit.delete()
        messages.success(request, 'Produit supprimé avec succès!')
        return redirect('liste_produits')

    return render(request, 'produits/confirmer_suppression.html', {
        'produit': produit
    })


def voir_produit(request, id):
    """
    Affiche les détails d'un produit.
    """
    produit = get_object_or_404(Produit, id=id)

    return render(request, 'produits/detail.html', {
        'produit': produit
    })


# ==================== CLIENTS ====================

def liste_clients(request):
    """
    Affiche la liste des clients avec pagination et recherche.
    """
    clients = Client.objects.all()

    # Recherche
    form = RechercheForm(request.GET)
    if form.is_valid() and form.cleaned_data.get('q'):
        q = form.cleaned_data['q']
        clients = Client.objects.filter(
            Q(nom__icontains=q) | Q(prenom__icontains=q)
        )

    # Pagination
    paginator = Paginator(list(clients), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'clients/liste.html', {
        'page_obj': page_obj,
        'form': form,
    })


def creer_client(request):
    """
    Crée un nouveau client.
    """
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # Attribuer un numéro libre côté serveur
            numero_client = 1
            try:
                dernier = Client.objects.order_by('-numero_client').first()
                numero_client = (dernier.numero_client + 1) if dernier else 1
            except Exception:
                numero_client = 1

            while Client.objects.filter(numero_client=numero_client).exists():
                numero_client += 1

            try:
                with transaction.atomic():
                    client = Client(
                        numero_client=numero_client,
                        nom=form.cleaned_data['nom'],
                        prenom=form.cleaned_data['prenom'],
                        adresse=form.cleaned_data['adresse'],
                        date_inscription=form.cleaned_data['date_inscription']
                    )
                    client.save()
                messages.success(request, f'Client créé avec succès! Numéro: {numero_client}')
                return redirect('liste_clients')
            except IntegrityError:
                messages.error(request, 'Un client avec ce numéro existe déjà. Réessayez.')
    else:
        form = ClientForm(initial={'date_inscription': date.today()})
    
    return render(request, 'clients/form.html', {
        'form': form,
        'titre': 'Créer un client'
    })


def modifier_client(request, id):
    """
    Modifie un client.
    """
    client = get_object_or_404(Client, id=id)
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client.nom = form.cleaned_data['nom']
            client.prenom = form.cleaned_data['prenom']
            client.adresse = form.cleaned_data['adresse']
            client.date_inscription = form.cleaned_data['date_inscription']
            client.save()
            messages.success(request, 'Client modifié avec succès!')
            return redirect('liste_clients')
    else:
        form = ClientForm(initial={
            'nom': client.nom,
            'prenom': client.prenom,
            'adresse': client.adresse,
            'date_inscription': client.date_inscription
        })
    
    return render(request, 'clients/form.html', {
        'form': form,
        'titre': 'Modifier le client'
    })


def supprimer_client(request, id):
    """
    Supprime un client.
    """
    client = get_object_or_404(Client, id=id)

    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client supprimé avec succès!')
        return redirect('liste_clients')

    return render(request, 'clients/confirmer_suppression.html', {
        'client': client
    })


def voir_client(request, id):
    """
    Affiche les détails d'un client.
    """
    client = get_object_or_404(Client, id=id)
    commandes = Commande.objects.filter(client=client)

    return render(request, 'clients/detail.html', {
        'client': client,
        'commandes': commandes
    })


# ==================== COMMANDES ====================

def liste_commandes(request):
    """
    Affiche la liste des commandes avec pagination.
    """
    commandes = Commande.objects.all()

    # Pagination
    paginator = Paginator(list(commandes), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'commandes/liste.html', {
        'page_obj': page_obj,
    })


def creer_commande(request):
    """
    Crée une nouvelle commande avec ses lignes.
    """
    if request.method == 'POST':
        client_id = request.POST.get('client')
        if not client_id:
            messages.error(request, 'Veuillez sélectionner un client!')
            return redirect('creer_commande')

        try:
            client = Client.objects.get(id=client_id)

            # Créer la commande
            max_numero = None
            try:
                max_numero = Commande.objects.order_by('-numero_commande').first()
            except:
                pass

            numero = (max_numero.numero_commande + 1) if max_numero else 1
            while Commande.objects.filter(numero_commande=numero).exists():
                numero += 1

            commande = Commande(
                numero_commande=numero,
                client=client,
                date_commande=datetime.now()
            )
            commande.save()

            # Ajouter les lignes de commande
            produit_ids = request.POST.getlist('produit_id')
            quantites = request.POST.getlist('quantite')

            for produit_id, quantite in zip(produit_ids, quantites):
                if quantite and int(quantite) > 0:
                    produit = Produit.objects.get(id=produit_id)
                    ligne = LigneCommande(
                        commande=commande,
                        produit=produit,
                        quantite=int(quantite)
                    )
                    ligne.save()

            messages.success(request, 'Commande créée avec succès!')
            return redirect('voir_commande', id=commande.id)

        except Client.DoesNotExist:
            messages.error(request, 'Client non trouvé!')
        except Exception as e:
            messages.error(request, f'Erreur : {str(e)}')

    clients = Client.objects.all()
    produits = Produit.objects.all()

    return render(request, 'commandes/creer.html', {
        'clients': clients,
        'produits': produits,
    })


def modifier_commande(request, id):
    """
    Modifie une commande.
    """
    commande = get_object_or_404(Commande, id=id)

    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            client_id = form.cleaned_data['client']
            commande.client = Client.objects.get(id=client_id)
            commande.save()
            messages.success(request, 'Commande modifiée avec succès!')
            return redirect('voir_commande', id=commande.id)
    else:
        form = CommandeForm(initial={'client': commande.client.id})

    return render(request, 'commandes/form.html', {
        'form': form,
        'titre': 'Modifier la commande'
    })


def supprimer_commande(request, id):
    """
    Supprime une commande.
    """
    commande = get_object_or_404(Commande, id=id)

    if request.method == 'POST':
        commande.delete()
        messages.success(request, 'Commande supprimée avec succès!')
        return redirect('liste_commandes')

    return render(request, 'commandes/confirmer_suppression.html', {
        'commande': commande
    })


def voir_commande(request, id):
    """
    Affiche les détails d'une commande.
    """
    commande = get_object_or_404(Commande, id=id)
    lignes = LigneCommande.objects.filter(commande=commande)
    total = commande.total()

    return render(request, 'commandes/detail.html', {
        'commande': commande,
        'lignes': lignes,
        'total': total,
    })


def ajouter_ligne_commande(request, commande_id):
    """
    Ajoute une ligne à une commande.
    """
    commande = get_object_or_404(Commande, id=commande_id)

    if request.method == 'POST':
        form = LigneCommandeForm(request.POST)
        if form.is_valid():
            produit_id = form.cleaned_data['produit']
            produit = Produit.objects.get(id=produit_id)
            quantite = form.cleaned_data['quantite']
            ligne = LigneCommande.objects.filter(commande=commande, produit=produit).first()
            if ligne:
                ligne.quantite += quantite
            else:
                ligne = LigneCommande(
                    commande=commande,
                    produit=produit,
                    quantite=quantite
                )
            ligne.save()
            messages.success(request, 'Ligne ajoutée avec succès!')
            return redirect('voir_commande', id=commande.id)
    else:
        form = LigneCommandeForm()

    return render(request, 'commandes/ajouter_ligne.html', {
        'form': form,
        'commande': commande,
    })


def supprimer_ligne_commande(request, ligne_id):
    """
    Supprime une ligne de commande.
    """
    ligne = get_object_or_404(LigneCommande, id=ligne_id)
    commande_id = ligne.commande.id

    if request.method == 'POST':
        ligne.delete()
        messages.success(request, 'Ligne supprimée avec succès!')
        return redirect('voir_commande', id=commande_id)

    return render(request, 'commandes/confirmer_suppression_ligne.html', {
        'ligne': ligne
    })


# ==================== IMPORT CSV ====================

def importer_produits(request):
    """
    Importe des produits depuis un fichier CSV.
    Format: nom;prix;marque;date_peremption;categorie
    """
    if request.method == 'POST':
        form = ImportCSVForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = request.FILES['fichier']

            try:
                fichier_texte = io.TextIOWrapper(fichier, encoding='utf-8')
                lecteur = csv.reader(fichier_texte, delimiter=';')

                nb_importes = 0
                erreurs = []

                for i, ligne in enumerate(lecteur, 1):
                    try:
                        if len(ligne) < 5:
                            erreurs.append(f"Ligne {i}: Format invalide")
                            continue

                        nom, prix, marque, date_peremption, nom_categorie = ligne

                        # Chercher ou créer la catégorie
                        try:
                            categorie = Categorie.objects.get(nom=nom_categorie.strip())
                        except Categorie.DoesNotExist:
                            categorie = Categorie(
                                nom=nom_categorie.strip(),
                                descriptif=''
                            )
                            categorie.save()

                        # Créer le produit
                        try:
                            date_perm = datetime.strptime(date_peremption.strip(), '%Y-%m-%d').date()
                        except ValueError:
                            date_perm = None

                        produit = Produit(
                            nom=nom.strip(),
                            prix=float(prix.strip()),
                            marque=marque.strip(),
                            date_peremption=date_perm,
                            categorie=categorie
                        )
                        produit.save()
                        nb_importes += 1

                    except Exception as e:
                        erreurs.append(f"Ligne {i}: {str(e)}")

                context = {
                    'nb_importes': nb_importes,
                    'erreurs': erreurs,
                    'succes': True if nb_importes > 0 else False,
                }

                if nb_importes > 0:
                    messages.success(request, f'{nb_importes} produit(s) importé(s) avec succès!')
                if erreurs:
                    messages.warning(request, f'{len(erreurs)} erreur(s) lors de l\'import')

                return render(request, 'importer_produits.html', context)

            except Exception as e:
                messages.error(request, f'Erreur lors de la lecture du fichier: {str(e)}')
    else:
        form = ImportCSVForm()

    return render(request, 'importer_produits.html', {'form': form})


def initialize_data(request):
    """
    Initialise les données de la base de données.
    """
    from django.views.decorators.http import require_http_methods

    try:
        # Créer les catégories
        categories = [
            {'nom': 'Boissons', 'descriptif': 'Boissons fraîches et sodas'},
            {'nom': 'Fruits', 'descriptif': 'Fruits frais de saison'},
            {'nom': 'Snacks', 'descriptif': 'Snacks et gâteaux'},
        ]

        cat_dict = {}
        for cat in categories:
            try:
                c = Categorie.objects.get(nom=cat['nom'])
            except Categorie.DoesNotExist:
                c = Categorie(nom=cat['nom'], descriptif=cat['descriptif'])
                c.save()
            cat_dict[cat['nom']] = c

        # Créer les produits
        produits = [
            {'nom': 'Coca Cola 1L', 'prix': 2.50, 'marque': 'Coca Cola', 'date_peremption': '2026-12-31', 'categorie': 'Boissons'},
            {'nom': 'Jus Orange 1L', 'prix': 3.20, 'marque': 'Tropicana', 'date_peremption': '2026-10-15', 'categorie': 'Boissons'},
            {'nom': 'Pommes Gala kg', 'prix': 4.50, 'marque': 'Bio', 'date_peremption': '2026-06-25', 'categorie': 'Fruits'},
            {'nom': 'Chips Salée 200g', 'prix': 1.99, 'marque': 'Lay\'s', 'date_peremption': '2026-12-01', 'categorie': 'Snacks'},
        ]

        for prod in produits:
            try:
                date_perm = datetime.strptime(prod['date_peremption'], '%Y-%m-%d').date()
            except:
                date_perm = None

            try:
                Produit.objects.get(nom=prod['nom'])
            except Produit.DoesNotExist:
                produit = Produit(
                    nom=prod['nom'],
                    prix=prod['prix'],
                    marque=prod['marque'],
                    date_peremption=date_perm,
                    categorie=cat_dict[prod['categorie']]
                )
                produit.save()

        # Créer les clients
        clients = [
            {'numero_client': 1, 'nom': 'Dupont', 'prenom': 'Jean', 'adresse': '12 rue des Fleurs'},
            {'numero_client': 2, 'nom': 'Martin', 'prenom': 'Claire', 'adresse': '45 avenue Principale'},
            {'numero_client': 3, 'nom': 'Bernard', 'prenom': 'Lucas', 'adresse': '78 route de Paris'},
        ]

        for client in clients:
            try:
                Client.objects.get(numero_client=client['numero_client'])
            except Client.DoesNotExist:
                nouveau_client = Client(
                    numero_client=client['numero_client'],
                    nom=client['nom'],
                    prenom=client['prenom'],
                    adresse=client['adresse'],
                    date_inscription=date.today()
                )
                nouveau_client.save()

        messages.success(request, 'Données initiales créées avec succès!')

    except Exception as e:
        messages.error(request, f'Erreur lors de l\'initialisation: {str(e)}')

    return redirect('accueil')

