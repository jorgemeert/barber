const params = new URLSearchParams(window.location.search);
const idBarbeiro = params.get("id");
const horariosAgendados = document.getElementById("horariosAgendados");
const horario = document.getElementById("horario");
horario.href = `horarios.html?id=${idBarbeiro}`;

document.addEventListener("DOMContentLoaded", () => {
  fetch(`http://127.0.0.1:5000/mostrarAgendamentos/${idBarbeiro}`)
    .then((response) => response.json())
    .then((servicos) => {
      servicos.forEach((servico) => {
        horariosAgendados.innerHTML += `
            <div>
                <p>dia: ${servico.dia}</p>
                <p>Hora: ${servico.horario}</p>
                <button onclick="cancelar(${servico.id})">Cancelar</button>
            </div>
        `;
      });
    });
});

function cancelar(id) {
  fetch(`http://127.0.0.1:5000/cancelarAgendamento/${id}`, {
    method: "DELETE",
  }).then((response) => {
    if (response.ok) {
      alert("Horário cancelado com sucesso");
    }
  });
}
