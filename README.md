# Analyse Approfondie des Autorisations d'Urbanisme à Paris

Ce projet concerne l'analyse des autorisations d'urbanisme. Il comprend des scripts pour l'exportation des données, le chargement dans une base de données et un carnet de notes pour l'analyse.

## Structure du Projet

- `main.py` : Ce script exporte les données au format CSV. Il récupère les données depuis une API et les enregistre localement.

- `db.py` : Ce script charge les données du fichier CSV dans une base de données MySQL. Il crée la table nécessaire et insère les données.

- `index.ipynb` : Ce carnet Jupyter contient le travail d'analyse. Il inclut l'exploration des données, la visualisation et toute autre analyse effectuée sur le jeu de données.

## Comment Exécuter

1. **Configuration de l'Environnement** :
   ```bash
    cp .env.example .env
   ```
    Remplissez le fichier .env avec vos informations d'identification pour l'API et la base de données.
   (Il y a un clé commenté dans load_csv.py pour tester le script)
1. **Exporter les Données** : 
   Exécutez `load_csv.py` pour exporter les données de l'API vers un fichier CSV.

   ```bash
   python load_csv.py
    ```
2. **Charger les Données dans MySQL (optionel)** :
Assurez-vous d'avoir configuré votre fichier .env avec les informations d'identification de la base de données. Ensuite, exécutez db.py pour charger les données dans votre base de données MySQL.

```bash
python load_db.py
```
3. **Installer les Dépendances** :
Assurez-vous d'avoir installé les dépendances nécessaires pour exécuter le carnet Jupyter. Vous pouvez installer les dépendances en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

4. **Analyser les Données** :
Ouvrez index.ipynb dans Jupyter Notebook pour effectuer l'analyse des données et visualiser les résultats.

```bash
jupyter notebook index.ipynb
```