const input = document.getElementById('password');
const regex_checks = [/(?=.*[A-Z].*[A-Z])/, /(?=.*[!?<>|@#$&*~-])/, /(?=.*[0-9].*[0-9])/, /(?=.*[a-z].*[a-z].*[a-z])/, /.{8}/]

function checkPassword() {
    var password = input.value;
    var validity = '';

    for (let checkNo in regex_checks) {
        check = regex_checks[checkNo];

        if (password.match(check)) {
            document.getElementById(`y${checkNo}`).style.display = "initial";
            document.getElementById(`n${checkNo}`).style.display = "none";
        } else {
            document.getElementById(`y${checkNo}`).style.display = "none";
            document.getElementById(`n${checkNo}`).style.display = "initial";
            validity = 'Password must contain at least 8 characters, 2 uppercase letters, 2 numbers, 3 lowercase letters and 1 special character';
        }
    }

    input.setCustomValidity(validity);
}

input.addEventListener('input', checkPassword);

checkPassword();
