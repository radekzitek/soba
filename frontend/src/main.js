/**
 * Main application entry point
 * Initializes Vue application with required plugins and configuration
 */

// Core imports
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

// Plugins
import vuetify from './plugins/vuetify'
import router from './router'

// Store imports
import { useAuthStore } from '@/stores/auth'
import { useThemeStore } from '@/stores/theme'

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import './style.css'

// Initialize application
const app = createApp(App)
const pinia = createPinia()

// Register plugins
app.use(pinia)
app.use(vuetify)
app.use(router)

// Initialize stores
const authStore = useAuthStore()
authStore.init()

// Mount application
app.mount('#app')
