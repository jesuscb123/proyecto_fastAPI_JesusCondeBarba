<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const auth = useAuthStore()
const router = useRouter()

const acceder = async () => {
  const exito = await auth.login(email.value, password.value)
  if (exito) {
    router.push('/productos') // Si el login es correcto, saltamos a productos
  } else {
    alert("Error: Usuario o contraseña incorrectos")
  }
}
</script>

<template>
  <div class="login">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="acceder">
      <input v-model="email" type="email" placeholder="Email (ej: jesus@paco.com)" required>
      <input v-model="password" type="password" placeholder="Contraseña" required>
      <button type="submit">Entrar</button>
      <router-link to="/registro">¿No tienes cuenta? Regístrate aquí</router-link>
    </form>
  </div>
</template>
