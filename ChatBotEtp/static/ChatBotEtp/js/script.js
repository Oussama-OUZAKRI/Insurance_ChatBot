function displayChatHome() {
    let chatPage = document.getElementById('Chat-Home');
    let homePage = document.getElementById('Home');
    chatPage.classList.add('open');
    homePage.style.transform = 'translateX(-100%)';
}

function displayHome() {
    let chatPage = document.getElementById('Chat-Home');
    let homePage = document.getElementById('Home');
    chatPage.classList.remove('open');
    homePage.style.transform = 'translateX(0)';
}

let messageCount = 0; // Variable pour garder une trace du nombre de messages affichés

function sendMessage() {
    let message = document.getElementById('input-message').value.trim();
    console.log(message);
    if (message) {
        // Afficher le message de l'utilisateur dans le chat
        displayMessage('user', message);
        // Effacer l'input
        document.getElementById('input-message').value = '';

        // Incrémenter le compteur de messages
        messageCount += 1;
        console.log(messageCount)

        // Afficher l'indicateur visuel d'attente
        displayMessage('bot', '', messageCount);

        fetch('process_message/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Afficher la réponse du serveur dans le chat et cacher l'indicateur visuel une fois la réponse reçue
            const loader = document.getElementById(`loader-${messageCount}`);
            const text = document.getElementById(`text-${messageCount}`);
            if (loader && text) {
                loader.style.display = 'none';
                text.innerText = data.response;
            } else {
                console.error('Error: Loader or text element not found');
            }
        })
        .catch(error => {
            console.error('Error:', error.error);
            const loader = document.getElementById(`loader-${messageCount}`);
            const text = document.getElementById(`text-${messageCount}`);
            if (loader && text) {
                loader.style.display = 'none';
                text.innerText = 'Error';
            } else {
                console.error('Error: Loader or text element not found');
            }
        });
    }
}

function displayMessage(sender, message, messageId) {
    const chatContainer = document.getElementById('Message-Container');
    const messageElement = document.createElement('div');
    messageElement.className = `message_${sender}`;
    
    const iconElement = document.createElement('span');
    iconElement.className = 'material-symbols-outlined';
    iconElement.innerText = sender === 'user' ? 'face' : 'smart_toy';
    messageElement.appendChild(iconElement);

    // Créer un identifiant unique pour chaque message
    const loaderId = `loader-${messageId}`;
    const textId = `text-${messageId}`;

    // Si c'est un message du bot, ajouter l'indicateur visuel et le texte "..."
    if (sender === 'bot') {
        const loader = document.createElement('div');
        loader.className = 'loader';
        loader.id = loaderId;
        messageElement.appendChild(loader);

        const textElement = document.createElement('span');
        textElement.id = textId;
        textElement.innerText = formatText(message);
        messageElement.appendChild(textElement);
    } else { // Si c'est un message de l'utilisateur
        const textElement = document.createElement('span');
        textElement.innerText = formatText(message);
        messageElement.appendChild(textElement);
    }

    chatContainer.appendChild(messageElement);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function formatText(text) {
    return text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
}

function getCsrfToken() {
    const tokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
    return tokenElement ? tokenElement.value : '';
}