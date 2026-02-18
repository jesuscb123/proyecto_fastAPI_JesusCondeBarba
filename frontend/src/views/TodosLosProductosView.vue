<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../stores/auth'

const auth = useAuthStore()
const productos = ref([])

const cargarTodos = async () => {
  try {
    const res = await axios.get('http://localhost:8000/productos/todos', {
      headers: { Authorization: `Bearer ${auth.token}` }
    })
    productos.value = res.data
  } catch (error) {
    console.error("Error cargando recetas globales:", error)
  }
}

onMounted(cargarTodos)
</script>

<template>
  <div class="container">
    <h1>🌍 Recetas de la Comunidad</h1>
    <p>Aquí puedes ver lo que están cocinando otros usuarios.</p>

    <div class="grid">
      <div v-for="p in productos" :key="p.id" class="card">
        <h3>{{ p.nombre }}</h3>
        <p class="autor">👨‍🍳 Creado por: <strong>{{ p.dueño_email }}</strong></p>
        
        <div v-if="p.ingredientes.length > 0">
          <small>Ingredientes:</small>
          <ul>
            <li v-for="ing in p.ingredientes" :key="ing.id">{{ ing.nombre }}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container { padding: 20px; }
.grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); 
  gap: 20px; 
}
.card { 
  border: 1px solid #ddd; 
  border-radius: 10px; 
  padding: 15px; 
  background: #fdfdfd;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.autor { color: #666; font-size: 0.9rem; }
h1 { color: #2c3e50; }
</style>