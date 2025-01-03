<template>
  <v-dialog v-model="dialog" max-width="600">
    <v-card>
      <v-card-title>
        {{ counterparty ? 'Edit Counterparty' : 'Create Counterparty' }}
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="handleSubmit" ref="form">
          <v-text-field
            v-model="formData.name"
            label="Name"
            required
          ></v-text-field>

          <v-textarea
            v-model="formData.description"
            label="Description"
            rows="3"
          ></v-textarea>

          <v-switch
            v-model="formData.is_active"
            label="Active"
            color="primary"
          ></v-switch>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="grey" @click="dialog = false">Cancel</v-btn>
        <v-btn color="primary" @click="handleSubmit" :loading="loading">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  modelValue: Boolean,
  counterparty: {
    type: Object,
    default: null
  },
  loading: Boolean
})

const emit = defineEmits(['update:modelValue', 'save'])

const dialog = ref(props.modelValue)
const formData = ref({
  name: '',
  description: '',
  is_active: true
})

watch(() => props.modelValue, (val) => {
  dialog.value = val
})

watch(dialog, (val) => {
  emit('update:modelValue', val)
})

watch(() => props.counterparty, (counterparty) => {
  if (counterparty) {
    formData.value = { ...counterparty }
  } else {
    formData.value = {
      name: '',
      description: '',
      is_active: true
    }
  }
}, { immediate: true })

const handleSubmit = () => {
  emit('save', { ...formData.value })
}
</script> 