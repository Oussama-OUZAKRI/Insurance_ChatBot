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