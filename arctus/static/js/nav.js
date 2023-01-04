function openMobileNav() {
    var nav = document.getElementById('mobnav')
    nav.classList.toggle('foldout');

    if (nav.classList.contains('foldout')) {
        nav.style.height = '100vh';
    } else {
        nav.style.height = '0';
    }
}
