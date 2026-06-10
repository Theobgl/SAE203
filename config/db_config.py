"""
Configuration de basculement entre MongoDB et SQLite
Permet à l'application de fonctionner avec MongoDB ou SQLite
"""

import os
import django
from django.conf import settings

# Déterminer quelle DB est active
USING_MONGODB = settings.MONGODB_ENABLED
USING_SQLITE = not USING_MONGODB

def get_db_type():
    """Retourne le type de DB actuellement utilisée"""
    return "MongoDB" if USING_MONGODB else "SQLite"

def get_db_info():
    """Retourne les informations de connexion à la DB"""
    if USING_MONGODB:
        return {
            'type': 'MongoDB',
            'host': 'localhost',
            'port': 27017,
            'database': 'drive_alimentaire',
            'status': '✅ Connecté'
        }
    else:
        db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        return {
            'type': 'SQLite',
            'path': db_path,
            'database': 'db.sqlite3',
            'status': '✅ Tableau de bord local'
        }

def print_db_status():
    """Affiche le statut de la DB"""
    info = get_db_info()
    print(f"\n{'='*60}")
    print(f"📊 Base de Données: {info['type']}")
    print(f"    Statut: {info['status']}")
    if 'path' in info:
        print(f"    Chemin: {info['path']}")
    else:
        print(f"    Host: {info['host']}:{info['port']}")
        print(f"    Base: {info['database']}")
    print(f"{'='*60}\n")

# Afficher le statut au démarrage
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings':
    print_db_status()

