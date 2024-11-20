from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from openai import OpenAI
from .vectorDB import get_chroma_collection 
import json

# Initialisation des embeddings et de Chroma via LangChain
collection = get_chroma_collection()

def index(request):
    return render(request, 'ChatBotEtp/index.html')

# Returns embeddings for a text.
def get_embeddings(text):
    # Get the API key from environment variables
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-large"
    )
    return response.data[0].embedding

# Query ChromaDB for similar sections
def get_similar_sections_chromadb(user_embedding, k=10):
    # Perform the query
    try:
        # Assuming 'collection' is the ChromaDB collection object
        results = collection.similarity_search_by_vector(embedding=user_embedding, k=k)
        print(f"Results: {results}") 
        # Assuming results have keys 'documents' and 'distances'
        sections = []
        for doc in results :
            section = doc.page_content + f"\n[{doc.metadata}]\n\n"
            sections += [section]
        return sections
    except AttributeError as e:
        print(f"ChromaDB method error: {e}")
        return []

# Global conversation history
conversation_history = []
MAX_HISTORY_LENGTH = 5  # Maximum messages in history

def process_message(request):
    global conversation_history

    if request.method == 'POST':
        data = json.loads(request.body)
        message_content = data.get('message')
        api_key = settings.OPENAI_API_KEY
        client = OpenAI(api_key=api_key)

        conversation_history.append({"role": "user", "content": message_content})

        user_embedding = get_embeddings(message_content)
        # Query ChromaDB for the most similar sections
        similar_sections = get_similar_sections_chromadb(user_embedding)

        # Flatten the list of similar sections if necessary
        context = " ".join(similar_sections)

        print(f"Context: {context}")

        if len(conversation_history) > MAX_HISTORY_LENGTH:
            conversation_history = conversation_history[-MAX_HISTORY_LENGTH:]

        prompt = (
            "Vous êtes un assistant virtuel spécialisé dans les questions législatives concernant l'assurance, en particulier les réglementations de l'ACAPS. "
            "Votre rôle est de répondre de manière précise uniquement aux questions liées aux lois, règlements, et aspects juridiques dans le domaine de l'assurance. "
            "Chaque réponse doit nécessaisserent inclure le numéro d'article pertinent, le cas échéant. "
            "En plus, tu dois donner la référence en bas de la réponse."
            "Ne répondez pas aux questions en dehors du domaine de l'assurance, telles que la science, les mathématiques ou d'autres sujets non pertinents. "
            "Soyez concis, précis, et fournissez des références légales si nécessaire."
            "Si la question ne concerne pas l'assurance ou la législation, indiquez poliment que la question est hors de votre champ de compétence."
            "\nVoici la conversation jusqu'à présent :\n"
        )

        for msg in conversation_history:
            prompt += f"{msg['role'].capitalize()} : {msg['content']}\n"

        prompt += (
            f"\nContexte : {context}\n(NB : Ne faites pas réfèrence au contexte dans votre réponse)\n\n"
            f"Question actuelle: {message_content}\n\n"
            "Réponse : "
            "[Référence : ]"
        )
        print(prompt)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content

        conversation_history.append({"role": "assistant", "content": answer})

        return JsonResponse({'response': answer})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
