<script>

    import axios from 'axios';

    export default {
        name: 'PainelContatos',
        data(){
            return{

                contatos: [],
                carregando: true,
                erro: null,
            }
        },
        async mounted(){
            try{const response = await axios.get('https://jsonplaceholder.typicode.com/users');
            this.contatos = response.data;
            }catch (erro){
                this.erro = 'Erro no carregamento dos contatos';
                console.log(erro);
            }finally{
                this.carregando = false;
            }
        }
    }

</script>

<template>
    <div class="PainelContatos">
        <h1>Painel de Contatos</h1>
        <div v-if="carregando" class="alert">
            carregando...
        </div>

        <div v-else-if="erro" class="erro">
            {{ erro }}
        </div>

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
    display: flex;
    flex-direction: column;
    align-items: center;
    list-style: none;
    padding: 0;
}

.cartao-contato {
    width: 100%;
    max-width: 400px;
    box-sizing: border-box;
    text-align: center;
    background: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 12px;
    color: #333;
}

.cartao-contato h2 {
  margin-top: 0;
  color: #1a237e;
}
</style>