btnTrocaRegistro = document.querySelector(".trocaRegistro");
btnTrocaLogin = document.querySelector(".trocaLogin");
login = document.getElementById("login");
registro = document.getElementById("registro");

btnTrocaRegistro.addEventListener("click", () => {
  login.style.display = "none";
  registro.style.display = "none";

  registro.style.display = "block";
});

btnTrocaLogin.addEventListener("click", () => {
  registro.style.display = "none";
  registro.style.display = "none";

  login.style.display = "block";
});
