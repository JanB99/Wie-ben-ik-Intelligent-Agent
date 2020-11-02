<template>
  <v-app>
    <v-main>
      <GameScreen/>
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import GameScreen from './screens/GameScreen';

export default {
  name: 'App',

  components: {
    GameScreen,
  },

  data: () => ({
    //
  }),
  created() {
    this.$vuetify.theme.light = true;
  }
};
</script>
