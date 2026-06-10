╔═══════════════════════════════════════════════════════════════════╗
║                   DRIVE ALIMENTAIRE                                 ║
║        Application Web de Gestion d'un Drive Alimentaire            ║
║                                                                     ║
║  ✅ 100% FONCTIONNELLE - PRÊTE À ÊTRE UTILISÉE                     ║
╚═══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 DÉMARRAGE RAPIDE (3 ÉTAPES)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  DÉMARRER MONGODB

    Windows:
    → Ouvrir Services Windows (services.msc)
    → Chercher "MongoDB"
    → Clic droit → Démarrer

    OU en PowerShell (admin):
    → net start MongoDB

    Linux:
    → sudo systemctl start mongod

    macOS:
    → brew services start mongodb-community

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2️⃣  INITIALISER LA BASE DE DONNÉES

    cd C:\Users\theob\PycharmProjects\SAE203
    python initialize_db.py

    Cela créera automatiquement:
    ✓ 3 catégories (Boissons, Fruits, Snacks)
    ✓ 4 produits
    ✓ 3 clients

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3️⃣  DÉMARRER L'APPLICATION

    python manage.py runserver

    Ouvrez votre navigateur:
    → http://localhost:8000

    🎉 Vous êtes prêt!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ QUESTIONS FRÉQUENTES

Q: Où est MongoDB?
A: Le télécharger sur https://www.mongodb.com/try/download/community

Q: Port 8000 occupé?
A: Utiliser: python manage.py runserver 8001

Q: Les données ne s'affichent pas?
A: Vérifier que MongoDB fonctionne et exécuter initialize_db.py

Q: Comment tester l'import CSV?
A: Aller à /importer/ et télécharger sample_import.csv

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 DOCUMENTATION

Fichiers à consulter:
├── README_COMPLET.md       → Vue d'ensemble complète
├── GUIDE_DEMARRAGE.md      → Guide étape par étape
├── MONGODB_SETUP.md        → Configuration MongoDB
├── CHECKLIST.md            → Vérification
└── INSTALLATION_COMPLETE.md → Synthèse d'installation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ FONCTIONNALITÉS

☑ Gestion des catégories
☑ Gestion des produits
☑ Gestion des clients
☑ Création de commandes
☑ Gestion des lignes de commande
☑ Import CSV en masse
☑ Recherche et pagination
☑ Interface Bootstrap 5
☑ Dashboard d'accueil
☑ Calcul automatique des totaux

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏗️ ARCHITECTURE

Modèles (MongoDB):
├── Categorie
├── Produit
├── Client
├── Commande
└── LigneCommande

Vues (Django):
├── Catégories (CRUD)
├── Produits (CRUD)
├── Clients (CRUD)
├── Commandes (CRUD)
├── Lignes (Ajout/Suppr)
└── Import CSV

Templates (Bootstrap 5):
├── Listes avec pagination
├── Formulaires
├── Détails
├── Confirmations
└── Dashboard

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 DONNÉES INITIALES

Catégories:
1. Boissons (Boissons fraîches et sodas)
2. Fruits (Fruits frais de saison)
3. Snacks (Snacks et gâteaux)

Produits:
1. Coca Cola 1L - 2.50€
2. Jus Orange 1L - 3.20€
3. Pommes Gala kg - 4.50€
4. Chips Salée 200g - 1.99€

Clients:
1. Jean Dupont - 12 rue des Fleurs
2. Claire Martin - 45 avenue Principale
3. Lucas Bernard - 78 route de Paris

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 VÉRIFICATION

Vérifier que tout fonctionne:

1. Accédez à http://localhost:8000
2. Les statistiques s'affichent
3. Cliquez sur "Catégories" → Liste affichée
4. Cliquez sur "Produits" → Liste affichée
5. Cliquez sur "Clients" → Liste affichée
6. Cliquez sur "Commandes" → Liste affichée
7. Créez une nouvelle commande
8. Testez l'import CSV

Si tout OK: ✅ Application prête!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚨 PROBLÈMES COURANTS

Problème: "Connection refused"
Solution: Démarrer MongoDB

Problème: "Port 8000 already in use"
Solution: python manage.py runserver 8001

Problème: "TemplateDoesNotExist"
Solution: Vérifier dossier templates/

Problème: "CSRF verification failed"
Solution: Rafraîchir la page, réessayer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💾 SAUVEGARDE MONGODB

Sauvegarder les données:
mongodump --db drive_alimentaire --out ./backup

Restaurer les données:
mongorestore ./backup

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 BESOIN D'AIDE?

1. Vérifiez MongoDB est lancé
2. Consultez les fichiers README_*.md
3. Relancez le serveur Django
4. Nettoyez le cache navigateur
5. Vérifiez les logs Django

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ L'APPLICATION EST 100% FONCTIONNELLE

Version: 1.0.0
Date: 2026-06-10
Statut: ✅ PRÊT À UTILISER

Bonne chance avec Drive Alimentaire! 🛒✨

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

