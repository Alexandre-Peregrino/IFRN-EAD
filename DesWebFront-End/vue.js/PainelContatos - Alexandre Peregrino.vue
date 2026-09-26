<script>
// Importa a biblioteca Axios para fazer as requisições HTTP
import axios from 'axios';

export default {
  name: 'PainelContatos',

  // Passo 1: A Estrutura do Estado (Model)
  data() {
    return {
      contatos: [],      // Array vazio que receberá os contatos vindos do servidor
      carregando: true,  // Variável booleana que controla o status de carregamento
      erro: ''           // Guarda a mensagem de erro para exibir na tela
    };
  },

  // Passo 2: O Ciclo de Vida e a Requisição (Controller)
  async mounted() {
    try {
      // Requisição GET assíncrona via Axios
      const resposta = await axios.get('https://jsonplaceholder.typicode.com/users');

      // O Axios converte automaticamente o payload da resposta para JSON nativo
      // Atribui os dados retornados à variável de estado
      this.contatos = resposta.data;
    } catch (erro) {
      // Tratamento de exceções: se a URL for inválida ou a rede falhar,
      // a aplicação não trava e o erro é impresso no console de forma controlada
      console.error('Erro ao buscar os contatos:', erro);
      this.erro = 'Não foi possível carregar os contatos. Verifique sua conexão.';
    } finally {
      // Garante que o carregamento termina com sucesso OU com erro
      this.carregando = false;
    }
  }
};
</script>

<template>
  <div class="painel-contatos">
    <h1>Painel de Contatos Corporativos</h1>

    <!-- Estado de carregamento (enquanto a requisição não termina) -->
    <p v-if="carregando" class="status">Carregando contatos...</p>

    <!-- Mensagem de erro (caso a requisição falhe) -->
    <p v-else-if="erro" class="status erro">{{ erro }}</p>

    <!-- Passo 3: Renderização da Interface (View)
         Laço de repetição que renderiza a lista quando os dados chegam -->
    <ul v-else class="lista-contatos">
      <li v-for="contato in contatos" :key="contato.id" class="cartao-contato">
        <h2>{{ contato.name }}</h2>
        <p><strong>Empresa:</strong> {{ contato.company.name }}</p>
        <p><strong>E-mail:</strong> {{ contato.email }}</p>
        <p><strong>Telefone:</strong> {{ contato.phone }}</p>
        <p><strong>Cidade:</strong> {{ contato.address.city }}</p>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.painel-contatos {
  max-width: 700px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  color: #333; /* cor do texto padrão do painel */
}

.status {
  text-align: center;
  color: #555;
}

.status.erro {
  color: #d32f2f;
  font-weight: bold;
}

.lista-contatos {
  list-style: none;
  padding: 0;
}

.cartao-contato {
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 12px;
  color: #333; /* garante texto escuro dentro do cartão */
}

.cartao-contato h2 {
  margin-top: 0;
  color: #1a237e;
}
</style>