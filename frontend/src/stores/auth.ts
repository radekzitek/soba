import { defineStore } from 'pinia'
import axios from 'axios'
import { config } from '@/config'

interface AuthState {
  token: string | null
  user: string | null
  error: string | null
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    token: localStorage.getItem('token'),
    user: localStorage.getItem('user'),
    error: null
  }),

  getters: {
    isAuthenticated: (state) => !!state.token
  },

  actions: {
    async login(username: string, password: string) {
      try {
        // Create form data
        const formData = new URLSearchParams()
        formData.append('username', username)
        formData.append('password', password)

        const response = await axios.post(`${config.api.baseUrl}/token`, 
          formData.toString(),
          {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          }
        )
        
        this.token = response.data.access_token
        this.user = username
        
        // Save to localStorage
        localStorage.setItem('token', this.token)
        localStorage.setItem('user', this.user)
        
        // Set axios default header
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
      } catch (error: any) {
        this.error = error.response?.data?.detail || 'Invalid username or password'
        console.error('Login error:', error)
      }
    },

    logout() {
      this.token = null
      this.user = null
      this.error = null
      
      // Clear localStorage
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      
      // Clear axios header
      delete axios.defaults.headers.common['Authorization']
    },

    // Initialize axios header if token exists
    init() {
      if (this.token) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
      }
    }
  }
}) 