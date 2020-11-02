<template>
  <div class="main">
    <v-app-bar color="accent">
      <div class="blue lighten-4 rounded ma-2 elevation-5" >
        <v-img src="../assets/Data_Intelligence_Logo.png" class="ma-1" width="200"></v-img>
      </div>

      <v-btn depressed class="mx-5 accent" @click="reset">restart</v-btn>
      <v-btn depressed class="mx-5 accent" @click="() => (openSim = true)">simulate</v-btn>
    </v-app-bar>

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
                class="ma-5"
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
              <v-flex md4 style="width: 100%">
                <v-card class="accent ma-2 pa-6 elevation-10" outlined rounded>
                  <v-layout column align-center>
                    <h3 class="my-3 secondary--text">Dit is je karakter</h3>
                    <v-hover v-slot:default="{ hover }">
                      <v-card
                        :elevation="hover ? 16 : 0"
                        @click="() => (isOpen = true)"
                        color="accent"
                        width="40%"
                      >
                        <v-img :src="getImage(player[player.length - 1])">
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
                      </v-card>
                    </v-hover>
                  </v-layout>
                </v-card>
              </v-flex>

              <v-flex md8 style="width: 100%">
                <Player
                  :player="player"
                  :onTurnEnd="turnIncrement"
                  v-if="turn % 2 == 0"
                />
                <AI
                  :onTurnEnd="turnIncrement"
                  :onAIWin="onAIWin"
                  :player="player"
                  v-else
                />
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>

    <v-dialog v-model="isOpen" width="unset">
      <Modal
        :character="player"
        :getImage="getImage"
        :onConfirm="() => (isOpen = false)"
        :confirmText="'OK'"
        :headerText="'Je karakter'"
      />
    </v-dialog>

    <v-dialog @click:outside="reset" v-model="isAIWin" width="unset">
      <Modal
        :character="aiAnswer"
        :getImage="getImage"
        :onConfirm="() => reset()"
        :confirmText="'Start opnieuw'"
        :headerText="'Je hebt verloren!'"
      />
    </v-dialog>

    <v-dialog @click:outside="reset" v-model="isPlayerWin" width="unset">
      <Modal
        :character="playerAnswer"
        :getImage="getImage"
        :onConfirm="() => reset()"
        :confirmText="'Start opnieuw'"
        :headerText="'Je hebt gewonnen!'"
      />
    </v-dialog>

    <v-dialog v-model="openSim" width="unset" persistent>
      <Simulation :onCancel="() => (openSim = false)" />
    </v-dialog>

    <v-bottom-sheet v-model="isSheetOpen" hide-overlay>
      <v-sheet
        class="text-center accent d-flex align-center justify-center"
        height="200px"
      >
        <div v-html="sheetText"></div>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
import axios from "axios";
import Start from "../components/Start";
import AI from "../components/AI";
import Player from "../components/Player";
import Modal from "../components/Modal";
import Simulation from "../components/SimulationModal";

import Vue from "vue";
import VueConfetti from "vue-confetti";

Vue.use(VueConfetti);

export default {
  name: "MainGameScreen",
  components: {
    Start,
    AI,
    Player,
    Modal,
    Simulation,
  },
  data() {
    return {
      player: null,
      turn: 0,
      characters: null,
      isOpen: false,
      isAIWin: false,
      isPlayerWin: false,
      openSim: false,
      aiAnswer: null,
      playerAnswer: null,
      isSheetOpen: false,
      sheetText: "",
    };
  },
  methods: {
    onGameStart(id) {
      axios.get(`http://127.0.0.1:5000/character?num=${id}`).then((res) => {
        this.player = res.data[0];
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
        this.player = res.data[0];
      });
    },
    reset() {
      axios.get("http://127.0.0.1:5000/reset").then((res) => {
        this.getAllCharacters();
        this.turn = 0;
        this.player = null;
        this.isAIWin = false;
        this.isPlayerWin = false;
        this.$confetti.stop();
        console.log(res.data);
      });
    },
    turnIncrement(data) {
      this.turn++;

      if (data) {
        this.isSheetOpen = true;
        setTimeout(() => (this.isSheetOpen = false), 4000);
        this.characters = data.characters;
        this.sheetText = `<h1 class="white--text">Je gestelde vraag, "${
          data.questionObject.question
        }", is ${
          data.boolean
            ? "<span class='green--text'>waar</span>"
            : "<span class='red--text'>niet waar</span>"
        }.</h1>`;
      }

      if (data && data.boolean && this.characters.length == 1) {
        this.isPlayerWin = true;
        this.playerAnswer = this.characters[0];
        this.$confetti.start(this.getConfigs());
      }
    },
    onAIWin(answer) {
      console.log(answer);
      this.aiAnswer = answer[0];
      this.isAIWin = true;
    },
    getConfigs() {
      let particles = [];
      for (let i = 1; i < 5; i++) {
        particles.push({
          type: "image",
          size: 50,
          url: `http://127.0.0.1:5000/images?id=${i}`,
        });
        for (let j = 0; j < 3; j++) {
          particles.push({ type: "circle" });
          particles.push({ type: "rect" });
          particles.push({ type: "heart" });
        }
      }

      return {
        particles,
        defaultDropRate: 10,
        defaultSize: 10,
        windSpeedMax: 0,
        particlesPerFrame: 1,
      };
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