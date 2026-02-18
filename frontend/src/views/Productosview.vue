<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../stores/auth'

const auth = useAuthStore()
const productos = ref([])

const cargarProductos = async () => {
  try {
    const res = await axios.get('http://localhost:8000/productos', {
      headers: { Authorization: `Bearer ${auth.token}` } 
    })
    productos.value = res.data
  } catch (error) {
    console.error("No pude cargar los productos", error)
  }
}

// Esto ejecuta la función en cuanto se abre la página
onMounted(cargarProductos)
</script>

<template>
  <div class="container">
    <h2>🌍 Recetas de la Comunidad</h2>
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
