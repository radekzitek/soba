<template>
  <v-container>
    <v-btn @click="handleLogout" color="error">Logout</v-btn>
    <SystemDebug />
  </v-container>
</template>

<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import SystemDebug from '@/components/SystemDebug.vue'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const handleLogout = () => {
  authStore.logout()
  router.push('/')
}
</script> 