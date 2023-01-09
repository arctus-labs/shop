window.onload = function() {
    const htmlTag = document.getElementsByTagName('html')[0]
    const themeTogglerIcon = document.getElementById('themeTogglerIcon');
    
    if (getCookie('theme') == 'light') {
        htmlTag.className = 'light';
        themeTogglerIcon.className = 'bi bi-sun';
    }
    
    if (getCookie('theme') == 'dark') {
        htmlTag.className = 'dark';
        themeTogglerIcon.className = 'bi bi-moon';
    }

    if (htmlTag.classList.contains('dark')) {
        setCookie('theme', 'dark');
    } else {
        setCookie('theme', 'light');
    }
}

function toggleTheme() {
    if (getCookie('theme') == 'dark') {
        setCookie('theme', 'light');
    } else {
        setCookie('theme', 'dark');
    }
    window.location.reload();
}