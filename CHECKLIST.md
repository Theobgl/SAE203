# ✅ Checklist - Drive Alimentaire

Utilisez cette checklist pour vous assurer que tout fonctionne correctement.

## 🔧 Configuration Initiale

### Environnement Python
- [ ] Python 3.10+ installé
- [ ] Virtual environment activé
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Django configuré (`python manage.py check` - OK)

### MongoDB
- [ ] MongoDB Community Server installé
- [ ] Service MongoDB en cours d'exécution
- [ ] Port 27017 écouté
- [ ] Connexion de test réussie (`mongosh`)

### Structure du Projet
- [ ] Dossier `app/` avec les modèles, vues, formulaires
- [ ] Dossier `config/` avec les paramètres Django
- [ ] Dossier `templates/` avec les fichiers HTML
- [ ] Fichier `manage.py` présent
- [ ] Fichier `requirements.txt` complet

## 🚀 Démarrage de l'Application

### Préparation
- [ ] MongoDB démarré et fonctionnel
- [ ] Virtual environment activé
- [ ] Aucun autre processus sur le port 8000

### Initialisation
- [ ] Exécuter: `python initialize_db.py`
- [ ] Catégories créées (3)
- [ ] Produits créés (4+)
- [ ] Clients créés (3)

### Serveur Django
- [ ] Exécuter: `python manage.py runserver`
- [ ] Message: "Starting development server at http://127.0.0.1:8000/"
- [ ] Aucune erreur de template
- [ ] Aucune erreur de base de données

## 🌐 Interface Web

### Page d'Accueil (/)
- [ ] Page charge sans erreur
- [ ] Cartes de statistiques affichées
- [ ] Bouton "Initialiser les données" présent
- [ ] Menu de navigation visible

### Gestion des Catégories (/categories/)
- [ ] Liste s'affiche
- [ ] Bouton "Ajouter" fonctionne
- [ ] Formulaire de création valide
- [ ] Création réussie → redirect vers liste
- [ ] Recherche fonctionne
- [ ] Pagination fonctionne (si >10 items)
- [ ] Bouton "Voir" affiche les détails
- [ ] Bouton "Modifier" fonctionne
- [ ] Bouton "Supprimer" demande confirmation

### Gestion des Produits (/produits/)
- [ ] Liste avec produits affichée
- [ ] Recherche par nom fonctionne
- [ ] Recherche par marque fonctionne
- [ ] Création de produit valide
- [ ] Catégorie sélectionnée correctement
- [ ] Détails du produit affichent prix et marque
- [ ] Modification de produit réussie
- [ ] Suppression avec confirmation fonctionne

### Gestion des Clients (/clients/)
- [ ] Liste des clients affichée
- [ ] Création de client avec numéro auto-incrémenté
- [ ] Recherche par nom/prénom fonctionne
- [ ] Détails client montre les commandes
- [ ] Modification de client réussie
- [ ] Suppression de client fonctionne

### Gestion des Commandes (/commandes/)
- [ ] Liste des commandes affichée
- [ ] Page de création avec sélection client
- [ ] Sélection de produits et quantités possible
- [ ] Calcul du total réussit
- [ ] Total s'affiche correctement
- [ ] Détails commande montre toutes les lignes
- [ ] Ajout de ligne à commande fonctionne
- [ ] Suppression de ligne réussit

### Import CSV (/importer/)
- [ ] Page d'import s'affiche
- [ ] Upload de fichier fonctionne
- [ ] Format sample_import.csv accepté
- [ ] Catégories créées automatiquement
- [ ] Produits importés correctement
- [ ] Rapport d'import affiché
- [ ] Aucune erreur lors de l'import
- [ ] Données visibles dans la liste des produits

## 💾 Base de Données

### Vérification MongoDB
```bash
mongosh
use drive_alimentaire
show collections
```

- [ ] Collection `categories` existe
- [ ] Collection `produits` existe
- [ ] Collection `clients` existe
- [ ] Collection `commandes` existe
- [ ] Collection `lignes_commande` existe

### Données

```javascript
db.categories.countDocuments()
```
- [ ] ≥ 3 catégories
- [ ] Chaque catégorie a un nom unique

```javascript
db.produits.countDocuments()
```
- [ ] ≥ 4 produits initiaux
- [ ] Chaque produit référence une catégorie
- [ ] Chaque produit a prix > 0

