<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const nombre = ref('')
const ingredientesRaw = ref('') // Lo que escribe el usuario
const auth = useAuthStore()
const router = useRouter()

const handleSubmit = async () => {
  // Convertimos el texto en una lista de OBJETOS, no solo strings
  const ingredientesArray = ingredientesRaw.value
    .split(',')
    .map(i => i.trim())
    .filter(i => i !== '')
    .map(nombreIngrediente => ({ nombre: nombreIngrediente })) // <--- ¡ESTA ES LA CLAVE!

  const exito = await auth.crearProducto(nombre.value, ingredientesArray)
  
  if (exito) {
    alert("¡Receta guardada!")
    router.push('/productos')
  } else {
    alert("Error 422: El formato de los datos no es correcto.")
  }
}
</script>

<template>
  <div class="form-container">
    <h2>🆕 Nueva Receta</h2>
    <form @submit.prevent="handleSubmit">
      <div class="input-group">
        <label>Nombre del plato:</label>
        <input v-model="nombre" placeholder="Ej: Paella Valenciana" required>
      </div>
      
      <div class="input-group">
        <label>Ingredientes (separados por comas):</label>
        <textarea v-model="ingredientesRaw" placeholder="Arroz, Pollo, Azafrán..." required></textarea>
      </div>

      <button type="submit">Publicar Receta</button>
    </form>
  </div>
</template>
