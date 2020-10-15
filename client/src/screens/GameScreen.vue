<template>
  <div class="main">
    <v-container>
      <Start v-if="!player" :onGameStart="onGameStart" />
      <div v-else>
        <Player :player="player" :onTurnEnd="turnIncrement" v-if="turn % 2 == 0"/>
        <AI :onTurnEnd="turnIncrement" v-else/>
      </div>

      <v-btn @click="reset">reset</v-btn>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import Start from "../components/Start";
import AI from '../components/AI'
import Player from '../components/Player'

export default {
  name: "MainGameScreen",
  components: {
    Start,
    AI,
    Player
  },
  data() {
    return {
      player: null,
      ai: null,
      turn: 0,
    };
  },
  methods: {
    onGameStart(id) {
      axios.get(`http://127.0.0.1:5000/character?num=${id}`).then((res) => {
        this.player = res.data[0];
        this.ai = res.data[1];
      });
    },
    getPlayerCharacter(){
      axios.get("http://127.0.0.1:5000/character").then(res => {
        this.player = res.data[0];
        this.ai = res.data[1];
      })
    },
    reset(){
      this.turn = 0;
      this.player = null
      this.ai = null
      axios.get("http://127.0.0.1:5000/reset").then(res => {
        console.log(res.data)
      })
    },
    turnIncrement(){
      this.turn++
      console.log(this.turn)
    }
  },
  created(){
    this.getPlayerCharacter();
  }
};
</script>

<style>
</style>