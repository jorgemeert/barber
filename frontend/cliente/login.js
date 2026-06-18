btnTrocaRegistro = document.getElementById("trocaRegistro");
btnTrocaLogin = document.getElementById("trocaLogin");
registroTrocaLogin = document.getElementById("registroTrocaLogin");
registroTrocaRegistro = document.getElementById("registroTrocaRegistro");
login = document.getElementById("login");
registro = document.getElementById("registro");
btnRegistrar = document.getElementById("btnRegistrar");
btnLogin = document.getElementById("btnLogin");

btnTrocaRegistro.addEventListener("click", () => {
  login.style.display = "none";
  registro.style.display = "block";
});

btnTrocaLogin.addEventListener("click", () => {
  registro.style.display = "none";
  login.style.display = "block";
});

registroTrocaRegistro.addEventListener("click", () => {
  login.style.display = "none";
  registro.style.display = "block";
});

registroTrocaLogin.addEventListener("click", () => {
  registro.style.display = "none";
  login.style.display = "block";
});

btnRegistrar.addEventListener("click", () => {
  numero = document.getElementById("numero_registro").value;
  nome = document.getElementById("nome_registro").value;
  senha = document.getElementById("senha_registro").value;

  fetch("http://127.0.0.1:5000/cadastro", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nome: nome,
      telefone: numero,
      senha: senha,
    }),
  });
});

btnLogin.addEventListener("click", () => {
  numero = document.getElementById("numero_login").value;
  senha = document.getElementById("senha_login").value;

  fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      telefone: numero,
      senha: senha,
    }),
  }).then((response) => {
    if (response.ok) {
      window.location.href = "barbearias.html";
    } else {
      alert("Telefone ou senha incorretos!");
    }
  });
});
