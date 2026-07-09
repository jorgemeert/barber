const params = new URLSearchParams(window.location.search);
const idBarberio = params.get("id_barber");
const idCliente = params.get("id");
const servicosBarbeiro = document.getElementById("servicos");
const btnAgendar = document.getElementById("btnAgendar");
const voltar = document.getElementById("voltar");
const selectHorario = document.getElementById("horario");

voltar.href = `barbearias.html?id=${idCliente}`;

document.addEventListener("DOMContentLoaded", () => {
  fetch(`https://barber-w2d9.onrender.com/servicos/${idBarberio}`)
    .then((response) => response.json())
    .then((servicos) => {
      servicos.forEach((servico) => {
        servicosBarbeiro.innerHTML += `
          <div>
            <input type="radio" name="servico" value="${servico.id}">
            <label>${servico.nome_servico} R$${servico.valor}</label>
          </div>
        `;
      });
    });
});

btnAgendar.addEventListener("click", () => {
  const data = document.getElementById("data").value;
  const horario = document.getElementById("horario").value;
  const servico = document.querySelector('input[name="servico"]:checked').value;
  const dataFormatada = data.split("-").reverse().join("/");
  fetch("https://barber-w2d9.onrender.com/agendarHorario", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      dia: dataFormatada,
      horario: horario,
      id_cliente: idCliente,
      id_barbeiro: idBarberio,
      id_servico: servico,
    }),
  }).then((response) => {
    if (response.ok) {
      window.location.href = `barbearias.html?id=${idCliente}`;
      alert("Seu agendamento foi um sucesso!");
    } else {
      alert("Ocorreu um erro no seu agendamento!");
    }
  });
});

for (let h = 7; h <= 21; h++) {
  selectHorario.innerHTML += `<option value="${String(h).padStart(2, "0")}:00">${String(h).padStart(2, "0")}:00</option>`;
  selectHorario.innerHTML += `<option value="${String(h).padStart(2, "0")}:30">${String(h).padStart(2, "0")}:30</option>`;
}
