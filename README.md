# Chatbot d'Assurance Législative avec OpenAI et ChromaDB

Ce projet implémente un chatbot spécialisé dans les questions législatives liées à l'assurance, en particulier les réglementations de l'ACAPS. Le chatbot utilise OpenAI pour la génération d'embeddings et les réponses, ainsi que ChromaDB pour stocker et interroger des sections similaires en fonction des questions de l'utilisateur.

## Fonctionnalités

- Génération d'embeddings à partir de texte avec OpenAI.
- Stockage et recherche de similarités avec ChromaDB.
- Chatbot capable de répondre à des questions liées aux lois et réglementations en assurance.
- Maintien de l'historique des conversations pour fournir des réponses contextuelles.
- Génération de réponses précises en se basant sur des articles législatifs et des références.

## Prérequis

- Python 3.x
- Clé API OpenAI
- Variables d'environnement pour la configuration des clés et services

## Créer un environnement virtuel et activer

-> python -m venv venv
-> source venv/bin/activate  # Sur Windows : venv\Scripts\activate

## Installer les dépendances

-> pip install -r requirements.txt

## Configurer les variables d'environnement

- OPENAI_API_KEY=your_openai_api_key (fichier Setting)

## insertion des données 

- python manage.py insert_data (changer le chemin vers output.json dans vectorDB.py)

## Démarrer le serveur Django

- python manage.py runserver
