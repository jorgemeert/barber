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

btnLogin.addEventListener("click", () => {
  numero = document.getElementById("numero_login").value;
  senha = document.getElementById("senha_login").value;

  fetch("http://127.0.0.1:5000/loginBarbeiro", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      telefone: numero,
      senha: senha,
    }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        alert("Telefone ou senha incorretos!");
      }
    })
    .then((dados) => {
      window.location.href = `calendario.html?id=${dados.id}`;
    });
});

btnRegistrar.addEventListener("click", () => {
  nome = document.getElementById("nome_registro").value;
  nome_barbearia = document.getElementById("nome_barbearia").value;
  telefone = document.getElementById("telefone").value;
  senha = document.getElementById("senha_registro").value;
  localizacao = document.getElementById("localizacao").value;
  foto = document.getElementById("foto").value;

  fetch("http://127.0.0.1:5000/cadastroBarbeiro", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nome: nome,
      nome_barbearia: nome_barbearia,
      senha: senha,
      localizacao: localizacao,
      telefone: telefone,
      foto: foto,
    }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        alert("Tente novamente!");
      }
    })
    .then((dados) => {
      if (dados && dados.id) {
        window.location.href = `config.html?id=${dados.id}`;
      }
    });
});
