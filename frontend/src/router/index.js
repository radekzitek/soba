import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Dashboard from '@/views/Dashboard.vue'
import Register from '@/views/Register.vue'
import { useAuthStore } from '@/stores/auth'
import CounterpartyList from '@/views/CounterpartyList.vue'

const routes = [
  { 
    path: '/', 
    component: Home 
  },
  { 
    path: '/login', 
    component: Login 
  },
  { 
    path: '/dashboard', 
    component: Dashboard, 
    meta: { requiresAuth: true } 
  },
  {
    path: '/register',
    component: Register
  },
  {
    path: '/accounts',
    component: () => import('@/views/AccountList.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/debug',
    component: () => import('@/views/SystemDebug.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/counterparties',
    name: 'counterparties',
    component: CounterpartyList,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/')
  } else {
    next()
  }
})

export default router 