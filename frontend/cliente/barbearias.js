lista_barbearias = document.getElementById("list_barbearias");

document.addEventListener("DOMContentLoaded", () => {
  fetch("http://127.0.0.1:5000/barbearias")
    .then((response) => response.json())
    .then((dados) => {
      dados[
        {
          nome: nome,
          nome_barbearia: nome_barbearia,
          id: id,
          foto: foto,
          localizacao,
        }
      ];
    });
});
