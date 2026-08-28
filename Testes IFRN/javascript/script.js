//Evento mostra e esconde uma div planeta

var elemento = document.getElementById("filha1");
var botao = document.getElementById("botao");

botao.addEventListener("click", function() {
    if (elemento.style.display === "none") {
        elemento.style.display = "block";
        mensagem.textContent = "Visível!";
    } else {
        elemento.style.display = "none";
        mensagem.textContent = "Ocultada!";
    }

});

// Adicionando elementos no array e mostrando na tela

var dados = []; // array vazio que vai guardar tudo

var input = document.getElementById("nome"); //input recebe nome digitado
var botao = document.getElementById("adicionar"); // Referência ao elemento do botão
var lista = document.getElementById("lista");//Armazena o elemento ul para usar na função

botao.addEventListener("click", function() {
    var valor = input.value; // pega o que foi digitado

    if (valor !== "") { // não adiciona campo vazio
        dados.push(valor); // adiciona no array
        input.value = ""; // limpa o campo após adicionar

        // cria um item na lista para mostrar o dado
        var item = document.createElement("li");//Cria o li
        item.textContent = valor;//Item recebe o valor do input
        lista.appendChild(item);//Lista armazena o ítem

        console.log(dados); // veja o array no console do navegador
        console.log(botao);

    }
});
