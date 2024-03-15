// ----------------------------
// navbar scrolling top sticky 
// ----------------------------
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
// end sticky navbar