```javascript
db.clients.countDocuments()
```
- [ ] ≥ 3 clients
- [ ] Chaque client a un numéro unique
- [ ] Chaque client a nom et prénom

## 🔒 Sécurité

### CSRF Protection
- [ ] Formulaires contiennent `{% csrf_token %}`
- [ ] POST requests travaillent sans erreur CSRF
- [ ] Modifications conservées après POST

### Messages de Feedback
- [ ] Messages de succès verts affichés
- [ ] Messages d'erreur rouges affichés
- [ ] Messages d'avertissement jaunes affichés
- [ ] Bouton fermer sur les alertes fonctionne

### Validation
- [ ] Champs obligatoires validés
- [ ] Prix doit être positif
- [ ] Quantité doit être ≥ 1
- [ ] Messages d'erreur clairs

## 🎨 Interface Utilisateur

### Bootstrap 5
- [ ] Bootstrap CSS chargé (pas de styling cassé)
- [ ] Navigation responsive fonctionne
- [ ] Menu déroulant fonctionne
- [ ] Boutons bien formatés
- [ ] Tableaux bien formatés

### Icons Font Awesome
- [ ] Icônes s'affichent correctement
- [ ] Navigation a des icônes (home, tags, box, etc.)

### Responsive Design
- [ ] Site accessible sur mobile (Chrome dev tools)
- [ ] Menu s'effondre sur petit écran
- [ ] Tableaux scrollables sur petit écran
- [ ] Formulaires readables sur petit écran

## 📱 Fonctionnalités Avancées

### Recherche et Pagination
- [ ] Recherche filtre les résultats
- [ ] Pagination navigue correctement
- [ ] URL params ?page=X fonctionne
- [ ] Recherche + pagination ensemble OK

### Auto-increment ID
- [ ] Chaque commande a numéro_commande unique
- [ ] Chaque client a numero_client unique
- [ ] Nombres s'incrémentent automatiquement

### Calculs Automatiques
- [ ] Total ligne = prix × quantité
- [ ] Total commande = somme des lignes
- [ ] Totaux recalculés après modification

## 📊 Rapports et Statistics

### Dashboard
- [ ] Nombre de catégories correct
- [ ] Nombre de produits correct
- [ ] Nombre de clients correct
- [ ] Nombre de commandes correct

### Historique Client
- [ ] Les commandes sont linkées au client
- [ ] Voir client montre ses commandes
- [ ] Supprimer client: gestion correcte

## 🐛 Dépannage

Si quelque chose ne fonctionne pas:

### ❌ "Connection refused"
- [ ] Vérifier MongoDB est en cours
- [ ] Vérifier port 27017
- [ ] Vérifier configuration settings.py

### ❌ "TemplateDoesNotExist"
- [ ] Vérifier dossier templates/ existe
- [ ] Vérifier fichiers .html sont présents
- [ ] Vérifier chemin dans settings.py

### ❌ "Schema validation"
- [ ] Vérifier MongoEngine models
- [ ] Vérifier types des champs
- [ ] Vérifier champs required

### ❌ "CSRF verification failed"
- [ ] Vérifier {% csrf_token %} dans form
- [ ] Vérifier middleware CSRF actif
- [ ] Rafraîchir page et réessayer

## ✨ Optimisations (Optionnel)

- [ ] Ajouter index MongoDB pour recherche
- [ ] Cacher les static files (CSS/JS)
- [ ] Compresser images produits
- [ ] Ajouter pagination plus paramétrable
- [ ] Ajouter export PDF commandes

## 📝 Documentation

- [ ] README_COMPLET.md lu
- [ ] GUIDE_DEMARRAGE.md compris
- [ ] MONGODB_SETUP.md consulté si besoin
- [ ] Commentaires dans le code clairs

## 🎉 État Final

- [ ] Tout fonctionne correctement
- [ ] Aucune erreur console
- [ ] Aucune erreur serveur
- [ ] Interface utilisable
- [ ] Données persistées

---

## 📞 Si des problèmes restent

1. Vérifiez mongoDb est en cours
2. Relancez le serveur Django
3. Nettoiez le cache du navigateur
4. Vérifiez les logs Django
5. Consultez les fichiers de documentation

---

**Checklist complétée le: ____________________**

**Statut: ☐ En cours | ☐ Complétée | ☐ Avec problèmes**


