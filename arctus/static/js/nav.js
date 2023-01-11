function openMobileNav() {
    const navPopup = document.getElementById('mobnav');
    const navIcon = document.getElementById('mobnav-icon');

    navPopup.classList.toggle('foldout');
    navIcon.classList.toggle('open');
    
    if (navPopup.classList.contains('foldout')) {
        navPopup.style.height = '100vh';
    } else {
        navPopup.style.height = '0';
    }
}

var lastScrollTop;

window.onscroll = function() {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    navbar = document.getElementById('header');

    if(scrollTop > lastScrollTop) {
        navbar.style.top = '-90px';
    } else{
        navbar.style.top='0';
    }

    lastScrollTop = scrollTop;
};
