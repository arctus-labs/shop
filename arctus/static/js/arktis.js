function toggleTheme() {
    if (getCookie('theme') == 'dark') {
        setCookie('theme', 'light');
    } else {
        setCookie('theme', 'dark');
    }
    window.location.reload();
}