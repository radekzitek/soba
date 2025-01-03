<template>
  <v-container>
    <v-card class="mb-4">
      <v-card-title class="d-flex align-center">
        Accounts
        <v-spacer />
        <v-switch
          v-model="showInactive"
          label="Show Inactive"
          class="mr-4"
          color="primary"
          inset
        ></v-switch>
      </v-card-title>

      <!-- Loading State -->
      <v-card-text v-if="accountStore.loading" class="text-center">
        <v-progress-circular indeterminate />
      </v-card-text>

      <!-- Error State -->
      <v-card-text v-else-if="accountStore.error">
        <v-alert type="error" :text="accountStore.error" />
      </v-card-text>

      <!-- Account List -->
      <v-card-text v-else>
        <v-table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Type</th>
              <th class="text-right">Balance</th>
              <th>Currency</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="account in accountStore.accounts" :key="account.id">
              <td>{{ account.name }}</td>
              <td>{{ formatAccountType(account.account_type) }}</td>
              <td class="text-right">{{ formatCurrency(account.current_balance) }}</td>
              <td>{{ account.currency }}</td>
              <td>
                <v-chip
                  :color="account.is_active ? 'success' : 'error'"
                  size="small"
                >
                  {{ account.is_active ? 'Active' : 'Inactive' }}
                </v-chip>
              </td>
              <td>
                <v-btn
                  icon
                  size="small"
                  class="mr-2"
                  @click="editAccount(account)"
                >
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
                <v-btn
                  icon
                  size="small"
                  color="error"
                  @click="confirmDelete(account)"
                >
                  <v-icon>mdi-delete</v-icon>
                </v-btn>
              </td>
            </tr>
          </tbody>
        </v-table>
      </v-card-text>
    </v-card>

    <!-- Create/Edit Dialog -->
    <AccountDialog
      v-model="showDialog"
      :account="selectedAccount"
      :loading="dialogLoading"
      @save="handleSave"
    />

    <!-- Floating Action Button -->
    <v-btn
      color="primary"
      icon="mdi-plus"
      size="large"
      @click="openDialog()"
      class="fab-button"
    >
    </v-btn>

    <!-- Delete Confirmation -->
    <v-dialog v-model="showDeleteDialog" max-width="400">
      <v-card>
        <v-card-title>Confirm Delete</v-card-title>
        <v-card-text>
          Are you sure you want to delete this account?
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn @click="showDeleteDialog = false">Cancel</v-btn>
          <v-btn color="error" @click="handleDelete">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useAccountStore } from '@/stores/account'
import AccountDialog from '@/components/AccountDialog.vue'

const accountStore = useAccountStore()
const showDialog = ref(false)
const showDeleteDialog = ref(false)
const selectedAccount = ref(null)
const accountToDelete = ref(null)
const showInactive = ref(false)

const formatAccountType = (type) => {
  return type.split('_').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ')
}

const formatCurrency = (amount) => {
  return new Intl.NumberFormat('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  }).format(amount)
}

const editAccount = (account) => {
  selectedAccount.value = account
  showDialog.value = true
}

const confirmDelete = (account) => {
  accountToDelete.value = account
  showDeleteDialog.value = true
}

const handleSave = async (accountData) => {
  try {
    if (selectedAccount.value) {
      await accountStore.updateAccount(selectedAccount.value.id, accountData)
    } else {
      await accountStore.createAccount(accountData)
    }
    showDialog.value = false
    selectedAccount.value = null
  } catch (error) {
    console.error('Save failed:', error)
  }
}

const handleDelete = async () => {
  if (accountToDelete.value) {
    try {
      await accountStore.deleteAccount(accountToDelete.value.id)
      showDeleteDialog.value = false
      accountToDelete.value = null
    } catch (error) {
      console.error('Delete failed:', error)
    }
  }
}

watch(showInactive, (newValue) => {
  accountStore.fetchAccounts(newValue)
})

onMounted(() => {
  accountStore.fetchAccounts(showInactive.value)
})
</script>

<style scoped>
.fab-button {
  position: fixed;
  bottom: 16px;
  right: 16px;
}
</style> 