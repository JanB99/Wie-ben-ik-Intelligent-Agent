<template>
  <div class="start">
    <v-container>
      <v-card class="ma-2 pa-6 primary elevation-10" outlined rounded>
        <h1 class="text-center">Kies een karakter</h1>
        <v-layout row wrap justify-center class="mt-5">
          <v-flex
            v-for="(char, index) in characters"
            :key="index"
            md1
            class="ma-2"
          >
            <v-hover v-slot:default="{ hover }">
              <v-card
                :elevation="hover ? 16 : 0"
                @click="selectCharacter(char)"
                class="accent"
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
              </v-card>
            </v-hover>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>

    <v-dialog v-model="isOpen" width="unset">
      <Modal
        :character="playerCharacter"
        :getImage="getImage"
        :onCancel="() => isOpen = false"
        :onConfirm="startGame"
      />
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import Modal from "./Modal";

export default {
  name: "Start",
  components: {
    Modal,
  },
  props: {
    onGameStart: Function
  },
  data() {
    return {
      characters: null,
      playerCharacter: null,
      isOpen: false,
      ai: null
    };
  },
  methods: {
    getAllCharacters() {
      axios.get("http://127.0.0.1:5000/getAllCharacters").then((res) => {
        this.characters = res.data;
      });
    },
    getImage(id) {
      return `http://127.0.0.1:5000/images?id=${id}`;
    },
    selectCharacter(char) {
      this.playerCharacter = char;
      this.isOpen = true;
    },
    startGame(char){
      console.log(char)
      let id = char[char.length - 1]
      this.isOpen = false
      // this.$emit("onGameStart", id)
      this.onGameStart(id)
    },
  },
  created() {
    this.getAllCharacters();
  },
  mounted(){
    this.getAllCharacters();
  }
};
</script>

<style>
</style>