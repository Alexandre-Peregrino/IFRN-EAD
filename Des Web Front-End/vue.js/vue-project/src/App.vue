<template>
  <div id="app">
    <PainelContatos />
  </div>
</template>

<script>
// Importa o componente que está na pasta components
import PainelContatos from './components/PainelContatos.vue';

export default {
  name: 'App',
  components: {
    PainelContatos
  }
};
</script>