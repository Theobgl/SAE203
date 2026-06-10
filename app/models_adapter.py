"""
Adaptateur de modèles - Bascule automatique MongoDB ↔ SQLite
Importe les bons modèles selon la base disponible
"""

import os
import sys
from django.conf import settings

# Déterminer la DB active
USING_MONGODB = settings.MONGODB_ENABLED

if USING_MONGODB:
    # Importer les modèles MongoEngine
    from app.models import (
        Categorie,
        Produit,
        Client,
        Commande,
        LigneCommande
    )
    print("📊 Modèles MongoDB importés")
else:
    # Importer les modèles Django SQLite
    from app.models_sqlite import (
        Categorie,
        Produit,
        Client,
        Commande,
        LigneCommande
    )
    print("📊 Modèles SQLite importés")

__all__ = [
    'Categorie',
    'Produit',
    'Client',
    'Commande',
    'LigneCommande'
]

