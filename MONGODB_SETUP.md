# Configuration de MongoDB pour le Drive Alimentaire

## 📋 Vue d'ensemble

MongoDB est une base de données NoSQL utilisée par cette application. Ce guide vous aide à installer et configurer MongoDB localement.

## 🪟 Installation sur Windows

### Option 1 : Utiliser MongoDB Community Server (Recommandé)

#### Étape 1 : Télécharger l'installateur
1. Allez sur https://www.mongodb.com/try/download/community
2. Sélectionnez:
   - **Version**: La dernière version stable
   - **OS**: Windows
   - **Package**: msi
3. Cliquez sur "Download"

#### Étape 2 : Exécuter l'installateur
1. Double-cliquez sur le fichier .msi téléchargé
2. Acceptez les termes de licence
3. Choisissez le répertoire d'installation (par défaut: C:\Program Files\MongoDB\Server\[version])
4. Sélectionnez "Install MongoDB as a Service" (recommandé)
5. Cliquez sur "Install"

#### Étape 3 : Vérifier l'installation
```cmd
# Ouvrez une invite de commande et vérifiez
mongod --version
mongosh --version
```

### Option 2 : Utiliser MongoDB via Docker (Alternative)

Si vous avez Docker installé:

```bash
# Télécharger et exécuter MongoDB
docker run -d -p 27017:27017 --name mongodb mongo:latest

# Vérifier que ça fonctionne
docker logs mongodb
```

## 🐧 Installation sur Linux (Ubuntu/Debian)

```bash
# Importer la clé GPG
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -

# Ajouter le dépôt MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# Mettre à jour les paquets
sudo apt-get update

# Installer MongoDB
sudo apt-get install -y mongodb-org

# Démarrer le service
sudo systemctl start mongod

# Activer au démarrage
sudo systemctl enable mongod

# Vérifier le statut
sudo systemctl status mongod
```

## 🍎 Installation sur Mac

```bash
# Avec brew (recommandé)
brew tap mongodb/brew
brew install mongodb-community

# Démarrer le service
brew services start mongodb-community

# Vérifier le statut
brew services list
```

## 🚀 Démarrer MongoDB

### Windows (si installé en tant que service)

```cmd
# Démarrer le service
net start MongoDB

# Arrêter le service
net stop MongoDB

# Redémarrer le service
net stop MongoDB && net start MongoDB
```

### Windows (démarrage manuel)

```cmd
# Dans une invite de commande (cmd) ou PowerShell
mongod
```

Le serveur affichera quelque chose comme:
```
[initandlisten] waiting for connections on port 27017
```

### Linux/Mac

```bash
# Démarrer
sudo systemctl start mongod

# Arrêter
sudo systemctl stop mongod

# Redémarrer
sudo systemctl restart mongod

# Vérifier le statut
sudo systemctl status mongod
```

## ✅ Vérifier que MongoDB fonctionne

### Depuis le terminal

```bash
# Se connecter à MongoDB
mongosh

# Il devrait afficher:
# MongoDB shell version v7.0.0
# ...
# rs0 [direct: primary] >

# Quitter
exit
```

### Depuis une autre fenêtre/session

```bash
# Vérifier les ports en écoute
# Windows
netstat -an | find "27017"

# Linux
lsof -i :27017

# Mac
lsof -i :27017
```

## 🗄️ Vérifier les bases de données

Dans le shell MongoDB:

```javascript
// Lister les bases de données
show dbs

// Passer à drive_alimentaire
use drive_alimentaire

// Lister les collections
show collections

// Afficher les catégories
db.categories.find()

// Afficher les produits
db.produits.find()

// Afficher les clients
db.clients.find()

// Compter les documents
db.categories.countDocuments()
```

## 🔧 Configuration avancée

### Activer l'authentification

1. Créer un utilisateur administrateur
2. Redémarrer avec authentification

```javascript
// Dans le shell MongoDB sans authentification initialement
use admin

db.createUser({
    user: "admin",
    pwd: "password123",
    roles: ["root"]
})

// Alors redémarrer mongod avec --auth
// mongod --auth
```

