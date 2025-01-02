<template>
  <v-container>
    <v-card class="mx-auto" max-width="800">
      <!-- Header -->
      <v-card-title class="d-flex align-center text-h5">
        System Debug Information
        <v-spacer />
        <v-btn
          icon
          @click="refreshData"
          :loading="store.loading"
          :disabled="store.loading"
          title="Refresh system information"
        >
          <v-icon>mdi-refresh</v-icon>
        </v-btn>
      </v-card-title>

      <!-- Error State -->
      <v-card-text v-if="store.error" class="text-error">
        <v-alert type="error" title="Error" :text="store.error" />
      </v-card-text>

      <!-- Loading State -->
      <v-card-text v-else-if="!store.systemInfo" class="d-flex justify-center">
        <v-progress-circular indeterminate />
      </v-card-text>

      <!-- Content -->
      <v-card-text v-else>
        <v-expansion-panels>
          <SystemInfoVersions :versions="store.systemInfo.versions" />
          <SystemInfoDatabase :database="store.systemInfo.database" />
          <SystemInfoEnvironment :environment="store.systemInfo.environment" />
          <SystemInfoLogging :config="store.systemInfo.logging_config" />
        </v-expansion-panels>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useSystemStore } from '@/stores/system'
import SystemInfoVersions from './system/SystemInfoVersions.vue'
import SystemInfoDatabase from './system/SystemInfoDatabase.vue'
import SystemInfoEnvironment from './system/SystemInfoEnvironment.vue'
import SystemInfoLogging from './system/SystemInfoLogging.vue'

const store = useSystemStore()

const refreshData = () => {
  store.fetchSystemInfo()
}

onMounted(() => {
  store.fetchSystemInfo()
})
</script> 