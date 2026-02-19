<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const auth = useAuthStore()
const router = useRouter()

const handleRegistro = async () => {
  const exito = await auth.registrar(email.value, password.value)
  if (exito) {
    alert("¡Usuario creado con éxito! Ahora inicia sesión.")
    router.push('/') // Nos manda al login
  } else {
    alert("Error: El email ya existe o los datos son incorrectos")
  }
}
</script>

<template>
  <div class="register">
    <h2>Registro</h2>
    <form @submit.prevent="handleRegistro">
      <input v-model="email" type="email" placeholder="Tu nuevo email" required>
      <input v-model="password" type="password" placeholder="Tu contraseña" required>
      <button type="submit">Registrarme</button>
    </form>
    <router-link to="/">¿Ya tienes cuenta? Entra aquí</router-link>
  </div>
</template>
