import axios from 'axios'
import { config } from '@/config'

export const accountApi = {
  async getAccounts(includeInactive = false) {
    const response = await axios.get(`${config.api.baseUrl}/accounts/`, {
      params: { include_inactive: includeInactive }
    })
    return response.data
  },

  async getAccount(id) {
    const response = await axios.get(`${config.api.baseUrl}/accounts/${id}`)
    return response.data
  },

  async createAccount(accountData) {
    const response = await axios.post(`${config.api.baseUrl}/accounts/`, accountData)
    return response.data
  },

  async updateAccount(id, accountData) {
    const response = await axios.put(`${config.api.baseUrl}/accounts/${id}`, accountData)
    return response.data
  },

  async deleteAccount(id) {
    await axios.delete(`${config.api.baseUrl}/accounts/${id}`)
  }
} 