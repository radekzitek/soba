/**
 * Application Configuration
 * Centralizes environment-based configuration
 */
export const config = {
  app: {
    name: import.meta.env.VITE_APP_NAME || 'Soba',
    version: import.meta.env.VITE_APP_VERSION || '0.1.1',
    environment: import.meta.env.VITE_APP_ENV || 'development'
  },
  api: {
    baseUrl: import.meta.env.VITE_API_BASE_URL || '/api',
    timeout: 5000
  }
} 