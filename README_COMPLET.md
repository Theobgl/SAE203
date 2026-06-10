# 🛒 Drive Alimentaire - Application Complète de Gestion

Une application web moderne et complète de gestion d'un Drive alimentaire, permettant de gérer les catégories, produits, clients et commandes.

## ✨ Caractéristiques Principales

✅ **CRUD Complets** pour toutes les entités
✅ **Interface Bootstrap 5** moderne et responsive
✅ **Recherche et Pagination** sur les listes
✅ **Import CSV** de produits avec création automatique de catégories
✅ **Gestion des commandes** avec lignes multiples
✅ **Calcul automatique** des totaux
✅ **MongoDB NoSQL** pour la base de données
✅ **Validation des formulaires** avec messages de feedback
✅ **Dashboard** avec statistiques rapides

## 🛠️ Technologies Utilisées

- **Backend**: Python 3.14 + Django 4.2
- **Base de données**: MongoDB (NoSQL)
- **ORM MongoDB**: MongoEngine 0.27
- **Frontend**: Bootstrap 5 + HTML5/CSS3
- **Formulaires**: Django Forms avec validation

## 📦 Installation

### Prérequis

- Python 3.10+
- MongoDB Community Server
- pip (gestionnaire de paquets Python)

### Étape 1 : Cloner/Accéder au projet

```bash
cd C:\Users\theob\PycharmProjects\SAE203
```

### Étape 2 : Activer l'environnement virtuel (si nécessaire)

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Étape 3 : Installer les dépendances

```bash
pip install -r requirements.txt
```

### Étape 4 : Démarrer MongoDB

#### Windows (MongoDB Community Server)

```bash
# Méthode 1 : Si MongoDB est installé comme service
net start MongoDB

# Méthode 2 : Lancer manuellement
"C:\Program Files\MongoDB\Server\7.0\bin\mongod.exe"
```

#### Linux
```bash
sudo systemctl start mongod
```

#### Mac
```bash
brew services start mongodb-community
```

### Étape 5 : Vérifier la configuration Django

```bash
python manage.py check
```

Vous devriez voir: `System check identified no issues (0 silenced).`

### Étape 6 : Initialiser la base de données

```bash
python initialize_db.py
```

Cela créera:
- 3 catégories (Boissons, Fruits, Snacks)
- 4 produits de démonstration
- 3 clients de démonstration

### Étape 7 : Démarrer le serveur Django

```bash
python manage.py runserver
```

Ou sur un port différent:
```bash
python manage.py runserver 8001
```

### Étape 8 : Accéder à l'application

Ouvrez votre navigateur et allez à:

```
http://localhost:8000
```

## 🗂️ Structure du Projet

```
SAE203/
│
├── app/                              # Application principale Django
│   ├── models.py                     # Modèles MongoEngine
│   │   ├── Categorie
│   │   ├── Produit
│   │   ├── Client
│   │   ├── Commande
│   │   └── LigneCommande
│   ├── views.py                      # Vues Django (CRUD, import)
│   ├── forms.py                      # Formulaires Django
│   ├── urls.py                       # Routes URL de l'app
│   ├── apps.py                       # Configuration de l'app
│   └── __init__.py
│
├── config/                           # Configuration Django
│   ├── settings.py                   # Paramètres globaux
│   ├── urls.py                       # URLs principales
│   ├── wsgi.py                       # Interface WSGI
│   └── __init__.py
│
├── templates/                        # Templates HTML
│   ├── base.html                     # Template de base
│   ├── accueil.html                  # Page d'accueil
│   ├── importer_produits.html        # Import CSV
│   │
│   ├── categories/                   # Templates catégories
│   │   ├── liste.html
│   │   ├── form.html
│   │   ├── detail.html
│   │   └── confirmer_suppression.html
│   │
│   ├── produits/                     # Templates produits
│   │   ├── liste.html
│   │   ├── form.html
│   │   ├── detail.html
│   │   └── confirmer_suppression.html
│   │
│   ├── clients/                      # Templates clients
│   │   ├── liste.html
│   │   ├── form.html
│   │   ├── detail.html
│   │   └── confirmer_suppression.html
│   │
│   └── commandes/                    # Templates commandes
│       ├── liste.html
│       ├── creer.html
│       ├── form.html
│       ├── detail.html
│       ├── ajouter_ligne.html
│       ├── confirmer_suppression.html
│       └── confirmer_suppression_ligne.html
│
├── initialize_db.py                  # Script d'initialisation MongoDB
├── manage.py                         # Utilitaire Django
├── requirements.txt                  # Dépendances Python
│
└── README.md                         # Ce fichier
```

