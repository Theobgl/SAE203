# 🔄 MODE HYBRIDE - MongoDB + SQLite

## 📋 Vue d'ensemble

L'application **Drive Alimentaire** supporte maintenant un **mode hybride** qui permet de fonctionner avec:

- ✅ **MongoDB** - Mode production (base NoSQL performante)
- ✅ **SQLite** - Mode développement (fallback automatique)

---

## 🎯 Fonctionnement

### Démarrage automatique

1. **MongoDB disponible?**
   - ✅ OUI → Utilise MongoDB (performance optimale)
   - ❌ NON → Bascule automatiquement à SQLite

2. **Au lancement:**
   ```
   ⚠️  MongoDB indisponible: connection refused
   💡 Utilisation de SQLite pour développement...
   ✅ SQLite activé comme fallback!
   ```

### Changement de DB en temps réel

Pas besoin de reconfiguration! L'application détecte automatiquement:

```
🚀 Démarrage
  ↓
MongoDB accessible?
  ├─ OUI  → MongoDB activé
  └─ NON  → SQLite activé
  ↓
Application prête ✅
```

---

## 🚀 UTILISATION

### Avec MongoDB (production)

**Démarrer MongoDB:**
```bash
# Windows
net start MongoDB

# Linux
sudo systemctl start mongod

# Mac
brew services start mongodb-community
```

**Initialiser:**
```bash
python initialize_hybrid.py
```

**Démarrer app:**
```bash
python manage.py runserver
```

**Résultat:**
```
✅ MongoDB connected successfully!
📊 Base de Données: MongoDB
    Statut: ✅ Connecté
    Host: localhost:27017
    Base: drive_alimentaire
```

### Avec SQLite (développement)

**Pas besoin de MongoDB!** Démarrez directement:

```bash
python initialize_hybrid.py
```

**Résultat:**
```
⚠️  MongoDB indisponible
💡 Utilisation de SQLite pour développement...
✅ SQLite activé comme fallback!
📊 Base de Données: SQLite
    Statut: ✅ Tableau de bord local
    Chemin: C:\Users\theob\PycharmProjects\SAE203\db.sqlite3
```

---

## 📊 ARCHITECTURE

### Importer dans les vues

**Avant (MongoDB uniquement):**
```python
from app.models import Categorie, Produit, ...
```

**Maintenant (Automatique):**
L'adapter bascule automatiquement!
```python
from app.models_adapter import Categorie, Produit, ...
# OU directement (l'app détermine la DB)
from app.models import Categorie, Produit, ...
```

### Structures de données

**MongoDB:** MongoEngine Documents
```python
# app/models.py
class Categorie(Document):
    nom = StringField(required=True, unique=True)
    ...
```

**SQLite:** Django Models
```python
# app/models_sqlite.py
class Categorie(models.Model):
    nom = models.CharField(max_length=200, unique=True)
    ...
```

### Adapter

L'adapter (`app/models_adapter.py`) importe automatiquement les bons modèles:
```python
if USING_MONGODB:
    # Utiliser MongoEngine
    from app.models import Categorie, ...
else:
    # Utiliser SQLite
    from app.models_sqlite import Categorie, ...
```

---

## 💾 DONNÉES

### MongoDB
- Collections séparées
- Structure NoSQL flexible
- Relations par ObjectId

### SQLite
- Tables SQL classiques
- Relations par ForeignKey
- Migrations Django automatiques

### Commandes d'initialisation

```bash
# Initialisation automatique (teste MongoDB d'abord)
python initialize_hybrid.py

# Force SQLite
# (arrêtez MongoDB ou commentez dans settings.py)
python initialize_hybrid.py

# Force MongoDB
# (démarrez MongoDB, puis)
python initialize_hybrid.py
```

---

## 🔧 CONFIGURATION

### Vérifier la DB active

**En Python:**
```python
from django.conf import settings

if settings.MONGODB_ENABLED:
    print("MongoDB")
else:
    print("SQLite")
```

