const agendamentosAtivos = document.getElementById("agendamentosAtivos");
const params = new URLSearchParams(window.location.search);
const idCliente = params.get("id");
const voltar = document.getElementById("voltar");
voltar.href = `barbearias.html?id=${idCliente}`;

document.addEventListener("DOMContentLoaded", () => {
  fetch(`http://127.0.0.1:5000/agendamentosAtivos/${idCliente}`)
    .then((response) => response.json())
    .then((agendamentos_cliente) => {
      agendamentosAtivos.innerHTML += `
            <div>
                <p>dia: ${agendamentos_cliente.dia}</p>
                <p>horario: ${agendamentos_cliente.horario}</p>

            </div>

        `;
    });
});
