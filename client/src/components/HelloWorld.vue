<template>
  <div class="hello">
    {{data}}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data(){
    return {
      data: null
    }
  },
  methods: {
    getTest(){
      axios.get("http://127.0.0.1:5000/")
        .then(res => {
          this.data = res.data
        })
    }
  },
  created(){
    this.getTest()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