## 📊 Collections MongoDB

### 1. **categories**
```json
{
    "_id": ObjectId,
    "nom": "Boissons",
    "descriptif": "Boissons fraîches et sodas"
}
```

### 2. **produits**
```json
{
    "_id": ObjectId,
    "nom": "Coca Cola 1L",
    "prix": 2.50,
    "marque": "Coca Cola",
    "date_peremption": "2026-12-31",
    "photo": "coca.jpg",
    "categorie": ObjectId,
    "date_creation": "2026-06-10T12:00:00"
}
```

### 3. **clients**
```json
{
    "_id": ObjectId,
    "numero_client": 1,
    "nom": "Dupont",
    "prenom": "Jean",
    "date_inscription": "2026-01-10",
    "adresse": "12 rue des Fleurs"
}
```

### 4. **commandes**
```json
{
    "_id": ObjectId,
    "numero_commande": 1,
    "client_id": ObjectId,
    "date_commande": "2026-06-10T14:30:00"
}
```

### 5. **lignes_commande**
```json
{
    "_id": ObjectId,
    "commande_id": ObjectId,
    "produit_id": ObjectId,
    "quantite": 3
}
```

## 🚀 Utilisation

### Page d'Accueil
- Vue globale avec statistiques
- Bouton pour initialiser les données
- Raccourcis rapides vers les principales actions

### Gestion des Catégories
- **Liste**: Affichage de toutes les catégories avec recherche
- **Créer**: Formulaire pour ajouter une nouvelle catégorie
- **Modifier**: Édition d'une catégorie existante
- **Supprimer**: Suppression avec confirmation
- **Voir détails**: Liste des produits de la catégorie

### Gestion des Produits
- **Liste**: Tableau avec pagination et recherche
- **Créer**: Ajout d'un produit avec catégorie, prix, marque
- **Modifier**: Édition des données du produit
- **Supprimer**: Suppression avec confirmation
- **Voir détails**: Information complète du produit

### Gestion des Clients
- **Liste**: Clients avec pagination et recherche
- **Créer**: Formulaire avec nom, prénom, adresse, date
- **Modifier**: Édition des informations client
- **Supprimer**: Suppression avec confirmation
- **Voir détails**: Historique des commandes du client

### Gestion des Commandes
- **Liste**: Commandes avec pagination
- **Créer**: Assistant de création avec:
  - Sélection du client
  - Sélection de plusieurs produits
  - Saisie des quantités
  - Création automatique de la commande et des lignes
- **Voir détails**: 
  - Informations de la commande
  - Liste des produits commandés
  - Calcul automatique du total
- **Ajouter des lignes**: Ajout de produits à une commande existante
- **Supprimer des lignes**: Suppression de produits de la commande

### Import CSV
1. Accédez à la page "Importer CSV"
2. Sélectionnez un fichier au format: `nom;prix;marque;date_peremption;categorie`
3. Les catégories inexistantes sont créées automatiquement
4. Les produits sont importés en masse
5. Rapport d'import avec erreurs affichées

Format attendu:
```csv
nom;prix;marque;date_peremption;categorie
Coca Cola 1L;2.50;Coca Cola;2026-12-31;Boissons
Jus Orange;3.20;Tropicana;2026-10-15;Boissons
Pommes;3.00;Bio;2026-06-20;Fruits
```

## 📱 Interface Utilisateur

### Navigation
- **Menu principal**: Liens vers toutes les sections
- **Dropdowns**: Sous-menus avec actions rapides
- **Recherche**: Barre de recherche sur les pages principales
- **Pagination**: Navigation dans les listes de 10 éléments

