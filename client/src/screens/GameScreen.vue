<template>
  <div class="main">
      <v-container>
          <Start/>
          <AI />
      </v-container>
  </div>
</template>

<script>
import Start from '../components/Start'
import AI from '../components/AI'


export default {
    name: 'MainGameScreen',
    components: {
        Start,
        AI
    }
}
</script>

<style>

</style>