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
const USER_ID_KEY = 'user_id'
const USER_FULLNAME_KEY = 'user_fullname'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem(TOKEN_KEY),
    user: localStorage.getItem(USER_KEY),
    userId: localStorage.getItem(USER_ID_KEY),
    userFullName: localStorage.getItem(USER_FULLNAME_KEY),
    error: null
  }),

  getters: {
    isAuthenticated: (state) => Boolean(state.token),
    displayName: (state) => state.userFullName || state.user
  },

  actions: {
    /**
     * Authenticates user with credentials and fetches user details
     */
    async login(username, password) {
      try {
        // First, get the token
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
        
        const token = response.data.access_token
        
        // Set the token in axios headers before making the /users/me call
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
        
        // Then fetch user details using the token
        const userResponse = await axios.get(`${config.api.baseUrl}/users/me`)
        
        // Store all user information
        this.setAuthData({
          token,
          username: userResponse.data.user_login,
          userId: userResponse.data.id,
          fullName: userResponse.data.user_full_name
        })
      } catch (error) {
        this.handleAuthError(error)
      }
    },

    /**
     * Sets authentication data in state and localStorage
     */
    setAuthData({ token, username, userId, fullName }) {
      this.token = token
      this.user = username
      this.userId = userId
      this.userFullName = fullName
      this.error = null
      
      localStorage.setItem(TOKEN_KEY, token)
      localStorage.setItem(USER_KEY, username)
      localStorage.setItem(USER_ID_KEY, userId)
      localStorage.setItem(USER_FULLNAME_KEY, fullName || '')
      
      this.setAxiosAuth(token)
    },

    /**
     * Clears all authentication data
     */
    clearAuthData() {
      this.token = null
      this.user = null
      this.userId = null
      this.userFullName = null
      this.error = null
      
      localStorage.removeItem(TOKEN_KEY)
      localStorage.removeItem(USER_KEY)
      localStorage.removeItem(USER_ID_KEY)
      localStorage.removeItem(USER_FULLNAME_KEY)
      
      delete axios.defaults.headers.common['Authorization']
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

    setAxiosAuth(token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    },

    handleAuthError(error) {
      this.error = error.response?.data?.detail || 'Invalid username or password'
      console.error('Login error:', error)
    }
  }
}) 