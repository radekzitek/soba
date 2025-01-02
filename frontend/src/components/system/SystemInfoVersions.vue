<template>
  <v-expansion-panel>
    <v-expansion-panel-title>Versions</v-expansion-panel-title>
    <v-expansion-panel-text>
      <v-list>
        <v-list-item v-for="(value, key) in versions" :key="key">
          <v-list-item-title>{{ formatKey(key) }}</v-list-item-title>
          <v-list-item-subtitle>{{ value }}</v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </v-expansion-panel-text>
  </v-expansion-panel>
</template>

<script setup lang="ts">
import type { VersionInfo } from '@/types/system'

defineProps<{
  versions: VersionInfo
}>()

const formatKey = (key: string): string => {
  return key.split('_').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ')
}
</script> 