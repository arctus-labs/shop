const passwordEle = document.getElementById('password');
const toggleButton = document.getElementById('showPassword');

function showPassword() {
    if (passwordEle.type === 'password') {
        passwordEle.type = 'text';

        toggleButton.classList.remove('bi-eye-slash');
        toggleButton.classList.add('bi-eye');
    }
}

function hidePassword() {
    if (passwordEle.type === 'text') {
        passwordEle.type = 'password';

        toggleButton.classList.remove('bi-eye');
        toggleButton.classList.add('bi-eye-slash');
    }
}

toggleButton.addEventListener('mousedown', showPassword);

toggleButton.addEventListener('mouseup', hidePassword);
toggleButton.addEventListener('mouseleave', hidePassword);
