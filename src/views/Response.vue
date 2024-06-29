<template>
  <div>
    <!-- <quill-editor ref="editorRef" v-model:content="content" />
    <button @click="saveChanges">Enregistrer les modifications</button> -->
    <WebViewer initialDoc="../../backend/public/output.docx" />
  </div>
</template>
    
  <script>
import WebViewer from '../components/DocumentEditor.vue'
export default {
  name: 'DocumentEditor',
  components: {
    WebViewer
  },
  data() {
    return {
      content: ''
    }
  }
}
</script>
    
<style scoped>
/* Add your custom styles here */
</style>