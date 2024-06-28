<template>
  <div class="p-4">
    <!-- Hidden file input -->
    <div class="flex justify-center text-center py-4">
      <input ref="fileInput" type="file" accept=".pdf" @change="handleFileSelect" class="hidden" />

      <!-- Button to select PDF -->
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        @click="$refs.fileInput.click()"
      >
        Select PDF
      </button>

      <!-- Toggle button for preview -->
      <button
        v-if="pdfSrc"
        class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded ml-4"
        @click="togglePreview"
      >
        {{ isPreviewEnabled ? 'Disable Preview' : 'Enable Preview' }}
      </button>
    </div>

    <!-- PDF preview -->
    <vue-pdf-app v-if="isPreviewEnabled && pdfSrc" :pdf="pdfSrc" style="height: 60vh" />

    <!-- Display extracted PDF text -->
    <div v-if="pdfText" class="flex justify-center text-center mt-10">
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-5 px-10  rounded"
        @click="getChatCompletion(pdfText)"
      >
        Commencer l'analyse
      </button>
      <loading-spinner :isLoading="isLoading"></loading-spinner>  
    </div>
    <modal :isVisible="isModalVisible" :message="first_pred" @close="isModalVisible = false"></modal>
  </div>
</template>

<script>
import VuePdfApp from 'vue3-pdf-app'
import axios from 'axios'
import LoadingSpinner from '../components/Loading.vue'
import Modal from '../components/Modal.vue'

export default {
  components: {
    VuePdfApp,
    LoadingSpinner,
    Modal
  },
  data() {
    return {
      pdfSrc: null,
      isPreviewEnabled: false,
      pdfText: '', // To store extracted PDF text
      first_pred: null,
      isLoading: false,
      isModalVisible: false,
    }
  },
  methods: {
    async handleFileSelect(event) {
      const file = event.target.files[0]
      if (file) {
        // Convert selected file to a local URL
        this.pdfSrc = URL.createObjectURL(file)
        this.isPreviewEnabled = true // Enable preview when a file is selected
        this.pdfText = await this.extractTextFromPdf(file)
      } else {
        this.pdfSrc = null
        this.isPreviewEnabled = false // Disable preview if no file selected
        this.pdfText = '' // Clear PDF text when no file selected
      }
    },
    togglePreview() {
      this.isPreviewEnabled = !this.isPreviewEnabled // Toggle preview state
    },
    async extractTextFromPdf(file) {
      try {
        const formData = new FormData()
        formData.append('file', file)

        const response = await axios.post('http://localhost:5000/extract_text', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        return response.data.text
      } catch (error) {
        console.error('Error extracting text from PDF:', error)
        return 'Error extracting text from PDF'
      }
    },
    async getChatCompletion(prompt) {
      this.isLoading = true
      try {
        const response = await axios.post("http://localhost:5000/analyse-ao", { prompt: prompt }, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        this.first_pred = response.data.response;
      } catch (error) {
        console.error("Error getting chat completion:", error);
      }
      this.isLoading = false
      this.isPreviewEnabled = false
      this.isModalVisible = true
    }
  }
}
</script>

<style scoped>
/* Add any scoped styles here */
</style>
