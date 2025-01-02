<template>
    <v-app>
        <v-app-bar>
            <v-app-bar-title>{{ config.app.name }}</v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn icon @click="themeStore.toggleTheme(theme)">
                <v-icon>{{ themeStore.isDark ? 'mdi-weather-sunny' : 'mdi-weather-night' }}</v-icon>
            </v-btn>
            <template v-if="authStore.isAuthenticated"><span class="mr-4">{{ authStore.user }}</span>
                <v-btn color="error" @click="authStore.logout">Logout</v-btn>
            </template>
        </v-app-bar>
        <v-main min-width="400">
            <router-view></router-view>
        </v-main>
    </v-app>
</template>
<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { useThemeStore } from '@/stores/theme'
import { useTheme } from 'vuetify'
import { config } from '@/config'

const authStore = useAuthStore()
const themeStore = useThemeStore()
const theme = useTheme()

// Initialize theme
themeStore.initTheme(theme)
</script>
