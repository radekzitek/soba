import { defineStore } from 'pinia'
import { accountApi } from '@/services/accountApi'
import axios from 'axios'
import { config } from '@/config'

export const useAccountStore = defineStore('account', {
  state: () => ({
    accounts: [],
    loading: false,
    error: null,
    currentAccount: null
  }),

  getters: {
    activeAccounts: (state) => state.accounts.filter(acc => acc.is_active),
    totalBalance: (state) => state.accounts.reduce((sum, acc) => sum + Number(acc.current_balance), 0)
  },

  actions: {
    async fetchAccounts(includeInactive = false) {
      this.loading = true
      this.error = null
      try {
        const response = await axios.get(`${config.api.baseUrl}/accounts/`, {
          params: { include_inactive: includeInactive }
        })
        this.accounts = response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch accounts'
        console.error('Accounts fetch error:', error)
      } finally {
        this.loading = false
      }
    },

    async createAccount(accountData) {
      try {
        this.loading = true
        const newAccount = await accountApi.createAccount(accountData)
        this.accounts.push(newAccount)
        return newAccount
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to create account'
        throw error
      } finally {
        this.loading = false
      }
    },

    async updateAccount(id, accountData) {
      try {
        this.loading = true
        const updated = await accountApi.updateAccount(id, accountData)
        const index = this.accounts.findIndex(acc => acc.id === id)
        if (index !== -1) {
          this.accounts[index] = updated
        }
        return updated
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to update account'
        throw error
      } finally {
        this.loading = false
      }
    },

    async deleteAccount(id) {
      try {
        this.loading = true
        await accountApi.deleteAccount(id)
        this.accounts = this.accounts.filter(acc => acc.id !== id)
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to delete account'
        throw error
      } finally {
        this.loading = false
      }
    }
  }
}) 