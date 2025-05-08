# Gestionnaire de Tâches API

Une API REST complète pour gérer vos tâches quotidiennes, développée avec Django et Django REST Framework.

## Fonctionnalités

- ✅ Gestion complète des tâches (création, lecture, mise à jour, suppression)
- 🔒 Authentification sécurisée avec JWT
- 📋 Catégorisation des tâches
- 🔍 Recherche et filtrage avancés
- 📊 Statistiques sur les tâches
- 📱 API RESTful compatible avec tout type de client (web, mobile, desktop)

## Prérequis

- Python 3.8+
- pip

## Installation

1. Clonez le dépôt
```bash
git clone https://github.com/henocn/Task-manager.git
cd Task-manager
```

2. Créez un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installez les dépendances
```bash
pip install -r requirements.txt
```

4. Appliquez les migrations
```bash
python manage.py migrate
```

5. Créez un superutilisateur
```bash
python manage.py createsuperuser
```

6. Lancez le serveur de développement
```bash
python manage.py runserver
```

## Structure de l'API

### Authentification

- `POST /api/token/` - Obtenir un token JWT
- `POST /api/token/rafraichir/` - Rafraîchir un token JWT
- `POST /api/token/verifier/` - Vérifier un token JWT

### Tâches

- `GET /api/taches/` - Liste des tâches
- `POST /api/taches/` - Créer une tâche
- `GET /api/taches/{id}/` - Détails d'une tâche
- `PUT /api/taches/{id}/` - Mettre à jour une tâche
- `DELETE /api/taches/{id}/` - Supprimer une tâche
- `POST /api/taches/{id}/terminer/` - Marquer une tâche comme terminée
- `POST /api/taches/{id}/annuler/` - Marquer une tâche comme annulée
- `GET /api/taches/en_retard/` - Liste des tâches en retard
- `GET /api/taches/par_statut/?status=todo` - Filtrer les tâches par statut

### Catégories

- `GET /api/categories/` - Liste des catégories
- `POST /api/categories/` - Créer une catégorie
- `GET /api/categories/{id}/` - Détails d'une catégorie
- `PUT /api/categories/{id}/` - Mettre à jour une catégorie
- `DELETE /api/categories/{id}/` - Supprimer une catégorie

### Utilisateurs

- `GET /api/mes-taches/` - Liste des tâches de l'utilisateur connecté
- `GET /api/mes-taches/statistiques/` - Statistiques sur les tâches de l'utilisateur

## Documentation

La documentation interactive de l'API est disponible aux endpoints suivants :

- Swagger UI: `/documentation/`
- ReDoc: `/redoc/`

## Modèles de données

### Tâche

- `title` - Titre de la tâche
- `description` - Description détaillée
- `created_at` - Date de création
- `updated_at` - Date de dernière modification
- `due_date` - Date d'échéance
- `status` - Statut (à faire, en cours, terminée, annulée)
- `priority` - Priorité (basse, normale, haute, urgente)
- `completed_at` - Date de complétion
- `owner` - Propriétaire de la tâche
- `category` - Catégorie de la tâche

### Catégorie

- `name` - Nom de la catégorie
- `description` - Description de la catégorie

## Déploiement

Pour un déploiement en production, veuillez suivre les recommandations de Django :
https://docs.djangoproject.com/en/5.1/howto/deployment/

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT.