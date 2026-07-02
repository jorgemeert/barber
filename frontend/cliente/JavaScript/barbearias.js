const lista_barbearias = document.getElementById("lista_barbearias");
const btnPesquisa = document.getElementById("btnPesquisa");
const params = new URLSearchParams(window.location.search);
const idCliente = params.get("id");
const agendamentosAtivos = document.getElementById("agendamentoAtivos");
agendamentosAtivos.href = `agendamento-ativo.html?id=${idCliente}`;

document.addEventListener("DOMContentLoaded", () => {
  fetch("http://127.0.0.1:5000/barbearias")
    .then((response) => response.json())
    .then((dados) => {
      dados.forEach((barbearias) => {
        lista_barbearias.innerHTML += `
    <div id='${barbearias.id}'>
      <p>${barbearias.nome_barbearia}</p>
      <p>${barbearias.localizacao}</p>
      <img src="${barbearias.foto}" alt="imagem barbearia">
    </div>
  `;
        document.getElementById(barbearias.id).addEventListener("click", () => {
          window.location.href = `agendamentos.html?id=${idCliente}&id_barber=${barbearias.id}`;
        });
      });
    });
});

btnPesquisa.addEventListener("click", () => {
  nome_barbearia = document.getElementById("pesquisa").value;
  fetch("http://127.0.0.1:5000/pesquisarBarbearia", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nome_barbearia: nome_barbearia,
    }),
  })
    .then((response) => response.json())
    .then((dados) => {
      lista_barbearias.innerHTML = "";

      if (dados.mensagem) {
        lista_barbearias.innerHTML =
          "<p>Nenhuma barbearia foi encontrada com esse nome!</p>";
      } else {
        dados.forEach((barbearias) => {
          lista_barbearias.innerHTML += `
    <div id='${barbearias.id}'>
      <p>${barbearias.nome_barbearia}</p>
      <p>${barbearias.localizacao}</p>
    </div>
  `;
        });
      }
    });
});
