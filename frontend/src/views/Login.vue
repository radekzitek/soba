<template>
  <v-container>
    <v-card>
      <!-- Login Form -->
      <v-card-title>{{ isRegistering ? 'Register' : 'Login' }}</v-card-title>
      <v-card-subtitle>
        {{ isRegistering ? 'Create a new account' : 'Please enter your credentials' }}
      </v-card-subtitle>

      <v-card-text>
        <!-- Registration Form -->
        <v-form v-if="isRegistering" @submit.prevent="handleRegister" ref="registerForm">
          <v-text-field
            v-model="registerData.user_login"
            label="Username"
            prepend-icon="mdi-account"
            required
          ></v-text-field>
          <v-text-field
            v-model="registerData.user_pass"
            label="Password"
            prepend-icon="mdi-lock"
            type="password"
            required
          ></v-text-field>
          <v-text-field
            v-model="registerData.user_full_name"
            label="Full Name"
            prepend-icon="mdi-card-account-details"
            required
          ></v-text-field>
          <v-text-field
            v-model="registerData.user_email"
            label="Email"
            prepend-icon="mdi-email"
            type="email"
            required
          ></v-text-field>
          <v-text-field
            v-model="registerData.user_note"
            label="Note (Optional)"
            prepend-icon="mdi-note"
          ></v-text-field>
          <v-btn type="submit" color="primary" class="mr-2">Register</v-btn>
          <v-btn @click="cancelRegister">Cancel</v-btn>
        </v-form>

        <!-- Login Form -->
        <v-form v-else @submit.prevent="handleLogin">
          <v-text-field
            v-model="username"
            label="Username"
            prepend-icon="mdi-account"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="Password"
            prepend-icon="mdi-lock"
            type="password"
            required
          ></v-text-field>
          <v-btn type="submit" color="primary" class="mr-2">Login</v-btn>
          <v-btn @click="startRegister" color="secondary">Register New User</v-btn>
        </v-form>

        <v-alert
          v-if="error || authStore.error"
          type="error"
          class="mt-3"
        >
          {{ error || authStore.error }}
        </v-alert>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { config } from '@/config'

const authStore = useAuthStore()
const router = useRouter()

// Login state
const username = ref('')
const password = ref('')

// Registration state
const isRegistering = ref(false)
const error = ref(null)
const registerData = ref({
  user_login: '',
  user_pass: '',
  user_full_name: '',
  user_email: '',
  user_note: ''
})

// Login handler
const handleLogin = async () => {
  error.value = null
  await authStore.login(username.value, password.value)
  if (authStore.isAuthenticated) {
    router.push('/dashboard')
  }
}

// Registration handlers
const startRegister = () => {
  isRegistering.value = true
  error.value = null
}

const cancelRegister = () => {
  isRegistering.value = false
  error.value = null
  registerData.value = {
    user_login: '',
    user_pass: '',
    user_full_name: '',
    user_email: '',
    user_note: ''
  }
}

const handleRegister = async () => {
  try {
    error.value = null
    await axios.post(`${config.api.baseUrl}/users/`, registerData.value)
    isRegistering.value = false
    // Pre-fill login form with registered username
    username.value = registerData.value.user_login
    password.value = ''
    cancelRegister() // Reset registration form
  } catch (err) {
    error.value = err.response?.data?.detail || 'Registration failed'
  }
}
</script> 