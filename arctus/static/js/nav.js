function openMobileNav() {
    const nav = document.getElementById('mobnav');
    const navIcon = document.getElementById('mobnav-icon');

    nav.classList.toggle('foldout');
    navIcon.classList.toggle('open');
    
    if (nav.classList.contains('foldout')) {
        nav.style.height = '100vh';
    } else {
        nav.style.height = '0';
    }
}

// window.onscroll = function() {
//     const nav = document.getElementById('mobnav');
//     var currentScrollPos = window.pageYOffset;
  
//     if (currentScrollPos > 20) {
//         nav.style.transform = "translateY(-100%)";
//     } else {
//         nav.style.display = "initial";
//     }
//   }