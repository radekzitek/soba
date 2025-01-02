/**
 * Application configuration
 */
export const config = {
  app: {
    name: import.meta.env.VITE_APP_NAME,
    version: import.meta.env.VITE_APP_VERSION,
    environment: import.meta.env.VITE_APP_ENV
  },
  api: {
    baseUrl: import.meta.env.VITE_API_BASE_URL || '/api',
    timeout: 5000
  }
} 