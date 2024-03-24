var menuToggle = document.getElementById('menu-toggle');
var header = document.querySelector('header');
var nameSite = document.querySelector('.nameSite');
const body = document.body;
var menuList1 = document.getElementById('mobile-items');
menuToggle.addEventListener('change', function() {
    if (menuToggle.checked) {
        body.style.overflow = 'hidden';
        menuList1.style.width = nameSite.offsetWidth + 4 + "px";
        console.log(menuList1.style.width);
    } else {
        header.style.position = 'relative';
        body.style.overflow = '';
    }
});




function navigateTo(url) {
    window.location.href = url;
}
var buttons = document.querySelectorAll('.btn4');
buttons.forEach(function (button) {
    button.addEventListener('click', function () {
        var link = this.querySelector('a');
        if (link && link.hasAttribute('href')) {
            var url = link.getAttribute('href');
            navigateTo(url);
        }
    });
});




var currentPath = window.location.pathname;
var buttons = document.querySelectorAll('.btn4');
buttons.forEach(function(button) {
    var link = button.querySelector('a');
    if (link && link.getAttribute('href') === currentPath.substring(0,1)){
        if (currentPath.charAt(1)==""){
            button.style.backgroundColor = '#15151b';
            button.style.scale = "1.1";
        }
    }
    else if ( link && link.getAttribute('href') === currentPath.substring(1)) {
        button.style.backgroundColor = '#15151b'; 
        button.style.scale = "1.1";
    }
});



const lib = document.querySelectorAll(".lib");
lib.forEach(lib => {
    const header = lib.querySelector(".lib_header");
    const description = lib.querySelector(".lib_description");
    header.addEventListener("click", () => {
        if (description.style.maxHeight === "0px" || description.style.maxHeight === "") {
            description.style.maxHeight = description.scrollHeight + "px";
        } 
        else {
            window.scrollTo(0, scrollY);
            description.style.maxHeight = "0";
        }
    });
});