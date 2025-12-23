document.addEventListener("DOMContentLoaded", function () {

    function showRegister() {
        console.log("showRegister called");
        document.getElementById("login-form").classList.remove("active");
        document.getElementById("register-form").classList.add("active");
        console.log("Register form active:", document.getElementById("register-form").classList.contains("active"));
    }

    function showLogin() {
        console.log("showLogin called");
        document.getElementById("register-form").classList.remove("active");
        document.getElementById("login-form").classList.add("active");
        console.log("Login form active:", document.getElementById("login-form").classList.contains("active"));
    }

    // expose to HTML
    window.showRegister = showRegister;
    window.showLogin = showLogin;

    // ✅ READ FROM BODY (Django controls this)
    const activeForm = document.body.dataset.activeForm || "login";

    // Check if URL is /register/ and override
    const pathname = window.location.pathname.toLowerCase();
    if (pathname.includes('/register')) {
        console.log("URL is /register/, showing register form");
        showRegister();
    } else if (activeForm === "register") {
        showRegister();
    } else {
        showLogin();
    }
});
