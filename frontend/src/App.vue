<template>
    <v-app>
        <v-app-bar>
            <v-app-bar-title>{{ config.app.name }}</v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn icon @click="themeStore.toggleTheme(theme)" class="mr-2">
                <v-icon>{{ themeStore.isDark ? 'mdi-weather-sunny' : 'mdi-weather-night' }}</v-icon>
            </v-btn>
            <template v-if="!authStore.isAuthenticated">
                <v-btn
                    prepend-icon="mdi-login"
                    class="mr-2"
                    @click="router.push('/login')"
                >
                    Login
                </v-btn>
                <v-btn
                    color="primary"
                    prepend-icon="mdi-account-plus"
                    @click="router.push('/register')"
                >
                    Register
                </v-btn>
            </template>
            <template v-else>
                <v-btn icon color="error" class="mr-2" @click="handleLogout">
                    <v-icon>mdi-logout</v-icon>
                </v-btn>
                <span class="mr-4">{{ authStore.displayName }}</span>
            </template>
        </v-app-bar>
        <v-main>
            <router-view></router-view>
        </v-main>
    </v-app>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { useThemeStore } from '@/stores/theme'
import { useTheme } from 'vuetify'
import { useRouter } from 'vue-router'
import { config } from '@/config'

const authStore = useAuthStore()
const themeStore = useThemeStore()
const theme = useTheme()
const router = useRouter()

// Initialize theme
themeStore.initTheme(theme)

const handleLogout = () => {
    authStore.logout()
    router.push('/')
}
</script>
