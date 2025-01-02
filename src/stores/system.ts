import { defineStore } from 'pinia'
import axios from 'axios'

interface SystemInfo {
  versions: {
    backend_version: string
    python_version: string
    fastapi_version: string
    sqlalchemy_version: string
    pydantic_version: string
  }
  database: {
    connected: boolean
    database_name: string
    host: string
    port: string
    user: string
  }
  environment: string
  cors_origins: string[]
  logging_config: {
    log_level: string
    log_file: string
    log_format: string
    max_file_size: string
    backup_count: number
  }
}

export const useSystemStore = defineStore('system', {
  state: () => ({
    systemInfo: null as SystemInfo | null,
    loading: false,
    error: null as string | null
  }),

  actions: {
    async fetchSystemInfo() {
      this.loading = true
      this.error = null
      try {
        const response = await axios.get('http://localhost:8000/debug/system')
        this.systemInfo = response.data
      } catch (error) {
        this.error = 'Failed to fetch system information'
        console.error('Error:', error)
      } finally {
        this.loading = false
      }
    }
  }
})