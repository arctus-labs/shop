function openMobileNav() {
    let nav = document.getElementById('mobnav')
    let navIcon = document.getElementById('mobnav-icon')
    nav.classList.toggle('foldout');
    navIcon.classList.toggle('open');

    if (nav.classList.contains('foldout')) {
        nav.style.height = '100vh';
    } else {
        nav.style.height = '0';
    }
}
