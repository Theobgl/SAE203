#!/usr/bin/env python
"""
QUICK START - Drive Alimentaire
Démarrage rapide de l'application
"""

print("""
╔════════════════════════════════════════════════════════════════╗
║        🛒 DRIVE ALIMENTAIRE - QUICK START 🛒                  ║
║                                                                ║
║        Application de gestion complète d'un Drive              ║
║        pour produits alimentaires                              ║
╚════════════════════════════════════════════════════════════════╝
""")

import os
import sys
import subprocess
import time

def print_step(step, title, description=""):
    print(f"\n{'='*60}")
    print(f"📍 ÉTAPE {step}: {title}")
    print(f"{'='*60}")
    if description:
        print(f"   {description}\n")

def check_requirement(name, command):
    """Vérifier si un outil est installé"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout.strip()
    except:
        return False, ""

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Étape 1 : Vérifications
    print_step(1, "VÉRIFICATIONS PRÉALABLES", "Vérification des outils nécessaires")

    print("🔍 Vérification de Python...")
    python_ok, python_version = check_requirement(
        "Python",
        "python --version"
    )
    if python_ok:
        print(f"   ✅ Python installé: {python_version}")
    else:
        print("   ❌ Python n'est pas installé!")
        print("   📦 Téléchargez Python 3.10+ depuis python.org")
        sys.exit(1)

    print("\n🔍 Vérification de MongoDB...")
    mongodb_ok, _ = check_requirement("MongoDB", "mongod --version")
    if mongodb_ok:
        print("   ✅ MongoDB installé")
    else:
        print("   ⚠️  MongoDB n'est pas détecté")
        print("   📖 Consultez MONGODB_SETUP.md pour l'installation")
        print("   💡 Vous pouvez continuer et démarrer MongoDB plus tard")

    print("\n🔍 Vérification de pip...")
    pip_ok, _ = check_requirement("pip", "pip --version")
    if pip_ok:
        print("   ✅ pip installé")
    else:
        print("   ❌ pip n'est pas installé!")
        sys.exit(1)

    # Étape 2 : Installation des dépendances
    print_step(2, "INSTALLATION DES DÉPENDANCES",
               "Installation des bibliothèques Python nécessaires")

    try:
        print("📦 Installation en cours...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=False,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("   ✅ Dépendances installées avec succès")
        else:
            print("   ⚠️  Il y a eu des avertissements")
            print(result.stderr)
    except Exception as e:
        print(f"   ❌ Erreur lors de l'installation: {e}")
        sys.exit(1)

    # Étape 3 : Vérification Django
    print_step(3, "VÉRIFICATION DE LA CONFIGURATION DJANGO")

    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
        django.setup()

        result = subprocess.run(
            [sys.executable, "manage.py", "check"],
            check=False,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("   ✅ Configuration Django OK")
        else:
            print("   ❌ Erreur de configuration Django:")
            print(result.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        sys.exit(1)

    # Étape 4 : Préparation de MongoDB
    print_step(4, "PRÉPARATION MONGODB",
               "Vérification et initialisation de la connexion")

    print("⏳ Tentative de connexion à MongoDB (localhost:27017)...")

    # Vérifier si MongoDB fonctionne
    mongodb_running = False
    try:
        from mongoengine import connect
        connect(
            db='drive_alimentaire',
            host='localhost',
            port=27017,
            connect=False,
            serverSelectionTimeoutMS=5000
        )
        mongodb_running = True
        print("   ✅ Connexion MongoDB réussie!")
    except Exception as e:
        print(f"   ❌ Impossible de se connecter à MongoDB")
        print(f"      Erreur: {str(e)[:80]}")
        print("\n   📖 Pour démarrer MongoDB:")
        print("      Windows:  net start MongoDB")
        print("      Linux:    sudo systemctl start mongod")
        print("      Mac:      brew services start mongodb-community")
        mongodb_running = False

    # Étape 5 : Initialisation des données
    if mongodb_running:
        print_step(5, "INITIALISATION DES DONNÉES",
                   "Création des catégories, produits et clients par défaut")

        try:
            print("🔄 Initialisation de la base de données...")
            result = subprocess.run(
                [sys.executable, "initialize_db.py"],
                check=False,
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                print("   ✅ Base de données initialisée!")
                if "Catégories:" in result.stdout:
                    print(result.stdout)
            else:
                print("   ⚠️  Initialisation partielle ou données déjà existantes")

        except Exception as e:
            print(f"   ⚠️  Erreur lors de l'initialisation: {e}")
    else:
        print_step(5, "INITIALISATION DES DONNÉES",
                   "Ignorée - MongoDB n'est pas disponible")
        print("   💡 Vous pourrez initialiser les données plus tard après avoir démarré MongoDB")

    # Étape 6 : Affichage des instructions finales
    print_step(6, "PRÊT À DÉMARRER! 🚀",
               "Dernières étapes avant de lancer l'application")

    print("""
    Vous avez trois options:
    
    1️⃣  DÉMARRER IMMÉDIATEMENT
        python manage.py runserver
        
        Puis ouvrez: http://localhost:8000
    
    2️⃣  DÉMARRER SUR UN AUTRE PORT
        python manage.py runserver 8001
        
        Puis ouvrez: http://localhost:8001
    
    3️⃣  DÉMARRER AVEC CONFIGURATION RÉSEAU
        python manage.py runserver 0.0.0.0:8000
        
        Puis ouvrez: http://localhost:8000
    
    ═══════════════════════════════════════════════════════════════
    
    📋 PREMIÈRE VISITE:
       1. Accédez à http://localhost:8000
       2. Cliquez sur "Initialiser les données"
       3. Explorez les différentes sections
    
    📤 POUR TESTER L'IMPORT CSV:
       1. Allez à Produits → Importer CSV
       2. Téléchargez sample_import.csv
       3. Vérifiez les résultats
    
    📖 DOCUMENTATION:
       • README_COMPLET.md     - Documentation complète
       • GUIDE_DEMARRAGE.md    - Guide détaillé de démarrage
       • MONGODB_SETUP.md      - Configuration MongoDB
    
    ═══════════════════════════════════════════════════════════════
    """)

    # Section finale
    print("\n" + "="*60)
    if mongodb_running:
        print("✅ TOUT EST PRÊT! L'application peut démarrer!")
    else:
        print("⚠️  MongoDB n'est pas actif")
        print("   Veuillez le démarrer avant de lancer l'application")

    print("="*60)
    print("\n🎉 Bonne utilisation de Drive Alimentaire!\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Arrêt par l'utilisateur")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

