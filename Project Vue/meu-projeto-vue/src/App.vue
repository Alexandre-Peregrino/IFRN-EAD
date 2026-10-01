<script>

import axios from 'axios';

export default {
  name: 'painelUsuarios',
  data() {
    return {
      carregando: true,
      usuarios: [],
      erro: null,
    }
  },
  async mounted() {
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/users');
      this.usuarios = response.data;
    } catch (erro) {
      this.erro = 'Erro ao carregar usuários';
    } finally {
      this.carregando = false;
    }
  },
}

</script>

<template>
  <div class="aplicacao-consumo">
    <h1>Painel de usuário da API</h1>

    <div v-if="carregando" class="alert">
      carregando...
    </div>

    <div v-else-if="erro" class="erro">
      {{ erro }}
    </div>

    <ul v-else>
      <li v-for="usuario in usuarios" :key="usuario.id">
        <strong> {{ usuario.name }} </strong>: {{ usuario.email }}
      </li>
    </ul>

  </div>


</template>

<style scoped>
.aplicacao-consumo {
  font-family: Arial, Helvetica, sans-serif;
  max-width: 600px;
  margin: 20px auto;
}

.alert {
  color: red;
  font-size: 1.2em;
  text-align: center;
}
</style>
