# MGL7460 TP1

## Structure du projet

```
mgl7460-python/
├── mgl7460_tp1/                   # Package principal
│   ├── implementations/           # Implémentations concrètes
│   │   ├── modeles/
│   │   └── traitements/
│   └── types/                     # Définitions de types / interfaces
│       ├── modeles/
│       └── traitements/
├── tests/                         # Tests unitaires
└── requirements.txt               # Dépendances du projet
```

## Installation

1. **Cloner ou télécharger le projet**
   ```powershell
   cd mgl7460-python
   ```

2. **Créer un environnement virtuel**
   ```powershell
   python -m venv venv
   
   # Sur Windows :
   venv\Scripts\Activate.ps1
   
   # Sur macOS / Linux :
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```powershell
   pip install -r requirements.txt
   ```

## Exécution des tests

```powershell
# Installer pytest si nécessaire (déjà présent dans requirements.txt)
pip install pytest

# Lancer les tests
python -m pytest
```

## Développement

### Formatage du code
```powershell
python -m black mgl7460_tp1/
```

### Vérification des types
```powershell
python -m mypy mgl7460_tp1/
```