**Via script:**
```python
from config.db_config import get_db_info

info = get_db_info()
print(info['type'])  # MongoDB ou SQLite
```

### Forcer une DB

**Dans `config/settings.py`**, modifier la section MongoDB:

```python
# Force SQLite (désactiver MongoDB)
MONGODB_ENABLED = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Force MongoDB (MongoDB doit être disponible)
MONGODB_ENABLED = True
try:
    connect(...)
except:
    # Erreur si MongoDB pas disponible
    pass
```

---

## ✅ STATUT DE LA DB

### Afficher le statut

```bash
# Automatiquement au démarrage
python manage.py check

# Ou
python initialize_hybrid.py
```

Affiche:
```
60
📊 Base de Données: SQLite (ou MongoDB)
    Statut: ✅ Connecté (ou Tableau de bord local)
    ...
```

---

## 📱 DONNÉES INITIALES

### Automatiquement créées

- **3 catégories**: Boissons, Fruits, Snacks
- **4 produits**: Coca Cola, Jus Orange, Pommes, Chips
- **3 clients**: Jean Dupont, Claire Martin, Lucas Bernard

Créées dans:
- MongoDB (collections)
- SQLite (tables)

---

## 🐛 TROUBLESHOOTING

### "MongoDB connection refused"
```
✅ Normal! L'app bascule à SQLite
    python initialize_hybrid.py
```

### "SQLite database locked"
```
❌ Arrêtez l'autre processus Django
    puis relancez
```

### "AttributeError: DatabaseWrapper"
```
✅ Erreur normale au démarrage
    L'app adapte automatiquement
```

### SQLite ne se crée pas
```
✅ Exécutez:
    python initialize_hybrid.py
    python manage.py migrate
```

---

## 🚀 MIGRATION MONGODB → SQLITE (ou vice-versa)

### De MongoDB à SQLite

1. **Arrêtez MongoDB**
2. **Exécutez:**
   ```bash
   python initialize_hybrid.py
   python manage.py runserver
   ```
3. **L'app bascule automatiquement!**

### De SQLite à MongoDB

1. **Démarrez MongoDB**
   ```bash
   net start MongoDB
   ```
2. **Exécutez:**
   ```bash
   python initialize_hybrid.py
   python manage.py runserver
   ```
3. **L'app détecte MongoDB et bascule!**

---

## 📊 PERFORMANCES

### MongoDB (Production)
- ✅ Performant pour grandes données
- ✅ Scalabilité NoSQL
- ✅ Flexible (vrai NoSQL)

### SQLite (Développement)
- ✅ Léger et autonome
- ✅ Pas de serveur externe
- ✅ Parfait pour dev/testing
- ⚠️ Limité pour multi-users

---

## 📝 FICHIERS CONCERNÉS

- **`config/settings.py`** - Configuration hybride
- **`config/db_config.py`** - Infos DB (NOUVEAU)
- **`app/models.py`** - MongoEngine
- **`app/models_sqlite.py`** - Django SQLite (NOUVEAU)
- **`app/models_adapter.py`** - Adapter (NOUVEAU)
- **`initialize_hybrid.py`** - Initialisation (NOUVEAU)

---

## 🎓 RÉSUMÉ

| Aspect | MongoDB | SQLite |
|--------|---------|--------|
| **Mode** | Production | Développement |
| **Démarrage** | `net start MongoDB` | Aucun |
| **Prérequis** | Serveur MongoDB | Fichier local |
| **Scalabilité** | Excellente | Basique |
| **Type** | NoSQL | SQL relationnel |
| **Initialisation** | `python initialize_hybrid.py` | `python initialize_hybrid.py` |

---

**L'application bascule automatiquement! 🚀**

Commencez par:
```bash
python initialize_hybrid.py
python manage.py runserver
```

Puis ouvrez: **http://localhost:8000**


