import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark: localStorage.getItem('theme') === 'dark'
  }),

  actions: {
    toggleTheme(theme) {
      this.isDark = !this.isDark
      theme.global.name.value = this.isDark ? 'dark' : 'light'
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light')
    },

    initTheme(theme) {
      theme.global.name.value = this.isDark ? 'dark' : 'light'
    }
  }
}) 