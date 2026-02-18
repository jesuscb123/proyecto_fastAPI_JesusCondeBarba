<script setup>
import { RouterView, useRouter } from 'vue-router'
import { useAuthStore } from './stores/auth'

const auth = useAuthStore()
const router = useRouter()

const handleLogout = () => {
  auth.logout()
  router.push('/login')
}
</script>

<template>
  <header v-if="auth.token">
    <nav>
      <router-link to="/productos-todos">🌎 Comunidad</router-link> | 
      <router-link to="/productos">🍳 Mis Recetas</router-link> | 
      <span>Bienvenido, {{ auth.userEmail }}</span> |
      <button @click="handleLogout">Salir</button>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
nav { background: #34495e; padding: 1rem; color: white; }
nav a { color: #42b983; margin: 0 10px; text-decoration: none; font-weight: bold; }
nav a.router-link-active { color: white; border-bottom: 2px solid white; }
button { background: #e74c3c; color: white; border: none; padding: 5px 10px; cursor: pointer; border-radius: 4px; }
</style>