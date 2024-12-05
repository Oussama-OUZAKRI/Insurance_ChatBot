# Chatbot d'Assurance Législative avec OpenAI et ChromaDB  

Ce projet implémente un **chatbot spécialisé** dans les questions législatives liées à l'assurance, en particulier les réglementations de l'**ACAPS**.  
Il utilise **OpenAI** pour la génération d'embeddings et les réponses, ainsi que **ChromaDB** pour le stockage et l'interrogation des sections pertinentes en fonction des questions de l'utilisateur.  

## 🌟 Fonctionnalités  

- **Génération d'embeddings** : Utilise OpenAI pour convertir le texte en représentations vectorielles.  
- **Recherche intelligente** : Stocke et interroge des sections législatives similaires avec ChromaDB.  
- **Réponses contextualisées** : Maintient un historique des conversations pour fournir des réponses pertinentes.  
- **Précision** : Génère des réponses basées sur des articles législatifs et des références fiables.  
- **Support législatif spécialisé** : Répond aux questions relatives aux lois et réglementations en assurance.  

---

## 🛠️ Prérequis  

- **Python 3.x**  
- **Clé API OpenAI**  
- **Variables d'environnement** : Nécessaires pour configurer les clés et services.  

---

## ⚙️ Installation  

### 1. Créer et activer un environnement virtuel  
Créez et activez un environnement virtuel avec la commande suivante :  
```bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows  
```

### 2. Installer les dépendances  
Installez les bibliothèques nécessaires avec :  
```bash
pip install -r requirements.txt
```

### 3. Configurer les variables d'environnement
Ajoutez votre clé API OpenAI dans un fichier de configuration :
```bash
OPENAI_API_KEY=your_openai_api_key
```

### 4. Insérer les données législatives
Ajoutez les données dans la base ChromaDB en exécutant :
```bash
python manage.py insert_data
```
**Remarque** : Si nécessaire, modifiez le chemin vers output.json dans vectorDB.py

### 5. Démarrer le serveur Django
Lancez le serveur pour commencer à utiliser le chatbot :
```bash
python manage.py runserver
```  

---

## 🧰 Outils et Technologies  

- **OpenAI** : Pour la génération d'embeddings et les réponses basées sur l'IA.  
- **ChromaDB** : Pour le stockage et la recherche de similarités.  
- **Django** : Framework backend pour gérer le serveur et les opérations de base.  

---

## 🎯 Objectif  

Faciliter l'accès aux réglementations législatives dans le domaine de l'assurance en répondant rapidement et avec précision aux questions des utilisateurs.  

---

## 📚 Ressources utiles  

- [Documentation OpenAI](https://platform.openai.com/docs/)  
- [Documentation ChromaDB](https://www.trychroma.com/docs)  
- [Documentation Django](https://docs.djangoproject.com/)  

---

## 💡 Contributions  

Les contributions sont les bienvenues ! Si vous avez des suggestions ou souhaitez signaler un problème, ouvrez une **issue** ou soumettez une **pull request**.  
