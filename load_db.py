import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les variables d'environnement
csv_file_path = os.getenv('CSV_FILE_PATH')
mysql_host = os.getenv('MYSQL_HOST')
mysql_database = os.getenv('MYSQL_DATABASE')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')

# Lire le fichier CSV
df = pd.read_csv(csv_file_path, on_bad_lines='warn', sep=';')

# Remplacer les valeurs NaN par None
df = df.where(pd.notnull(df), None)

# Se connecter à la base de données MySQL
try:
    connection = mysql.connector.connect(
        host=mysql_host,
        database=mysql_database,
        user=mysql_user,
        password=mysql_password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Créer la table si elle n'existe pas
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS dossiers (
            nom_dossier VARCHAR(255) PRIMARY KEY,
            type_dossier VARCHAR(255),
            demandeur TEXT,
            objet TEXT,
            programme TEXT,
            adresse TEXT,
            date_depot DATE,
            date_decision DATE,
            libelle TEXT,
            type_decision VARCHAR(255),
            etat VARCHAR(255),
            circonscription VARCHAR(255),
            x FLOAT,
            y FLOAT
        );'''
        cursor.execute(create_table_query)

        # Insérer les données dans la table
        for index, row in df.iterrows():
            insert_query = """
            INSERT INTO dossiers (
                nom_dossier, type_dossier, demandeur, objet, programme,
                 adresse, date_depot, date_decision, libelle,
                type_decision, etat, circonscription, x,
                y
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            record = (
                row['nom_dossier'], row['type_dossier'], row['demandeur'], row['objet'],
                row['programme'], row['adresse'], row['date_depot'],
                row['date_decision'], row['libelle'], row['type_decision'], row['etat'],
                row['circonscription'], row['x'], row['y']
            )
            cursor.execute(insert_query, record)
            connection.commit()

        print("Les données ont été insérées avec succès dans la table MySQL")

except Error as e:
    print(f"Erreur de connexion à MySQL : {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("La connexion MySQL est fermée")
