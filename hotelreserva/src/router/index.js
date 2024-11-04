// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import Nosotros from '@/views/Nosotros.vue';
import Reservas from '@/views/Reservas.vue';
import Login from '@/views/Login.vue';
import Admin from '@/views/admin.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/nosotros',
    name: 'Nosotros',
    component: Nosotros
  },
  {
    path: '/reservas',
    name: 'Reservas',
    component: Reservas
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('isAuthenticated')) {
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;





