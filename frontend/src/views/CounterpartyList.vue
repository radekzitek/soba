<template>
  <v-container>
    <v-card class="mb-4">
      <v-card-title class="d-flex align-center">
        Counterparties
        <v-spacer />
        <v-switch
          v-model="showInactive"
          label="Show Inactive"
          class="mr-4"
        ></v-switch>
        <v-btn
          color="primary"
          @click="openDialog()"
        >
          <v-icon left>mdi-plus</v-icon>
          Add Counterparty
        </v-btn>
      </v-card-title>

      <!-- Loading State -->
      <v-card-text v-if="store.loading">
        <v-progress-linear indeterminate></v-progress-linear>
      </v-card-text>

      <!-- Error State -->
      <v-card-text v-else-if="store.error">
        <v-alert type="error" title="Error" :text="store.error" />
      </v-card-text>

      <!-- Data Table -->
      <v-data-table
        v-else
        :headers="headers"
        :items="store.counterparties"
        :loading="store.loading"
      >
        <template v-slot:item.is_active="{ item }">
          <v-chip
            :color="item.raw.is_active ? 'success' : 'grey'"
            size="small"
          >
            {{ item.raw.is_active ? 'Active' : 'Inactive' }}
          </v-chip>
        </template>

        <template v-slot:item.actions="{ item }">
          <v-btn
            icon
            size="small"
            @click="openDialog(item.raw)"
            class="mr-2"
          >
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn
            icon
            size="small"
            color="error"
            @click="handleDelete(item.raw.id)"
          >
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </template>
      </v-data-table>
    </v-card>

    <!-- Create/Edit Dialog -->
    <CounterpartyDialog
      v-model="showDialog"
      :counterparty="selectedCounterparty"
      :loading="dialogLoading"
      @save="handleSave"
    />
  </v-container>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useCounterpartyStore } from '@/stores/counterparty'
import CounterpartyDialog from '@/components/CounterpartyDialog.vue'

const store = useCounterpartyStore()
const showDialog = ref(false)
const selectedCounterparty = ref(null)
const dialogLoading = ref(false)
const showInactive = ref(false)

const headers = [
  { title: 'Name', key: 'name' },
  { title: 'Description', key: 'description' },
  { title: 'Status', key: 'is_active', align: 'center' },
  { title: 'Actions', key: 'actions', align: 'end', sortable: false }
]

const openDialog = (counterparty = null) => {
  selectedCounterparty.value = counterparty
  showDialog.value = true
}

const handleSave = async (formData) => {
  dialogLoading.value = true
  try {
    if (selectedCounterparty.value) {
      await store.updateCounterparty(selectedCounterparty.value.id, formData)
    } else {
      await store.createCounterparty(formData)
    }
    showDialog.value = false
  } finally {
    dialogLoading.value = false
  }
}

const handleDelete = async (id) => {
  if (confirm('Are you sure you want to delete this counterparty?')) {
    await store.deleteCounterparty(id)
  }
}

watch(showInactive, (newValue) => {
  store.fetchCounterparties(newValue)
})

onMounted(() => {
  store.fetchCounterparties(showInactive.value)
})
</script> 