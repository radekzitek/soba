/**
 * Main application entry point
 * Sets up Vue with Vuetify and Pinia
 */
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import { useAuthStore } from '@/stores/auth'

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import './style.css'

// Create and configure app
const app = createApp(App)
const pinia = createPinia()

// Install plugins
app.use(pinia)
app.use(vuetify)
app.use(router)

// Initialize auth state
const authStore = useAuthStore()
authStore.init()

// Mount app
app.mount('#app')