### Configurer un fichier de configuration (Linux/Mac)

Créer `/etc/mongod.conf`:

```yaml
systemLog:
  destination: file
  path: /var/log/mongodb/mongod.log
storage:
  dbPath: /var/lib/mongodb
net:
  port: 27017
  bindIp: 127.0.0.1
```

Puis redémarrer:
```bash
sudo systemctl restart mongod
```

## 🔗 Connexion depuis Django

### Configuration dans config/settings.py

```python
from mongoengine import connect

# Connexion locale (par défaut)
connect(
    db='drive_alimentaire',
    host='localhost',
    port=27017,
    connect=False
)
```

### Connexion à un serveur distant

```python
connect(
    db='drive_alimentaire',
    host='votre-serveur.com',
    port=27017,
    username='user',
    password='password',
    connect=False
)
```

### Connexion à MongoDB Atlas (Cloud)

```python
connect(
    db='drive_alimentaire',
    host='mongodb+srv://user:password@cluster.mongodb.net/drive_alimentaire',
    connect=False
)
```

## 📊 Tools MongoDB

### MongoDB Compass (GUI)

Interface graphique pour MongoDB:
1. Téléchargez sur https://www.mongodb.com/products/compass
2. Connectez-vous à `mongodb://localhost:27017`
3. Explorez les données visuellement

### mongosh (Shell CLI moderne)

```bash
# Connexion
mongosh

# Afficher la version
mongosh --version
```

## 🐛 Dépannage

### Erreur : « Connection refused »

```
❌ MongoError: connect ECONNREFUSED 127.0.0.1:27017
```

**Solutions**:
1. Vérifiez que MongoDB est en cours d'exécution
2. Vérifiez le port (par défaut 27017)
3. Vérifiez l'adresse du serveur

### Erreur : « Already in use »

```
❌ Port 27017 is already in use
```

**Solutions**:
1. Arrêtez l'instance précédente: `net stop MongoDB`
2. Utilisez un autre port: `mongod --port 27018`
3. Trouvez le processus: `lsof -i :27017`

### La base de données n'existe pas

```
❌ drive_alimentaire not found
```

**Solution**: La base de données est créée automatiquement lorsque vous y insérez des documents. Exécutez:
```bash
python initialize_db.py
```

### Performances lentes

**Optimisations**:
- Ajouter des index
- Limiter les requêtes
- Utiliser la pagination
- Archiver les données anciennes

```javascript
// Ajouter un index
db.produits.createIndex({ "nom": 1 })

// Lister les index
db.produits.getIndexes()
```

## 📈 Intégrité des données

### Sauvegarde

```bash
# Sauvegarde complète
mongodump --db drive_alimentaire --out ./backup

# Restauration
mongorestore ./backup
```

### Validation

Vérifier l'intégrité des données:

```javascript
use drive_alimentaire

// Vérifier les références invalides
db.produits.find({ "categorie": null })

db.lignes_commande.find({ "produit": null })
```

## 🔐 Sécurité

### Recommandations

1. ✅ Utiliser l'authentification en production
2. ✅ Configurer les pare-feu
3. ✅ Utiliser SSL/TLS
4. ✅ Sauvegarder régulièrement
5. ✅ Utiliser des mots de passe forts
6. ✅ Limiter les accès

### Créer un utilisateur pour l'application

```javascript
use admin
db.createUser({
    user: "drive_app",
    pwd: "SecurePassword123!",
    roles: [
        { role: "readWrite", db: "drive_alimentaire" }
    ]
})
```

Puis en Django:
```python
connect(
    db='drive_alimentaire',
    username='drive_app',
    password='SecurePassword123!',
    host='localhost'
)
```

## 📞 Ressources Utiles

- **Documentation MongoDB**: https://docs.mongodb.com/
- **MongoDB Download**: https://www.mongodb.com/try/download/community
- **MongoDB University**: https://university.mongodb.com/
- **MongoEngine Docs**: http://mongoengine.org/

---

**Vous êtes prêt à utiliser MongoDB ! 🚀**


