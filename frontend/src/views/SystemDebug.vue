<template>
  <v-container>
    <v-card class="mx-auto" max-width="1200" elevation="10">
      <!-- Header -->
      <v-card-title class="d-flex align-center text-h5">
        Runtime Information
        <v-spacer />
        <v-btn
          elevation="10"
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
        <v-row>
          <!-- Frontend Versions -->
          <v-col cols="12" md="6">
            <v-card height="100%" elevation="10">
              <v-card-title>Frontend Versions</v-card-title>
              <v-card-text>
                <v-list>
                  <v-list-item>
                    <v-list-item-title>Application Version</v-list-item-title>
                    <v-list-item-subtitle>{{ config.app.version }}</v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-title>Vue.js</v-list-item-title>
                    <v-list-item-subtitle>3.5.13</v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-title>Vuetify</v-list-item-title>
                    <v-list-item-subtitle>3.7.6</v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-title>Pinia</v-list-item-title>
                    <v-list-item-subtitle>2.3.0</v-list-item-subtitle>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>

          <!-- Backend Versions -->
          <v-col cols="12" md="6">
            <v-card height="100%" elevation="10">
              <v-card-title>Backend Versions</v-card-title>
              <v-card-text>
                <v-list>
                  <v-list-item v-for="(value, key) in store.systemInfo.versions" :key="key">
                    <v-list-item-title>{{ formatKey(key) }}</v-list-item-title>
                    <v-list-item-subtitle>{{ value }}</v-list-item-subtitle>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>

          <!-- Database Info -->
          <v-col cols="12" md="6">
            <v-card height="100%" elevation="10">
              <v-card-title>Database</v-card-title>
              <v-card-text>
                <v-list>
                  <v-list-item v-for="(value, key) in store.systemInfo.database" :key="key">
                    <v-list-item-title>{{ formatKey(key) }}</v-list-item-title>
                    <v-list-item-subtitle>
                      <v-chip
                        v-if="key === 'connected'"
                        :color="value ? 'success' : 'error'"
                        size="small"
                      >
                        {{ value ? 'Connected' : 'Disconnected' }}
                      </v-chip>
                      <span v-else>{{ value }}</span>
                    </v-list-item-subtitle>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>

          <!-- Environment and Logging -->
          <v-col cols="12" md="6">
            <v-card height="100%" elevation="10">
              <v-card-title>System Configuration</v-card-title>
              <v-card-text>
                <v-list>
                  <v-list-item>
                    <v-list-item-title>Environment</v-list-item-title>
                    <v-list-item-subtitle>
                      <v-chip :color="getEnvironmentColor(store.systemInfo.environment)">
                        {{ store.systemInfo.environment }}
                      </v-chip>
                    </v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item v-for="(value, key) in store.systemInfo.logging_config" :key="key">
                    <v-list-item-title>{{ formatKey(key) }}</v-list-item-title>
                    <v-list-item-subtitle>{{ value }}</v-list-item-subtitle>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useSystemStore } from '@/stores/system'
import { config } from '@/config'
import SystemInfoVersions from '@/components/system/SystemInfoVersions.vue'
import SystemInfoDatabase from '@/components/system/SystemInfoDatabase.vue'
import SystemInfoEnvironment from '@/components/system/SystemInfoEnvironment.vue'
import SystemInfoLogging from '@/components/system/SystemInfoLogging.vue'

const store = useSystemStore()

const formatKey = (key) => {
  return key.split('_').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ')
}

const getEnvironmentColor = (env) => {
  switch (env) {
    case 'production':
      return 'error'
    case 'staging':
      return 'warning'
    default:
      return 'success'
  }
}

const refreshData = () => {
  store.fetchSystemInfo()
}

onMounted(() => {
  store.fetchSystemInfo()
})
</script> 