<template>
  <div class="player">
    <v-container>
      <v-card outlined rounded class="elevation-10 accent">
        <v-layout column justify-space-around>
          <v-flex md6>
            <v-img :src="getImage(player[player.length - 1])"></v-img>
          </v-flex>

          <v-flex md6>
            <v-select
              v-model="selectedLabel"
              @change="getValues"
              :items="labels"
            >
            </v-select>

            <v-select v-model="selectedValue" :items="values"> </v-select>

            <v-btn @click="askQuestion" :disabled="selectedValue == ''">
              Stel vraag
            </v-btn>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Player",
  data() {
    return {
      labels: [],
      values: [],
      selectedLabel: "",
      selectedValue: "",
    };
  },
  props: {
    player: Array,
    onTurnEnd: Function,
  },
  methods: {
    // getAllCharacters() {
    //   axios.get("http://127.0.0.1:5000/getAllCharacters").then((res) => {
    //     this.characters = res.data;
    //   });
    // },
    getImage(id) {
      return `http://127.0.0.1:5000/images?id=${id}`;
    },

    getLabels() {
      axios.get("http://127.0.0.1:5000/labels").then((res) => {
        this.labels = res.data.slice(0, res.data.length - 1);
      });
    },
    getValues() {
      axios
        .get(`http://127.0.0.1:5000/values?label=${this.selectedLabel}`)
        .then((res) => {
          this.values = res.data;
        });
      this.selectedValue = "";
    },

    askQuestion() {
      axios
        .get(
          `http://127.0.0.1:5000/question?label=${this.selectedLabel}&value=${this.selectedValue}`
        )
        .then((res) => {
          this.characters = res.data;
          this.onTurnEnd(res.data);
        });
      
    },
  },
  created() {
    this.getLabels();
  },
};
</script>

<style>
</style>