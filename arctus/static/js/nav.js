function openMobileNav() {
    const navPopup = document.getElementById("mobnav");
    const navIcon = document.getElementById("mobnav-icon");

    navPopup.classList.toggle("foldout");
    navIcon.classList.toggle("open");

    if (navPopup.classList.contains("foldout")) {
        navPopup.style.height = "100vh";
    } else {
        navPopup.style.height = "0";
    }
}

$(window).on('scroll',function(){
    if($(window).scrollTop()){
        $('#header').addClass('short');
    }
    else{
        $('#header').removeClass('short');
    }
})
