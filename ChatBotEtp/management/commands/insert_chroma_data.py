from django.core.management.base import BaseCommand
from ChatBotEtp.vectorDB import get_chroma_collection, insert_data_once

class Command(BaseCommand):
    help = 'Insère les données dans ChromaDB via LangChain une seule fois'

    def handle(self, *args, **kwargs):
        collection = get_chroma_collection()  # Récupérer la collection Chroma via LangChain
        insert_data_once(collection)  # Insérer les données dans Chroma via LangChain
        self.stdout.write(self.style.SUCCESS('Données insérées dans ChromaDB via LangChain.'))
