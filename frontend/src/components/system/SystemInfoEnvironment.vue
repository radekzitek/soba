<template>
  <v-expansion-panel>
    <v-expansion-panel-title>Environment</v-expansion-panel-title>
    <v-expansion-panel-text>
      <v-chip :color="getEnvironmentColor">
        {{ environment }}
      </v-chip>
    </v-expansion-panel-text>
  </v-expansion-panel>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  environment: string
}>()

const getEnvironmentColor = computed(() => {
  switch (props.environment) {
    case 'production':
      return 'error'
    case 'staging':
      return 'warning'
    default:
      return 'success'
  }
})
</script> 