<template>
  <div id="app">
    <el-container>
      <el-header><Header/></el-header>
      <el-main>
        <router-view/>
      </el-main>
      <el-footer><Footer/></el-footer>
    </el-container>
  </div>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>

<style>
#app {
  font-family: 'Lato', sans-serif;
}
</style>