### Formulaires
- **Auto-complétion**: Sélection de catégories et clients
- **Validation**: Messages d'erreur en temps réel
- **Bootstrap classes**: Mise en forme automatique
- **Placeholders**: Indices visuels pour remplissage

### Tableaux
- **Données**: Affichage clair et organisé
- **Actions**: Boutons Ajouter, Modifier, Supprimer, Voir
- **Pagination**: Navigation par pages
- **Recherche**: Filtrage des résultats

## 🔍 Recherche et Pagination

### Pagination
- **Par défaut**: 10 éléments par page
- **Navigation**: Boutons Précédent/Suivant
- **URLs**: Paramètre `?page=X`

### Recherche
- **Catégories**: Recherche par nom
- **Produits**: Recherche par nom ou marque
- **Clients**: Recherche par nom ou prénom

## ⚙️ Configuration

### Connexion MongoDB

Modifiez `config/settings.py` pour changer la connexion:

```python
# Local (par défaut)
connect(
    db='drive_alimentaire',
    host='localhost',
    port=27017,
    connect=False
)

# Distant (exemple)
connect(
    db='drive_alimentaire',
    host='mongodb.example.com',
    port=27017,
    username='user',
    password='password',
    connect=False
)
```

### Langue et Fuseau horaire

`config/settings.py`:
```python
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'Europe/Paris'
```

### Port du serveur

```bash
# Défaut: 8000
python manage.py runserver

# Autre port
python manage.py runserver 8001

# Tous les IPs du réseau
python manage.py runserver 0.0.0.0:8000
```

## 🐛 Dépannage

### MongoDB n'est pas accessible
```
❌ Socket error: Connection refused
✅ Solution: Démarrez MongoDB avant l'application
   Windows: net start MongoDB
   Linux: sudo systemctl start mongod
```

### Port 8000 déjà utilisé
```bash
# Utiliser un autre port
python manage.py runserver 8001
```

### Erreur de template
```
❌ TemplateDoesNotExist
✅ Vérifiez que le dossier templates/ existe et contient les fichiers
```

### Erreur CSRF
```
❌ CSRF verification failed
✅ Assurez-vous que le formulaire inclut {% csrf_token %}
```

### Données non affichées
```
✅ Vérifiez:
  - MongoDB est en cours d'exécution
  - Les données sont créées (python initialize_db.py)
  - Pas d'erreurs dans les logs Django
```

## 📋 Commandes Utiles

```bash
# Vérifier la configuration
python manage.py check

# Lancer le serveur
python manage.py runserver

# Initialiser les données
python initialize_db.py

# Accéder à MongoDB en ligne de commande
mongo

db.drive_alimentaire
db.categories.find()
db.produits.find()
```

## 📈 Améliorations Futures

- [ ] Authentification et permissions
- [ ] Système de paiement intégré
- [ ] Exports PDF des commandes
- [ ] Dashboard analytique avancé
- [ ] Gestion des stocks et alertes
- [ ] Notifications par email
- [ ] Support multi-devises
- [ ] API REST avec Django REST Framework
- [ ] Tests unitaires et intégration
- [ ] Docker pour déploiement

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à:
1. Reporter des bugs
2. Proposer des améliorations
3. Soumettre des pull requests

## 📝 Licence

Projet créé à titre éducatif.

## 📞 Support

Pour toute question ou problème:
1. Consultez le fichier GUIDE_DEMARRAGE.md
2. Vérifiez les logs de l'application
3. Assurez-vous que MongoDB fonctionne correctement

---

**Créé avec ❤️ pour la gestion de Drive Alimentaire**

### Version
- **Version**: 1.0.0
- **Date**: 2026-06-10
- **Statut**: ✅ Prêt pour production (après ajustements de sécurité)

### À faire avant production
- [ ] Changer SECRET_KEY dans settings.py
- [ ] Configurer un serveur SMTP pour les emails
- [ ] Ajouter l'authentification utilisateur
- [ ] Configurer HTTPS/SSL
- [ ] Optimiser les requêtes MongoDB
- [ ] Ajouter des sauvegardes régulières
- [ ] Mettre en place un monitoring

---

**Bonne utilisation! 🚀**

