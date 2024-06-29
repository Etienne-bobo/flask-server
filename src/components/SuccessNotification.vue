<template>
    <div class="fixed left-0 mb-4 m-4 p-4 bg-green-500 text-white rounded-lg shadow-md z-50 max-w-xs max-h-24"
         v-if="show">
      <div class="flex items-center justify-between">
        <div class="flex items-center">
          <svg class="h-6 w-6 mr-2 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M5 13l4 4L19 7"/>
          </svg>
          <p class="text-sm font-medium">Success!</p>
        </div>
        <!-- <button @click="closeNotification"
                class="text-white hover:text-white focus:outline-none focus:text-white">
        </button> -->
      </div>
      <p class="text-sm mt-1">{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SuccessNotification',
    data() {
      return {
        show: false,
        message: ''
      };
    },
    methods: {
      showNotification(message) {
        this.message = message;
        this.show = true;
        setTimeout(() => {
          this.show = false;
        }, 3000); // Adjust the timeout (in milliseconds) as needed
      },
      closeNotification() {
        this.show = false;
      }
    }
  };
  </script>

  