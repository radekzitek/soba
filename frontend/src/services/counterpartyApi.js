import axios from 'axios'
import { config } from '@/config'

export const counterpartyApi = {
  async getCounterparties(includeInactive = false) {
    const response = await axios.get(`${config.api.baseUrl}/counterparties/`, {
      params: { include_inactive: includeInactive }
    })
    return response.data
  },

  async getCounterparty(id) {
    const response = await axios.get(`${config.api.baseUrl}/counterparties/${id}`)
    return response.data
  },

  async createCounterparty(counterpartyData) {
    const response = await axios.post(`${config.api.baseUrl}/counterparties/`, counterpartyData)
    return response.data
  },

  async updateCounterparty(id, counterpartyData) {
    const response = await axios.put(`${config.api.baseUrl}/counterparties/${id}`, counterpartyData)
    return response.data
  },

  async deleteCounterparty(id) {
    await axios.delete(`${config.api.baseUrl}/counterparties/${id}`)
  }
} 