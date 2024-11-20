from langchain_chroma import Chroma 
from langchain_openai import OpenAIEmbeddings 
from langchain_core.documents import Document
from django.conf import settings
import json

# Utilisation des embeddings OpenAI avec LangChain
embedding_function = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY, model="text-embedding-3-large")

# Initialisation de ChromaDB via LangChain
def get_chroma_collection():
    # Vous pouvez utiliser un répertoire pour stocker la base de données localement (par ex. "./chroma_db")
    persist_directory = "./chroma_db"
    collection = Chroma(collection_name="VectorDB", embedding_function=embedding_function, persist_directory=persist_directory)
    return collection

# Fonction pour insérer les données une seule fois dans Chroma via LangChain
def insert_data_once(collection):
    json_file_path = "C:/Users/Oussama Ouzakri/Desktop/Chatbot Entreprise/ChatBot/output.json"  # Chemin vers le fichier output.json contenant les données

    # Charger les données depuis le fichier JSON
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Boucle pour insérer chaque texte et son embedding
    Docs = []
    for item in data:
        doc = Document(
            page_content=item['text'],
            metadata={"source": item.get('source', 'unknown')}
        )
        Docs.append(doc)

    # Insérer les textes dans Chroma
    collection.add_documents(Docs)
    print("Données insérées et persistées dans ChromaDB via LangChain.")
