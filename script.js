//gestion de la connexion
document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "" || password === "") {
      alert("Veuillez remplir tous les champs !");
      return;
    }

    if (username === "user1" && password === "password123") {
      alert("Connexion réussie !");
      window.location.href = "dashboard.html";
    } else {
      alert("Nom d'utilisateur ou mot de passe incorrect !");
    }
  });

const togglePassword = document.getElementById("togglePassword");
const passwordField = document.getElementById("password");

//affichage du mot de passe
togglePassword.addEventListener("click", function () {
  if (passwordField.type === "password") {
    passwordField.type = "text";
    togglePassword.textContent = "🙈";
  } else {
    passwordField.type = "password";
    togglePassword.textContent = "👁️";
  }
});
