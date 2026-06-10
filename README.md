# Drive Alimentaire - Django Application

Une application web complète de gestion de Drive alimentaire développée avec **Django**, **MongoDB** et **Bootstrap 5**.

## Fonctionnalités

✅ **CRUD Complet** pour les 5 entités principales :
- Categories
- Produits  
- Clients
- Commandes
- Lignes de commande

✅ **Fonctionnalités avancées** :
- Recherche et pagination sur tous les éléments
- Création de commandes avec sélection de produits
- Calcul automatique des totaux et montants
- Import de produits depuis CSV
- Initialisation des données de base

✅ **Interface moderne** :
- Bootstrap 5
- Navigation intuitive
- Messages de succès/erreur
- Design responsive

## Prérequis

- Python 3.8+
- MongoDB (en local ou distant)
- pip

## Installation

### 1. Cloner/Ouvrir le projet

```bash
cd C:\Users\theob\PycharmProjects\SAE203
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer MongoDB

**Option A : MongoDB Local**

Assurez-vous que MongoDB est installé et en cours d'exécution sur localhost:27017

```bash
# Windows
mongod.exe

# Linux/Mac
mongod
```

**Option B : MongoDB Atlas (Cloud)**

Modifiez le fichier `config/settings.py` :

```python
connect(
    db='drive_alimentaire',
    host='votre-cluster.mongodb.net',
    port=27017,
    username='votre_username',
    password='votre_password',
    authentication_source='admin',
    connect=False
)
```

### 5. Démarrer le serveur Django

```bash
python manage.py runserver
```

Le serveur sera accessible à : **http://localhost:8000**

## Utilisation

### Page d'accueil
- Accédez à http://localhost:8000
- Cliquez sur "Initialiser les données" pour charger les données de base

### Gestion des catégories
- Voir la liste : `/categories/`
- Créer : `/categories/creer/`
- Modifier : `/categories/<id>/modifier/`
- Supprimer : `/categories/<id>/supprimer/`

### Gestion des produits
- Voir la liste : `/produits/`
- Créer : `/produits/creer/`
- Import CSV : `/importer/`

### Gestion des clients
- Voir la liste : `/clients/`
- Créer : `/clients/creer/`

### Gestion des commandes
- Voir la liste : `/commandes/`
- Créer : `/commandes/creer/`

## Import CSV

Format attendu (séparé par des points-virgules) :
```
nom;prix;marque;date_peremption;categorie
Coca Cola 1L;2.50;Coca Cola;2026-12-31;Boissons
```

Un fichier exemple `sample_import.csv` est fourni.

## Structure du projet

```
SAE203/
├── config/
│   ├── settings.py          # Configuration Django
│   ├── urls.py              # URLs principales
│   ├── wsgi.py              # Application WSGI
│   └── __init__.py
├── app/
│   ├── models.py            # Modèles MongoEngine
│   ├── forms.py             # Formulaires Django
│   ├── views.py             # Vues et logique
│   ├── urls.py              # URLs de l'app
│   ├── apps.py              # Configuration app
│   └── __init__.py
├── templates/
│   ├── base.html            # Template de base
│   ├── accueil.html         # Accueil
│   ├── categories/          # Templates catégories
│   ├── produits/            # Templates produits
│   ├── clients/             # Templates clients
│   ├── commandes/           # Templates commandes
│   └── importer_produits.html
├── manage.py                # Utilitaire Django
├── requirements.txt         # Dépendances Python
├── sample_import.csv        # Fichier CSV exemple
└── README.md                # Ce fichier
```

## Collections MongoDB

### categories
```json
{
  "_id": ObjectId,
  "nom": "Boissons",
  "descriptif": "Boissons fraîches et sodas"
}
```

### produits
```json
{
  "_id": ObjectId,
  "nom": "Coca Cola 1L",
  "prix": 2.50,
  "marque": "Coca Cola",
  "date_peremption": "2026-12-31",
  "categorie_id": ObjectId,
  "photo": "Binary",
  "date_creation": "2026-06-10T14:30:00"
}
```

### clients
```json
{
  "_id": ObjectId,
  "numero_client": 1,
  "nom": "Dupont",
  "prenom": "Jean",
  "adresse": "12 rue des Fleurs",
  "date_inscription": "2026-01-10"
}
```

### commandes
```json
{
  "_id": ObjectId,
  "numero_commande": 1,
  "client_id": ObjectId,
  "date_commande": "2026-06-10T14:30:00"
}
```

### lignes_commande
```json
{
  "_id": ObjectId,
  "commande_id": ObjectId,
  "produit_id": ObjectId,
  "quantite": 3
}
```

## Technologies utilisées

- **Framework** : Django 4.2.0
- **Base de données** : MongoDB + MongoEngine 0.27.0
- **Frontend** : Bootstrap 5
- **Langage** : Python 3

## Notes importantes

- **Base NoSQL** : Cette application utilise MongoDB (NoSQL) au lieu d'une base SQL traditionnelle
- **Pagination** : Tous les affichages en liste incluent une pagination (10 éléments par page)
- **Recherche** : Recherche disponible sur produits et clients
- **Validation** : Les formulaires sont validés côté serveur
- **Messages** : Messages de succès/erreur pour chaque action

## Troubleshooting

### Erreur de connexion MongoDB
- Vérifiez que MongoDB est en cours d'exécution
- Vérifiez l'adresse du serveur MongoDB dans `config/settings.py`

### Erreur d'import des formulaires
- Les formulaires utilisent `mongoengine.django.forms.DocumentForm`
- Assurez-vous que MongoEngine est correctement installé

### Données non persistées
- Vérifiez que MongoDB fonctionne correctement
- Vérifiez que la base de données `drive_alimentaire` est créée

## Auteur

Application développée pour la SAE 203.

## Licence

MIT License

