<template>
  <v-app>
    <v-app-bar>
      <v-app-bar-title>System Debug Dashboard</v-app-bar-title>
    </v-app-bar>

    <v-main>
      <SystemDebug />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import SystemDebug from '@/components/SystemDebug.vue'
</script>