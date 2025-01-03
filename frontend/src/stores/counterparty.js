import { defineStore } from 'pinia'
import { counterpartyApi } from '@/services/counterpartyApi'

export const useCounterpartyStore = defineStore('counterparty', {
  state: () => ({
    counterparties: [],
    loading: false,
    error: null
  }),

  getters: {
    activeCounterparties: (state) => 
      state.counterparties.filter(c => c.is_active)
  },

  actions: {
    async fetchCounterparties(includeInactive = false) {
      this.loading = true
      this.error = null
      try {
        this.counterparties = await counterpartyApi.getCounterparties(includeInactive)
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to fetch counterparties'
        console.error('Counterparties fetch error:', error)
      } finally {
        this.loading = false
      }
    },

    async createCounterparty(counterpartyData) {
      this.loading = true
      this.error = null
      try {
        const newCounterparty = await counterpartyApi.createCounterparty(counterpartyData)
        this.counterparties.push(newCounterparty)
        return newCounterparty
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to create counterparty'
        throw error
      } finally {
        this.loading = false
      }
    },

    async updateCounterparty(id, counterpartyData) {
      this.loading = true
      this.error = null
      try {
        const updatedCounterparty = await counterpartyApi.updateCounterparty(id, counterpartyData)
        const index = this.counterparties.findIndex(c => c.id === id)
        if (index !== -1) {
          this.counterparties[index] = updatedCounterparty
        }
        return updatedCounterparty
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to update counterparty'
        throw error
      } finally {
        this.loading = false
      }
    },

    async deleteCounterparty(id) {
      this.loading = true
      this.error = null
      try {
        await counterpartyApi.deleteCounterparty(id)
        this.counterparties = this.counterparties.filter(c => c.id !== id)
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to delete counterparty'
        throw error
      } finally {
        this.loading = false
      }
    }
  }
}) 