const params = new URLSearchParams(window.location.search);
const idBarbeiro = params.get("id");
const horariosAgendados = document.getElementById("horariosAgendados");
const horario = document.getElementById("horario");
horario.href = `horarios.html?id=${idBarbeiro}`;

document.addEventListener("DOMContentLoaded", () => {
  fetch(`http://127.0.0.1:5000/mostrarAgendamentos/${idBarbeiro}`)
    .then((response) => response.json())
    .then((servicos) => {
      if (servicos.mensagem) {
        horariosAgendados.innerHTML = "<h2>Você não possui agendamentos</h2>";
      } else {
        horariosAgendados.innerHTML = "<h2>Seu horários agendados!</h2>";
        servicos.forEach((servico) => {
          horariosAgendados.innerHTML += `
            <div>
                <p>dia: ${servico.dia}</p>
                <p>Hora: ${servico.horario}</p>
                <button onclick="cancelar(${servico.id})">Cancelar</button>
            </div>
        `;
        });
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
