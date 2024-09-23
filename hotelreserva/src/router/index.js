import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue' // Asegúrate de que esta ruta es correcta

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/rooms',
    name: 'Rooms',
    component: () => import('../views/Rooms.vue')
  },
 
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router





