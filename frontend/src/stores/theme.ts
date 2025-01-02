import { defineStore } from 'pinia'
import type { Theme } from 'vuetify'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark: localStorage.getItem('theme') === 'dark'
  }),

  actions: {
    toggleTheme(theme: Theme) {
      this.isDark = !this.isDark
      theme.global.name.value = this.isDark ? 'dark' : 'light'
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light')
    },

    initTheme(theme: Theme) {
      theme.global.name.value = this.isDark ? 'dark' : 'light'
    }
  }
}) 