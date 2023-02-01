const passwordEle = document.getElementById('password');
const toggleButton = document.getElementById('showPassword');

function togglePassword() {
    if (passwordEle.type === 'password') {
        passwordEle.type = 'text';
        toggleButton.classList.remove('bi-eye-slash');
        toggleButton.classList.add('bi-eye');

    } else {
        passwordEle.type = 'password';
        toggleButton.classList.remove('bi-eye');
        toggleButton.classList.add('bi-eye-slash');

    }
}

// now add an event listener which toggles the password input on or off
toggleButton.addEventListener('click', togglePassword);

//toggleButton.addEventListener('mousedown', showPassword);

//toggleButton.addEventListener('mouseup', hidePassword);
//toggleButton.addEventListener('mouseleave', hidePassword);
