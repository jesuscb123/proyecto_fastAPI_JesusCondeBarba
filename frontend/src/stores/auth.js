import { defineStore } from 'pinia'
import axios from 'axios'

// --- CONFIGURACIÓN GLOBAL DE AXIOS ---
// Esto añade el token automáticamente a todas las peticiones al backend
axios.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    userEmail: localStorage.getItem('email') || null,
  }),

  actions: {
    async login(email, password) {
      const formData = new FormData()
      formData.append('username', email)
      formData.append('password', password)

      try {
        const res = await axios.post('http://localhost:8000/usuarios/login', formData)

        this.token = res.data.access_token
        this.userEmail = email

        localStorage.setItem('token', this.token)
        localStorage.setItem('email', email)

        return true
      } catch (error) {
        console.error("Error al entrar:", error)
        return false
      }
    },

    logout() {
      this.token = null
      this.userEmail = null
      localStorage.removeItem('token')
      localStorage.removeItem('email')
      localStorage.clear()

    },

    async registrar(email, password) {
      try {
        await axios.post('http://localhost:8000/usuarios', {
          email: email,
          password: password
        })
        return true
      } catch (error) {
        console.error("Error en registro:", error)
        return false
      }
    },

    async crearProducto(nombre, ingredientesArray) {
      try {

        await axios.post('http://localhost:8000/productos', {
          nombre: nombre,
          ingredientes: ingredientesArray
        })
        return true
      } catch (error) {
        console.error("Error al crear:", error.response?.data || error)
        return false
      }
    }
  }
})