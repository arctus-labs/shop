function toggleTheme() {
    if (getCookie('theme') == 'dark') {
        setCookie('theme', 'light');
    } else {
        setCookie('theme', 'dark');
    }
    window.location.reload();
}

window.onload = function() {
    document.getElementsByTagName('main')[0].setAttribute('id', 'main')
}
