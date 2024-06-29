<template>
  <div class="mx-auto p-4">
    <div v-if="responseObject" class="bg-white shadow-md rounded-lg overflow-hidden">
      <div class="p-4">
        <h2 class="text-xl font-semibold mb-2">Informations extraites de l'AO</h2>
        <div class="grid grid-cols-2 gap-4">
          <div v-for="(value, key) in responseObject" :key="key">
            <div class="mb-2">
              <span class="font-semibold">{{ key }}:</span> {{ value }}
            </div>
          </div>
        </div>
      </div>
      <div class="flex justify-end">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white m-4 font-bold py-2 px-4 rounded"
          @click="generateResponse"
        >
          Generer une reponse
        </button>
      </div>
      <success-notification ref="successNotification" />
    </div>
    <div v-else>
      <p>Aucune information disponible</p>
    </div>
  </div>
</template>

<script>
import SuccessNotification from '@/components/SuccessNotification.vue'
export default {
  name: 'ResponseVisualization',
  data() {
    return {
      responseObject: null
    }
  },
  components: {
    SuccessNotification
  },
  mounted() {
    // Load JSON file using a relative path
    fetch('../../saved_json/data.json')
      .then((response) => response.json())
      .then((data) => {
        this.responseObject = data
      })
      .catch((error) => {
        console.error('Error loading JSON file:', error)
      })
  },
  methods: {
    async generateResponse() {
      try {
        await fetch('http://localhost:5000/generate-document', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.responseObject)
        })
        this.$refs.successNotification.showNotification('Template generé avec succès!')
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
}
</script>

<style scoped>
/* Tailwind CSS classes */
.container {
  max-width: 800px;
}
.bg-white {
  background-color: #ffffff;
}
.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.rounded-lg {
  border-radius: 0.5rem;
}
.overflow-hidden {
  overflow: hidden;
}
.p-4 {
  padding: 1rem;
}
.text-xl {
  font-size: 1.25rem;
}
.font-semibold {
  font-weight: 600;
}
.mb-2 {
  margin-bottom: 0.5rem;
}
.grid {
  display: grid;
}
.grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.gap-4 {
  gap: 1rem;
}
</style>
