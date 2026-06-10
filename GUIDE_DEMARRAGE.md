# Guide de Démarrage - Drive Alimentaire

## 📋 Vue d'ensemble

Application web complète de gestion d'un Drive alimentaire, développée avec:
- **Python 3.14+**
- **Django 4.2**
- **MongoDB** (NoSQL)
- **MongoEngine** (ORM pour MongoDB)
- **Bootstrap 5** (Interface utilisateur)

## ✅ Prérequis

1. **Python 3** installé
2. **MongoDB** en fonctionnement (local ou distant)
3. **Virtual Environment** Python activé

## 🚀 Installation et Démarrage

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Vérifier la configuration Django

```bash
python manage.py check
```

### 3. Démarrer le serveur Django

```bash
python manage.py runserver
```

Accédez à l'application via: **http://localhost:8000**

## 📂 Structure du Projet

```
SAE203/
├── app/                          # Application principale
│   ├── models.py                 # Modèles MongoEngine
│   ├── views.py                  # Vues Django
│   ├── forms.py                  # Formulaires Django
│   ├── urls.py                   # Routes URL
│   └── __init__.py
├── config/                       # Configuration Django
│   ├── settings.py               # Paramètres généraux
│   ├── urls.py                   # Configuration URL principale
│   └── wsgi.py
├── templates/                    # Templates HTML
│   ├── base.html                 # Template de base (Bootstrap 5)
│   ├── accueil.html              # Page d'accueil
│   ├── importer_produits.html    # Import CSV
│   ├── categories/               # Templates catégories CRUD
│   ├── produits/                 # Templates produits CRUD
│   ├── clients/                  # Templates clients CRUD
│   └── commandes/                # Templates commandes CRUD
├── requirements.txt              # Dépendances Python
├── manage.py                     # Utilitaire Django
└── README.md                     # Documentation principale

```

## 🗄️ Configuration MongoDB

Par défaut, l'application se connecte à MongoDB sur:**localhost:27017**

Pour utiliser une autre connexion, modifiez dans `config/settings.py`:

```python
connect(
    db='drive_alimentaire',
    host='votre-hote',
    port=27017,
    connect=False
)
```

## 📊 Collections MongoDB

L'application utilise 5 collections MongoDB:

### 1. **categories**
- Catégories de produits (Boissons, Fruits, Snacks)

### 2. **produits**
- Produits du Drive
- Lié à une catégorie

### 3. **clients**
- Clients du Drive
- Numéro unique par client

### 4. **commandes**
- Commandes des clients
- Numéro unique par commande

### 5. **lignes_commande**
- Détails des lignes de chaque commande
- Quantités et références produits

## ⚙️ Fonctionnalités Principales

### CRUD Complets

- ✅ **Catégories**: Créer, Lire, Modifier, Supprimer
- ✅ **Produits**: Créer, Lire, Modifier, Supprimer
- ✅ **Clients**: Créer, Lire, Modifier, Supprimer
- ✅ **Commandes**: Créer, Lire, Modifier, Supprimer
- ✅ **Lignes de commande**: Ajouter, Supprimer

### Pages de Listes

- 📋 Tableaux avec pagination (10 éléments par page)
- 🔍 Recherche en temps réel
- 🔘 Boutons d'action (Ajouter, Modifier, Supprimer, Voir)

### Spécificités

- 🛒 **Création de commande**: Interface intuitive pour créer une commande avec plusieurs produits
- 📄 **Fiche commande**: Affichage détaillé avec calcul automatique du total
- 📤 **Import CSV**: Importation en masse de produits avec création automatique des catégories
- 📊 **Dashboard**: Statistiques rapides sur accueil

## 🔑 Pages Principales

### Navigation

| URL | Page | Description |
|-----|------|-------------|
| `/` | Accueil | Tableau de bord avec statistiques |
| `/categories/` | Catégories | Liste des catégories |
| `/produits/` | Produits | Liste des produits |
| `/clients/` | Clients | Liste des clients |
| `/commandes/` | Commandes | Liste des commandes |
| `/importer/` | Import CSV | Importation de produits |

