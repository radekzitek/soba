<template>
    <v-app>
        <v-app-bar>
            <!-- Navigation menu - shown only when authenticated -->
            <template v-if="authStore.isAuthenticated">
                <v-menu>
                    <template v-slot:activator="{ props }">
                        <v-btn
                            icon
                            v-bind="props"
                        >
                            <v-icon>mdi-menu</v-icon>
                        </v-btn>
                    </template>

                    <v-list>
                        <v-list-item
                            to="/dashboard"
                            :active="route.path === '/dashboard'"
                        >
                            <template v-slot:prepend>
                                <v-icon>mdi-view-dashboard</v-icon>
                            </template>
                            <v-list-item-title>Dashboard</v-list-item-title>
                        </v-list-item>

                        <v-list-item
                            to="/accounts"
                            :active="route.path === '/accounts'"
                        >
                            <template v-slot:prepend>
                                <v-icon>mdi-bank</v-icon>
                            </template>
                            <v-list-item-title>Accounts</v-list-item-title>
                        </v-list-item>

                        <v-list-item
                            to="/debug"
                            :active="route.path === '/debug'"
                        >
                            <template v-slot:prepend>
                                <v-icon>mdi-bug</v-icon>
                            </template>
                            <v-list-item-title>System Debug</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>
            </template>

            <!-- App logo and title -->
            <v-img
                src="/assets/soba.png"
                max-height="32"
                max-width="32"
                class="mr-2"
                alt="Soba Logo"
            ></v-img>
            <v-app-bar-title>Soba Finance</v-app-bar-title>
            
            <v-spacer></v-spacer>

            <!-- User menu -->
            <template v-if="authStore.isAuthenticated">
                <v-menu>
                    <template v-slot:activator="{ props }">
                        <v-btn
                            v-bind="props"
                            text
                        >
                            {{ authStore.displayName }}
                            <v-icon right>mdi-account-circle</v-icon>
                        </v-btn>
                    </template>

                    <v-list>
                        <v-list-item @click="handleLogout">
                            <template v-slot:prepend>
                                <v-icon>mdi-logout</v-icon>
                            </template>
                            <v-list-item-title>Logout</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>
            </template>
        </v-app-bar>

        <v-main>
            <router-view></router-view>
        </v-main>
    </v-app>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'

const authStore = useAuthStore()
const route = useRoute()
const router = useRouter()

const handleLogout = () => {
    authStore.logout()
    router.push('/login')
}
</script>
