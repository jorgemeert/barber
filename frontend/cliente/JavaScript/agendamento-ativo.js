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
        agendamentosAtivos.innerHTML = "<h2>Agendamento ativo</h2>";
        agendamentosAtivos.innerHTML += `
            <div>
                <p>dia: ${agendamentos_cliente.dia}</p>
                <p>horario: ${agendamentos_cliente.horario}</p>
                <button onclick="cancelar(${agendamentos_cliente.id})">Cancelar</button>
            </div>

        `;
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
