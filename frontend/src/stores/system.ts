import { defineStore } from 'pinia'
import axios from 'axios'
import type { SystemInfo } from '@/types/system'

interface SystemState {
  systemInfo: SystemInfo | null
  loading: boolean
  error: string | null
}

/**
 * Store for managing system debug information
 * Handles fetching and storing system state from the backend
 */
export const useSystemStore = defineStore('system', {
  state: (): SystemState => ({
    systemInfo: null,
    loading: false,
    error: null
  }),

  actions: {
    /**
     * Fetches system information from the backend
     * Updates store state with the result or error
     */
    async fetchSystemInfo() {
      this.loading = true
      this.error = null
      try {
        const response = await axios.get<SystemInfo>('/api/debug/system')
        this.systemInfo = response.data
      } catch (error) {
        this.error = 'Failed to fetch system information'
        console.error('Error fetching system info:', error)
      } finally {
        this.loading = false
      }
    }
  }
}) 