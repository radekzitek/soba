<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card elevation="10">
          <v-card-title class="text-h5 text-center pt-6">
            Register New User
          </v-card-title>
          <v-card-subtitle class="text-center">
            Create a new account
          </v-card-subtitle>

          <v-card-text>
            <v-form @submit.prevent="handleRegister" ref="form">
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
              <div class="d-flex gap-2">
                <v-btn
                  type="submit"
                  color="primary"
                  block
                  class="mt-2"
                  :loading="loading"
                >
                  Register
                </v-btn>
                <v-btn
                  block
                  class="mt-2"
                  @click="router.push('/login')"
                >
                  Cancel
                </v-btn>
              </div>
            </v-form>

            <v-alert
              v-if="error"
              type="error"
              class="mt-3"
            >
              {{ error }}
            </v-alert>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { config } from '@/config'

const router = useRouter()
const error = ref(null)
const loading = ref(false)

const registerData = ref({
  user_login: '',
  user_pass: '',
  user_full_name: '',
  user_email: '',
  user_note: ''
})

const handleRegister = async () => {
  try {
    loading.value = true
    error.value = null
    await axios.post(`${config.api.baseUrl}/users/`, registerData.value)
    router.push('/login')
  } catch (err) {
    error.value = err.response?.data?.detail || 'Registration failed'
  } finally {
    loading.value = false
  }
}
</script> 