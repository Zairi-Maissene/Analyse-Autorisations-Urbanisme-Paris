import requests
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# L'URL du point de terminaison
# On peut utiliser cet clé pour le demo: 355d72e094f15ea7af9561b56203a78fd558c9327e9e9e1bd291924c
url = f"https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/dossiers-recents-durbanisme@parisdata/exports/csv?apikey={os.getenv('API_KEY')}"

# Envoyer une requête GET à l'URL
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Définir le nom du fichier où le contenu sera enregistré
    filename = "autorisations_durbanisme.csv"

    # Ouvrir le fichier en mode écriture-binaire et écrire le contenu
    with open(filename, "wb") as file:
        print(response.content[:100])
        file.write(response.content)
    print(f"Fichier enregistré sous le nom {filename}")
else:
    print(f"Échec de la récupération des données. Code de statut : {response.status_code}")
