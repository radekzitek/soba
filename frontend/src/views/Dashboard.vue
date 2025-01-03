<template>
  <v-container>
    <!-- Navigation Cards -->
    <v-row>
      <v-col cols="12" md="4">
        <v-card
          elevation="4"
          class="mb-4"
          :to="'/accounts'"
          hover
        >
          <v-card-title class="d-flex align-center">
            <v-icon size="large" color="primary" class="mr-2">mdi-bank</v-icon>
            Accounts
          </v-card-title>
          <v-card-text>
            Manage your bank accounts, credit cards, and cash
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card
          elevation="4"
          class="mb-4"
          disabled
        >
          <v-card-title class="d-flex align-center">
            <v-icon size="large" color="primary" class="mr-2">mdi-swap-horizontal</v-icon>
            Transactions
          </v-card-title>
          <v-card-text>
            Record and manage your income and expenses
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card
          elevation="4"
          class="mb-4"
          disabled
        >
          <v-card-title class="d-flex align-center">
            <v-icon size="large" color="primary" class="mr-2">mdi-chart-pie</v-icon>
            Budget
          </v-card-title>
          <v-card-text>
            Set and track your budgeting goals
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
// No imports needed anymore
</script> 