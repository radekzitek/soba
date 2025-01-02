<template>
  <v-container>
    <SystemDebug />
  </v-container>
</template>

<script setup>
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