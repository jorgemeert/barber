const btnConfirma = document.getElementById("btnConfirma");
const params = new URLSearchParams(window.location.search);
const idBarbeiro = params.get("id");

btnConfirma.addEventListener("click", () => {
  const marcados = document.querySelectorAll('input[class="servicos"]:checked');
  const promessas = [];
  marcados.forEach((marcado) => {
    const idValor = marcado.id.replace("check", "valor");
    const valor = document.getElementById(idValor).value;
    const nome_servico = marcado.dataset.nome;

    const promessa = fetch("http://127.0.0.1:5000/cadastroServico", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nome_servico: nome_servico,
        valor: valor,
        id_barbeiro: idBarbeiro,
      }),
    });
    promessas.push(promessa);
  });
  Promise.all(promessas).then(() => {
    window.location.href = `calendario.html?id=${idBarbeiro}`;
  });
});
