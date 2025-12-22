document.addEventListener("DOMContentLoaded", function () {

    function showRegister() {
        document.getElementById("login-form").classList.remove("active");
        document.getElementById("register-form").classList.add("active");
    }

    function showLogin() {
        document.getElementById("register-form").classList.remove("active");
        document.getElementById("login-form").classList.add("active");
    }

    // expose functions to HTML
    window.showRegister = showRegister;
    window.showLogin = showLogin;

    // default view
    showLogin();
});
