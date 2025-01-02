/**
 * Main application entry point
 * Sets up Vue with Vuetify and Pinia
 */
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import vuetify from './plugins/vuetify'

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import './style.css'

// Create and configure app
const app = createApp(App)

// Install plugins
app.use(createPinia())
app.use(vuetify)

// Mount app
app.mount('#app')
