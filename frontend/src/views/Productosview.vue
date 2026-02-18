<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../stores/auth'

const auth = useAuthStore()
const productos = ref([])

const cargarProductos = async () => {
  try {
    const res = await axios.get('http://localhost:8000/productos', {
      headers: { Authorization: `Bearer ${auth.token}` } // <--- ¡La llave maestra!
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
  <div class="contenedor">
    <h2>🍳 Mis Recetas Privadas</h2>
    <div v-if="productos.length === 0">No tienes productos aún...</div>
    
    <div class="grid">
      <div v-for="p in productos" :key="p.id" class="card">
        <h3>{{ p.nombre }}</h3>
        <p>Propietario: <strong>{{ p.dueño_email }}</strong></p>
        <ul>
            <li v-for="ing in p.ingredientes" :key="ing.id">{{ ing.nombre }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1rem; }
.card { border: 1px solid #ddd; padding: 1rem; border-radius: 8px; background: #fff; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
h2 { color: #42b983; }
</style>