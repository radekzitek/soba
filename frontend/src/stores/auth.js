/**
 * Authentication Store
 * Manages user authentication state and token handling
 */
import { defineStore } from 'pinia'
import axios from 'axios'
import { config } from '@/config'

// Constants
const TOKEN_KEY = 'token'
const USER_KEY = 'user'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem(TOKEN_KEY),
    user: localStorage.getItem(USER_KEY),
    error: null
  }),

  getters: {
    isAuthenticated: (state) => Boolean(state.token)
  },

  actions: {
    /**
     * Authenticates user with credentials
     * @param {string} username - User's username
     * @param {string} password - User's password
     */
    async login(username, password) {
      try {
        const formData = new URLSearchParams()
        formData.append('username', username)
        formData.append('password', password)

        const response = await axios.post(
          `${config.api.baseUrl}/token`,
          formData.toString(),
          {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          }
        )
        
        this.setAuthData(response.data.access_token, username)
      } catch (error) {
        this.handleAuthError(error)
      }
    },

    /**
     * Logs out user and cleans up auth state
     */
    logout() {
      this.clearAuthData()
    },

    /**
     * Initializes auth state from storage
     */
    init() {
      if (this.token) {
        this.setAxiosAuth(this.token)
      }
    },

    // Private helper methods
    setAuthData(token, username) {
      this.token = token
      this.user = username
      this.error = null
      
      localStorage.setItem(TOKEN_KEY, token)
      localStorage.setItem(USER_KEY, username)
      
      this.setAxiosAuth(token)
    },

    clearAuthData() {
      this.token = null
      this.user = null
      this.error = null
      
      localStorage.removeItem(TOKEN_KEY)
      localStorage.removeItem(USER_KEY)
      
      delete axios.defaults.headers.common['Authorization']
    },

    setAxiosAuth(token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    },

    handleAuthError(error) {
      this.error = error.response?.data?.detail || 'Invalid username or password'
      console.error('Login error:', error)
    }
  }
}) 