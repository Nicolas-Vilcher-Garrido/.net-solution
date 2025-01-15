<template>
  <div>
    <h1>Lista de Entidades</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Última Atualização</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="entity in entities" :key="entity.id">
          <td>{{ entity.id }}</td>
          <td>{{ entity.name }}</td>
          <td>{{ new Date(entity.updatedAt).toLocaleString() }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      entities: [],
    };
  },
  async created() {
    try {
      const response = await axios.get("http://localhost:5000/api/MyEntity");
      this.entities = response.data;
    } catch (error) {
      console.error("Erro ao carregar entidades:", error);
    }
  },
};
</script>