## 📝 Initialisation des Données

Au premier lancement, initialisez les données de base:

1. Accédez à: **http://localhost:8000**
2. Cliquez sur le bouton **"Initialiser les données"**
3. Les catégories, produits et clients par défaut seront créés

### Données créées par défaut:

**Catégories:**
- Boissons
- Fruits
- Snacks

**Produits:**
- Coca Cola 1L (2.50€)
- Jus Orange 1L (3.20€)
- Pommes Gala kg (4.50€)
- Chips Salée 200g (1.99€)

**Clients:**
- Jean Dupont
- Claire Martin
- Lucas Bernard

## 📤 Import CSV

### Format attendu:

```
nom;prix;marque;date_peremption;categorie
Coca Cola 1L;2.50;Coca Cola;2026-12-31;Boissons
Jus Orange;3.20;Tropicana;2026-10-15;Boissons
```

Format du fichier:
- **Délimiteur**: point-virgule (`;`)
- **Encodage**: UTF-8
- **Colonnes**: nom, prix, marque, date_peremption, categorie

### Comportement:

- La catégorie est recherchée en base
- Si elle n'existe pas, elle est créée automatiquement
- Le produit est inséré dans MongoDB
- Un rapport d'import est généré

## 🎨 Interface

- **Bootstrap 5**: Design moderne et responsive
- **Font Awesome 6**: Icônes pour les actions
- **Navigation**: Menu déroulant avec accès rapide
- **Alertes**: Messages de succès/erreur/warning
- **Pagination**: Navigation intuitive dans les listes

## ✅ Validation

- Validation des formulaires Django
- Gestion des erreurs MongoDB
- Messages de confirmation pour les suppressions
- Validation des données d'import CSV

## 🔒 Sécurité

- Protection CSRF activée
- Middleware de sécurité actif
- SECRET_KEY unique (à changer en production)

## 🐛 Dépannage

### MongoDB ne répond pas
```
Vérifiez que MongoDB est lancé:
- Windows: MongoDB Community Server doit tourner
- Linux: sudo service mongod start
```

### Port 8000 déjà utilisé
```bash
python manage.py runserver 8001
```

### Erreur de templates
```
Vérifiez que le dossier templates/ existe et contient les fichiers HTML
```

## 📋 Architecture

### Vues (Views)

Chaque module (catégories, produits, clients, commandes) dispose de:
- `liste_xxx()`: Affiche la liste avec pagination
- `creer_xxx()`: Crée un nouvel élément
- `modifier_xxx()`: Modifie un élément existant
- `supprimer_xxx()`: Supprime un élément
- `voir_xxx()`: Affiche les détails

### Modèles (Models)

Utilise MongoEngine pour mapper des classes Python aux collections MongoDB:
- `Categorie`
- `Produit`
- `Client`
- `Commande`
- `LigneCommande`

### Formulaires (Forms)

Django Forms avec validation et widgets Bootstrap:
- `CategorieForm`
- `ProduitForm`
- `ClientForm`
- `CommandeForm`
- `LigneCommandeForm`
- `ImportCSVForm`

## 📱 Responsive Design

- Mobile-first approach avec Bootstrap 5
- Navigation adaptative
- Tables responsives
- Formulaires optimisés pour mobile

## 💾 Développement Futur

Améliorations possibles:
- [ ] Authentification utilisateur
- [ ] Système de paiement
- [ ] Exports PDF des commandes
- [ ] Dashboard analytique avancé
- [ ] Gestion des stocks
- [ ] Notifications par email

## 📞 Support

Pour toute question ou problème:
1. Vérifiez que MongoDB est en fonctionnement
2. Relancez le serveur Django avec `python manage.py runserver`
3. Consultez les logs Django pour les détails d'erreur

---

**Créé avec ❤️ pour la gestion de Drive Alimentaire**

