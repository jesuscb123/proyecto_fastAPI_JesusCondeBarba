import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    userEmail: localStorage.getItem('email') || null,
  }),
  actions: {
    async login(email, password) {
      // Preparamos los datos como espera OAuth2 en FastAPI
      const formData = new FormData()
      formData.append('username', email)
      formData.append('password', password)

      try {
        const res = await axios.post('http://localhost:8000/login', formData)
        this.token = res.data.access_token
        this.userEmail = email
        
        // Guardamos en el navegador para que no se borre al refrescar
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
      localStorage.clear()
    },

    async registrar(email, password) {
  try {
    // Llamamos a tu endpoint de registrar usuario
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


  }
})