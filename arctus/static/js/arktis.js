var htmlTag = document.getElementsByTagName('html')[0]
var themeTogglerIcon = document.getElementById('themeTogglerIcon');

// if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
//     htmlTag.className = 'dark';
//     themeTogglerIcon.className = 'bi bi-moon';
// } else {
//     htmlTag.className = 'light';
//     themeTogglerIcon.className = 'bi bi-sun';
// }

if (getCookie('theme') == 'light') {
    htmlTag.className = 'light';
    themeTogglerIcon.className = 'bi bi-sun';
}

if (getCookie('theme') == 'dark') {
    htmlTag.className = 'dark';
    themeTogglerIcon.className = 'bi bi-moon';
}



if (htmlTag.contains('dark')) {
    setCookie('theme', 'dark');
} else {
    setCookie('theme', 'light');
}

function toggleTheme() {
    if (getCookie('theme') == 'dark') {
        setCookie('theme', 'light');
    } else {
        setCookie('theme', 'dark');
    }
    window.location.reload();
}