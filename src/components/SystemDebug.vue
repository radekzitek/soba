<template>
  <v-container>
    <v-card class="mx-auto" max-width="800">
      <v-card-title class="text-h5">
        System Debug Information
        <v-btn
          icon
          class="ml-auto"
          @click="refreshData"
          :loading="store.loading"
        >
          <v-icon>mdi-refresh</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text v-if="store.error" class="text-error">
        {{ store.error }}
      </v-card-text>

      <v-card-text v-else-if="store.systemInfo">
        <v-expansion-panels>
          <!-- Versions -->
          <v-expansion-panel>
            <v-expansion-panel-title>Versions</v-expansion-panel-title>
            <v-expansion-panel-text>
              <v-list>
                <v-list-item v-for="(value, key) in store.systemInfo.versions" :key="key">
                  <v-list-item-title>{{ key }}</v-list-item-title>
                  <v-list-item-subtitle>{{ value }}</v-list-item-subtitle>
                </v-list-item>
              </v-list>
            </v-expansion-panel-text>
          </v-expansion-panel>

          <!-- Database -->
          <v-expansion-panel>
            <v-expansion-panel-title>Database</v-expansion-panel-title>
            <v-expansion-panel-text>
              <v-list>
                <v-list-item v-for="(value, key) in store.systemInfo.database" :key="key">
                  <v-list-item-title>{{ key }}</v-list-item-title>
                  <v-list-item-subtitle>
                    <v-chip
                      v-if="key === 'connected'"
                      :color="value ? 'success' : 'error'"
                      small
                    >
                      {{ value ? 'Connected' : 'Disconnected' }}
                    </v-chip>
                    <span v-else>{{ value }}</span>
                  </v-list-item-subtitle>
                </v-list-item>
              </v-list>
            </v-expansion-panel-text>
          </v-expansion-panel>

          <!-- Environment -->
          <v-expansion-panel>
            <v-expansion-panel-title>Environment</v-expansion-panel-title>
            <v-expansion-panel-text>
              <v-chip :color="getEnvironmentColor">
                {{ store.systemInfo.environment }}
              </v-chip>
            </v-expansion-panel-text>
          </v-expansion-panel>

          <!-- Logging -->
          <v-expansion-panel>
            <v-expansion-panel-title>Logging Configuration</v-expansion-panel-title>
            <v-expansion-panel-text>
              <v-list>
                <v-list-item v-for="(value, key) in store.systemInfo.logging_config" :key="key">
                  <v-list-item-title>{{ key }}</v-list-item-title>
                  <v-list-item-subtitle>{{ value }}</v-list-item-subtitle>
                </v-list-item>
              </v-list>
            </v-expansion-panel-text>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-card-text>

      <v-card-text v-else>
        <v-progress-circular indeterminate />
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted, computed } from 'vue'
import { useSystemStore } from '@/stores/system'

const store = useSystemStore()

const getEnvironmentColor = computed(() => {
  switch (store.systemInfo?.environment) {
    case 'production':
      return 'error'
    case 'staging':
      return 'warning'
    default:
      return 'success'
  }
})

const refreshData = () => {
  store.fetchSystemInfo()
}

onMounted(() => {
  store.fetchSystemInfo()
})
</script>