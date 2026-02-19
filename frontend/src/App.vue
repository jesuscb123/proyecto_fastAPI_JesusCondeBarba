<script setup>
import { RouterView, useRouter } from 'vue-router'
import { useAuthStore } from './stores/auth'

const auth = useAuthStore()
const router = useRouter()

const handleLogout = () => {
  auth.logout()
  router.push('/')
}
</script>

<template>
  <header v-if="auth.token" class="main-header">
    <nav>
      <div class="nav-links">
        <router-link to="/productos-todos">🌎 Comunidad</router-link>
        <router-link to="/productos">🍳 Mis Recetas</router-link>
        <router-link to="/crear" class="btn-nuevo">➕ Nueva Receta</router-link>
      </div>

      <div class="nav-user">
        <span class="user-email" v-if="auth.userEmail">{{ auth.userEmail }}</span>
        <button class="btn-salir" @click="handleLogout">Salir</button>
      </div>
    </nav>
  </header>

  <main class="contenedor-principal">
    <RouterView />
  </main>
</template>
