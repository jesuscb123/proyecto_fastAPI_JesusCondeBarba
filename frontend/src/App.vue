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
  <header v-if="true" class="main-header">
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

<style scoped>
/* Estos estilos aseguran que el header sea visible incluso si el CSS externo falla */
.main-header {
  display: block !important;
  width: 100%;
  min-height: 60px;
}

.contenedor-principal {
  padding-top: 20px;
}
</style>