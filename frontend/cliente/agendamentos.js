const params = new URLSearchParams(window.location.search);
const idBarberio = params.get("id");
const servicosBarbeiro = document.getElementById("servicosBarbeiro");

document.addEventListener("DOMContentLoaded", () => {
  console.log(params, idBarberio);
  fetch(`http://127.0.0.1:5000/servicos/${idBarberio}`)
    .then((response) => response.json())
    .then((servicos) => {
      servicos.forEach((servico) => {
        servicosBarbeiro.innerHTML += `
        <div>
            <p>${servico.nome_servico}</p>
            <p>${servico.valor}</p>

        </div>
        `;
      });
    });
});
