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

<script setup>
import { computed } from 'vue'

const props = defineProps({
  environment: {
    type: String,
    required: true
  }
})

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