var welcomeText = document.getElementById("welcomeText");
var greetings = ["Готовы к новому квесту?","Приготовьтесь к игровым открытиям.","У нас интересно, оставайтесь с нами!","Добро пожаловать в мир игр и консолей."];

var currentIndex = 0;

function displayAndErase(word) {
    var index = 0;
    var interval = setInterval(function () {
        welcomeText.textContent = word.substring(0, index);
        index++;
        if (index > word.length) {
            clearInterval(interval);
            setTimeout(function () {
                eraseWord();
            }, 4000);
        }
    }, 55); 
}

function eraseWord() {
    var index = welcomeText.textContent.length;
    var interval = setInterval(function () {
        welcomeText.textContent = welcomeText.textContent.substring(0, index);
        index--;
        if (index < 0) {
            clearInterval(interval);
            currentIndex = (currentIndex + 1) % greetings.length;
            setTimeout(function () {
                displayAndErase(greetings[currentIndex]);
            }, 0);
        }
    }, 25); 
}

displayAndErase(greetings[currentIndex]);
