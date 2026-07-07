const agendamentosAtivos = document.getElementById("agendamentosAtivos");
const params = new URLSearchParams(window.location.search);
const idCliente = params.get("id");
const voltar = document.getElementById("voltar");
voltar.href = `barbearias.html?id=${idCliente}`;

document.addEventListener("DOMContentLoaded", () => {
  fetch(`http://127.0.0.1:5000/agendamentosAtivos/${idCliente}`)
    .then((response) => response.json())
    .then((agendamentos_cliente) => {
      if (agendamentos_cliente.mensagem) {
        agendamentosAtivos.innerHTML = "<h2>Você não possui agendamentos!</h2>";
      } else {
        gerarCalendario(agendamentos_cliente.dia, agendamentos_cliente.id);
      }
    });
});

function cancelar(id) {
  modal = document.getElementById("meuModal");
  modal.classList.remove("modalEscondido");
  modal.classList.add("modalVisivel");
  btnSim = document.getElementById("sim");
  btnNao = document.getElementById("nao");

  btnSim.addEventListener("click", () => {
    fetch(`http://127.0.0.1:5000/cancelarAgendamento/${id}`, {
      method: "DELETE",
    }).then((response) => {
      if (response.ok) {
        alert("Horário cancelado com sucesso");
      }
    });
    modal.classList.remove("modalVisivel");
    modal.classList.add("modaEscondido");
  });

  btnNao.addEventListener("click", () => {
    modal.classList.remove("modalVisivel");
    modal.classList.add("modalEscondido");
  });
}

// Calendário

const diasNoMes = new Date(ano, mes, 0).getDate();

function gerarCalendario(data, idAgendamento) {
  // separando data em ano, mes e dia
  const partes = data.split("-");
  const ano = parseInt(partes[0]);
  const mes = parseInt(partes[1]);
  const dia = parseInt(partes[2]);

  // Salvando data atual
  const diasNoMes = new Date(ano, mes, 0).getDate();
  const primeiroDia = new Date(ano, mes - 1, 1).getDay();

  // criando calendario

  const calendario = document.getElementById("calendario");

  calendario.innerHTML = `
  <div class="cal-header">
    <button id="mesAnterior">&#8249;</button>
    <span>${mes}/${ano}</span>
    <button id="mesSeguinte">&#8250;</button>
  </div>
  <div class="cal-grid">
    <div class="cal-dia-semana">D</div>
    <div class="cal-dia-semana">S</div>
    <div class="cal-dia-semana">T</div>
    <div class="cal-dia-semana">Q</div>
    <div class="cal-dia-semana">Q</div>
    <div class="cal-dia-semana">S</div>
    <div class="cal-dia-semana">S</div>
  </div>
`;
  let celulas = "";

  for (let i = 0; i < primeiroDia; i++) {
    celulas += `<div class="cal-celula vazia"></div>`;
  }

  for (let d = 1; d <= diasNoMes; d++) {
    const temAgendamento = d === dia;
    celulas += `<div class="cal-celula ${temAgendamento ? "agendado" : ""}">
    ${d}
    ${temAgendamento ? `<span>Agendado</span><button onclick="cancelar(${idAgendamento})">Cancelar</button>` : ""}
  </div>`;
  }
  document.querySelector(".cal-grid").innerHTML += celulas;
}
