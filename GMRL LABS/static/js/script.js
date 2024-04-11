// ----------------------------
// navbar scrolling top sticky 
// ----------------------------
// window.addEventListener('scroll', function () {
//     const navbar = document.getElementById('navbar', 'nav_contain');
//     if (window.scrollY > 50) { // Adjust the value as needed
//         navbar.classList.add('sticky');
//         nav_contain.style.width = '100vw';

//     } else {
//         navbar.classList.remove('sticky');
//         nav_contain.style.width = '88vw';

//     }
// });
window.addEventListener('scroll', function () {
    const navbar = document.getElementById('navbar', 'nav_contain');
    if (window.scrollY > 50) { // Adjust the value as needed
        navbar.classList.add('sticky');
        nav_contain.style.width = '100vw';

    } else {
        navbar.classList.remove('sticky');
        nav_contain.style.width = '88vw';
    }
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

// Include the CSRF token in your AJAX request headers
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
