<template>
  <div class="header">
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      msg: 'Header Component'
    }
  }
}
</script>

<style scoped>
</style>
