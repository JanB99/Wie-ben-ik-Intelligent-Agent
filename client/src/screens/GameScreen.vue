<template>
  <div class="main">
    <v-container>
      <Start
        v-if="!player"
        :characters="characters"
        :onGameStart="onGameStart"
      />
      <v-card v-else class="ma-2 pa-6 primary elevation-10" outlined rounded>
        <v-layout row wrap justify-space-around>
          <v-flex md7>
            <v-layout row wrap justify-start>
              <v-flex
                v-for="(char, index) in characters"
                :key="index"
                md1
                class="ma-2"
              >
                <v-img :src="getImage(char[char.length - 1])">
                  <template v-slot:placeholder>
                    <v-row
                      class="fill-height ma-0"
                      align="center"
                      justify="center"
                    >
                      <v-progress-circular
                        indeterminate
                        color="grey lighten-5"
                      ></v-progress-circular>
                    </v-row>
                  </template>
                </v-img>
                {{ char[char.length - 2] }}
              </v-flex>
            </v-layout>
          </v-flex>

          <v-flex md3>
            <v-layout column align-center>
              <v-flex md4>
                <v-img
                  :src="getImage(player[player.length - 1])"
                  contain
                ></v-img>
              </v-flex>

              <v-flex md8 style="width: 100%">
                <Player
                  :player="player"
                  :onTurnEnd="turnIncrement"
                  v-if="turn % 2 == 0"
                />
                <AI :onTurnEnd="turnIncrement" :player="player" v-else />
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-card>

      <v-btn @click="reset">reset</v-btn>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import Start from "../components/Start";
import AI from "../components/AI";
import Player from "../components/Player";

export default {
  name: "MainGameScreen",
  components: {
    Start,
    AI,
    Player,
  },
  data() {
    return {
      player: null,
      // ai: null,
      turn: 0,
      characters: null,
    };
  },
  methods: {
    onGameStart(id) {
      axios.get(`http://127.0.0.1:5000/character?num=${id}`).then((res) => {
        this.player = res.data[0];
        // this.ai = res.data[1];
      });
    },
    getAllCharacters() {
      axios.get("http://127.0.0.1:5000/getAllCharacters").then((res) => {
        this.characters = res.data;
      });
    },
    getImage(id) {
      return `http://127.0.0.1:5000/images?id=${id}`;
    },
    getPlayerCharacter() {
      axios.get("http://127.0.0.1:5000/character").then((res) => {
        console.log(res)
        this.player = res.data[0];
        // this.ai = res.data[1];
      });
    },
    reset() {
      // this.ai = null;
      axios.get("http://127.0.0.1:5000/reset").then((res) => {
        this.getAllCharacters();
        this.turn = 0;
        this.player = null;
        console.log(res.data);
      });
    },
    turnIncrement(data) {
      this.turn++;
      if (data) {
        this.characters = data;
      }
      // this.getPlayerCharacter()
      console.log(this.characters);
    },
  },
  created() {
    this.getPlayerCharacter();
    this.getAllCharacters();
  },
};
</script>

<style>
</style>