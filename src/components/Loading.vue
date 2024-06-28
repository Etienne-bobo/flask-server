<template>
    <div v-if="isLoading" class="fixed inset-0 flex items-center justify-center bg-gray-700 bg-opacity-50 z-50">
      <div class="loader ease-linear rounded-full border-8 border-t-8 border-gray-200 h-32 w-32"></div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isLoading: {
        type: Boolean,
        required: true
      }
    }
  }
  </script>
  
  <style>
  .loader {
    border-top-color: #3498db;
    animation: spin 1s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
  </style>
  