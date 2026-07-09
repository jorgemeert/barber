const agendamentosAtivos = document.getElementById("agendamentosAtivos");
const params = new URLSearchParams(window.location.search);
const idCliente = params.get("id");
const voltar = document.getElementById("voltar");
voltar.href = `barbearias.html?id=${idCliente}`;

document.addEventListener("DOMContentLoaded", () => {
  fetch(`https://barber-w2d9.onrender.com/agendamentosAtivos/${idCliente}`)
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
    fetch(`https://barber-w2d9.onrender.com/cancelarAgendamento/${id}`, {
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

function gerarCalendario(data, idAgendamento, mesAgendamento, anoAgendamento) {
  const partes = data.split("-");
  const ano = parseInt(partes[0]);
  const mes = parseInt(partes[1]);
  const dia = parseInt(partes[2]);

  // Se não foram passados, usa os do mês atual (primeira chamada)
  if (!mesAgendamento) mesAgendamento = mes;
  if (!anoAgendamento) anoAgendamento = ano;

  const diasNoMes = new Date(ano, mes, 0).getDate();
  const primeiroDia = new Date(ano, mes - 1, 1).getDay();

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
  </div>`;

  let celulas = "";

  for (let i = 0; i < primeiroDia; i++) {
    celulas += `<div class="cal-celula vazia"></div>`;
  }

  for (let d = 1; d <= diasNoMes; d++) {
    const temAgendamento =
      d === dia && mes === mesAgendamento && ano === anoAgendamento;
    celulas += `<div class="cal-celula ${temAgendamento ? "agendado" : ""}">
    ${d}
    ${temAgendamento ? `<span>Agendado</span><button onclick="cancelar(${idAgendamento})">Cancelar</button>` : ""}
  </div>`;
  }

  document.querySelector(".cal-grid").innerHTML += celulas;

  document.getElementById("mesAnterior").addEventListener("click", () => {
    let novoMes = mes - 1;
    let novoAno = ano;
    if (novoMes === 0) {
      novoMes = 12;
      novoAno = ano - 1;
    }
    const novaData = `${novoAno}-${String(novoMes).padStart(2, "0")}-${String(dia).padStart(2, "0")}`;
    gerarCalendario(novaData, idAgendamento, mesAgendamento, anoAgendamento);
  });

  document.getElementById("mesSeguinte").addEventListener("click", () => {
    let novoMes = mes + 1;
    let novoAno = ano;
    if (novoMes === 13) {
      novoMes = 1;
      novoAno = ano + 1;
    }
    const novaData = `${novoAno}-${String(novoMes).padStart(2, "0")}-${String(dia).padStart(2, "0")}`;
    gerarCalendario(novaData, idAgendamento, mesAgendamento, anoAgendamento);
  });
}
