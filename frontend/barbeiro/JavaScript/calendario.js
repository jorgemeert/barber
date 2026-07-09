const params = new URLSearchParams(window.location.search);
const idBarbeiro = params.get("id");
const horario = document.getElementById("horario");
horario.href = `horarios.html?id=${idBarbeiro}`;

const hoje = new Date();
const anoAtual = hoje.getFullYear();
const mesAtual = hoje.getMonth() + 1;

document.addEventListener("DOMContentLoaded", () => {
  fetch(`https://barber-w2d9.onrender.com/mostrarAgendamentos/${idBarbeiro}`)
    .then((response) => response.json())
    .then((agendamentos) => {
      if (agendamentos.mensagem) {
        gerarCalendario(anoAtual, mesAtual, []);
      } else {
        gerarCalendario(anoAtual, mesAtual, agendamentos);
      }
    });
});

function gerarCalendario(ano, mes, agendamentos) {
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
    </div>
  `;

  let celulas = "";

  for (let i = 0; i < primeiroDia; i++) {
    celulas += `<div class="cal-celula vazia"></div>`;
  }

  for (let d = 1; d <= diasNoMes; d++) {
    const diaStr = `${ano}-${String(mes).padStart(2, "0")}-${String(d).padStart(2, "0")}`;
    const agendamentosDoDia = agendamentos.filter((a) => a.dia === diaStr);

    let conteudo = "";
    agendamentosDoDia.forEach((a) => {
      conteudo += `
        <div class="agendamento-item">
          <span>${a.horario}</span>
          <button onclick="cancelar(${a.id})">Cancelar</button>
        </div>
      `;
    });

    celulas += `
      <div class="cal-celula ${agendamentosDoDia.length > 0 ? "tem-agendamento" : ""}">
        ${String(d).padStart(2, "0")}
        ${conteudo}
      </div>
    `;
  }

  document.querySelector(".cal-grid").innerHTML += celulas;

  document.getElementById("mesAnterior").addEventListener("click", () => {
    let novoMes = mes - 1;
    let novoAno = ano;
    if (novoMes === 0) {
      novoMes = 12;
      novoAno = ano - 1;
    }
    gerarCalendario(novoAno, novoMes, agendamentos);
  });

  document.getElementById("mesSeguinte").addEventListener("click", () => {
    let novoMes = mes + 1;
    let novoAno = ano;
    if (novoMes === 13) {
      novoMes = 1;
      novoAno = ano + 1;
    }
    gerarCalendario(novoAno, novoMes, agendamentos);
  });
}

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
        location.reload();
      }
    });
    modal.classList.remove("modalVisivel");
    modal.classList.add("modalEscondido");
  });

  btnNao.addEventListener("click", () => {
    modal.classList.remove("modalVisivel");
    modal.classList.add("modalEscondido");
  });
}
