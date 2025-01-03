<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card elevation="10">
          <v-card-title class="text-h5 text-center pt-6">
            Login
          </v-card-title>
          <v-card-subtitle class="text-center">
            Please enter your credentials
          </v-card-subtitle>

          <v-card-text>
            <v-form @submit.prevent="handleLogin">
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
              <v-btn
                type="submit"
                color="primary"
                block
                class="mt-2"
                :loading="authStore.loading"
              >
                Login
              </v-btn>
            </v-form>

            <v-alert
              v-if="authStore.error"
              type="error"
              class="mt-3"
            >
              {{ authStore.error }}
            </v-alert>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const username = ref('')
const password = ref('')

const handleLogin = async () => {
  await authStore.login(username.value, password.value)
  if (authStore.isAuthenticated) {
    router.push('/dashboard')
  }
}
</script> 