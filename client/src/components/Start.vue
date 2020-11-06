<template>
  <div class="start">
    <v-container>
      <v-card class="ma-2 pa-6 primary elevation-10" outlined rounded>
        <h1 class="text-center">Kies een karakter</h1>
        <v-select
          class="mx-16 mt-3"
          v-model="strategy"
          :items="[
            'gini index',
            'entropy log2',
            'entropy log10',
            'entropy logE',
          ]"
          outlined
          :error="isError"
          color="accent"
          item-color="accent"
          label="Kies de strategie van de intelligent agent"
        ></v-select>
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
                class="secondary text-center"
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
                {{ char[char.length - 2] | capitalize }}
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
        :onCancel="() => (isOpen = false)"
        :onConfirm="startGame"
        :confirmText="'Bevestig karakter'"
        :headerText="'Je gekozen karakter'"
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
    onGameStart: Function,
  },
  data() {
    return {
      characters: [],
      playerCharacter: null,
      isOpen: false,
      ai: null,
      strategy: "",
      isError: false,
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
      if (this.strategy != "") {
        this.playerCharacter = char;
        this.isOpen = true;
        this.isError = false
      } else {
        this.isError = true;
      }
    },
    startGame(char) {
      let id = char[char.length - 1];
      this.isOpen = false;
      this.onGameStart(id, this.strategy);
    },
  },
  filters: {
    capitalize(value) {
      return value.charAt(0).toUpperCase() + value.slice(1);
    },
  },
  created() {
    this.getAllCharacters();
  },
  mounted() {
    this.getAllCharacters();
  },
};
</script>

<style>
</style>