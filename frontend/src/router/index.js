import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import TodosLosProductosView from '../views/TodosLosProductosView.vue'
import CrearProductoView from '../views/CrearProductoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', // Esta es tu página de entrada
      name: 'login',
      component: LoginView
    },
    {
      path: '/registro',
      name: 'registro',
      component: RegisterView
    },
    {
      path: '/productos',
      name: 'productos',
      component: () => import('../views/ProductosView.vue')
    },
    {
      path: '/productos-todos',
      name: 'todos',
      component: () => import('../views/TodosLosProductosView.vue')
    },
    {
      path: '/crear',
      name: 'crear',
      component: () => import('../views/CrearProductoView.vue') // ¡Asegúrate de que este nombre sea exacto!
    },

    {
      path: '/login',
      redirect: '/' // Si alguien busca /login, lo mandamos a la raíz
    }
  ]
})

export default router