<template>
  <v-dialog v-model="dialog" max-width="600">
    <v-card>
      <v-card-title>
        {{ account ? 'Edit Account' : 'Create Account' }}
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="handleSubmit" ref="form">
          <v-text-field
            v-model="formData.name"
            label="Account Name"
            required
          />
          <v-select
            v-model="formData.account_type"
            :items="accountTypes"
            label="Account Type"
            required
          />
          <v-text-field
            v-model="formData.initial_balance"
            label="Initial Balance"
            type="number"
            step="0.01"
            required
          />
          <v-text-field
            v-model="formData.currency"
            label="Currency"
            maxlength="3"
          />
          <v-textarea
            v-model="formData.description"
            label="Description"
          />
          <v-switch
            v-model="formData.is_active"
            label="Active"
          />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn @click="dialog = false">Cancel</v-btn>
        <v-btn
          color="primary"
          @click="handleSubmit"
          :loading="accountStore.loading"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useAccountStore } from '@/stores/account'

const props = defineProps({
  modelValue: Boolean,
  account: Object
})

const emit = defineEmits(['update:modelValue', 'save'])
const accountStore = useAccountStore()

const dialog = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

const accountTypes = [
  { title: 'Cash', value: 'cash' },
  { title: 'Checking', value: 'checking' },
  { title: 'Savings', value: 'savings' },
  { title: 'Credit Card', value: 'credit_card' },
  { title: 'Investment', value: 'investment' }
]

const formData = ref({
  name: '',
  account_type: 'checking',
  initial_balance: 0,
  currency: 'USD',
  description: '',
  is_active: true
})

watch(() => props.account, (newAccount) => {
  if (newAccount) {
    formData.value = { ...newAccount }
  } else {
    formData.value = {
      name: '',
      account_type: 'checking',
      initial_balance: 0,
      currency: 'USD',
      description: '',
      is_active: true
    }
  }
}, { immediate: true })

const handleSubmit = () => {
  emit('save', { ...formData.value })
}
</script> 