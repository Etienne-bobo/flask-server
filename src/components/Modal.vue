<template>
  <div
    v-if="isVisible"
    class="fixed inset-0 flex items-center justify-center bg-gray-700 bg-opacity-50 z-50"
  >
    <div class="bg-white rounded-lg p-6 w-1/2 overflow-y-auto max-h-80 z-50">
      <h2 class="text-2xl mb-4">{{ title }}</h2>
      <div class="grid grid-cols-2 gap-4">
        <div v-for="(value, key) in message" :key="key">
          <div class="mb-2">
            <span class="font-semibold">{{ key }}:</span> {{ value }}
          </div>
        </div>
      </div>
      <div class="flex justify-end">
        <button
        @click="saveToJson(message)"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
      >
        Enregistrer
      </button>
      <button
        @click="closeModal"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Close
      </button>
      </div>
    </div>
  </div>
  <SuccessNotification ref="successNotification" />
</template>
  import SuccessNotification from './components/SuccessNotification.vue';
  <script>
import { saveAs } from 'file-saver'
import axios from 'axios'
import SuccessNotification from '../components/SuccessNotification.vue';
export default {
    components: {
    SuccessNotification
  },
  props: {
    isVisible: {
      type: Boolean,
      required: true
    },
    title: {
      type: String,
      default: "Information extraites de l'AO"
    },
    message: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      //   structuredMessage: {}
    }
  },
  methods: {
    closeModal() {
      this.$emit('close')
    },
    // saveAsJson() {
    //     const blob = new Blob([JSON.stringify(this.message)], { type: 'application/json' })
    //     saveAs(blob, 'src/assets/chat_completion.json')
    // }
    async saveToJson(data) {
      this.isLoading = true
      try {
        const response = await axios.post('http://localhost:5000/save-json', data, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        this.first_pred = response.data.response
        this.$refs.successNotification.showNotification('Informations enregistrees!');
        // close the modal
        this.closeModal()
      } catch (error) {
        console.error('Error getting chat completion:', error)
      }
    }
  }
}
</script>
  
  <style>
/* CSS styles remain the same */
.fixed {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* .flex {
  display: flex;
  align-items: center;
  justify-content: center;
} */

.z-50 {
  z-index: 50;
}

.max-h-80 {
  max-height: 80vh;
  overflow-y: auto;
}
</style>
  