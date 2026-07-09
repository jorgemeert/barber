const params = new URLSearchParams(window.location.search);
const idBarbeiro = params.get("id");
const btnBloqueio = document.getElementById("btnBloquear");
const voltar = document.getElementById("voltar");
voltar.href = `calendario.html?id=${idBarbeiro}`;

document.addEventListener("DOMContentLoaded", () => {
  const selectHorario = document.getElementById("horaBloqueio");
  selectHorario.innerHTML = '<option value="">Dia inteiro</option>';

  for (let h = 7; h <= 21; h++) {
    selectHorario.innerHTML += `<option value="${String(h).padStart(2, "0")}:00">${String(h).padStart(2, "0")}:00</option>`;
    selectHorario.innerHTML += `<option value="${String(h).padStart(2, "0")}:30">${String(h).padStart(2, "0")}:30</option>`;
  }
});

btnBloqueio.addEventListener("click", () => {
  const dia = document.getElementById("diaBloqueio").value;
  const horario = document.getElementById("horaBloqueio").value;
  const dataFormatada = dia.split("-").reverse().join("/");

  fetch(`http://127.0.0.1:5000/bloquarDia`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      data: dataFormatada,
      horario: horario,
      id_barbeiro: idBarbeiro,
    }),
  }).then((response) => {
    if (response.ok) {
      alert("Seu dia foi bloqueado com sucesso!");
    } else {
      alert("infelizmente ocorreu um erro no seu Bloqueio!");
    }
  });
});
