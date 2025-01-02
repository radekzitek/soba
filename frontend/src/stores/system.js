/**
 * System Store
 * Manages system information and debug data
 */
import { defineStore } from 'pinia'
import axios from 'axios'
import { config } from '@/config'

export const useSystemStore = defineStore('system', {
  state: () => ({
    systemInfo: null,
    loading: false,
    error: null
  }),

  actions: {
    /**
     * Fetches system debug information from the backend
     * Updates store state with the result or error
     */
    async fetchSystemInfo() {
      this.loading = true
      this.error = null
      
      try {
        const response = await axios.get('/api/debug/system')
        this.systemInfo = response.data
      } catch (error) {
        const errorMessage = error.response?.data?.detail || 'Failed to fetch system information'
        this.error = errorMessage
        console.error('System info fetch error:', error)
      } finally {
        this.loading = false
      }
    }
  }
}) 