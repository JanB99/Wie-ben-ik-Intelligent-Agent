<template>
  <div class="player">
    <v-container>
      <v-card class="ma-2 pa-6 primary elevation-10" outlined rounded>
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
            <v-card outlined rounded class="elevation-10 accent">
              <v-layout column justify-space-around>
                <v-flex md6>
                  <v-img :src="getImage(player[player.length - 1])"></v-img>
                </v-flex>

                <v-flex md6>

                  <v-select v-model="selectedLabel" @change="getValues" :items="labels">
                  </v-select>

                  <v-select v-model="selectedValue" :items="values">
                  </v-select>

                  <v-btn @click="askQuestion" :disabled="selectedValue == ''"> Stel vraag </v-btn>
<!-- 
                  <select v-model="selectedLabel" @change="getValues">
                    <option v-for="label in labels" :key="label">
                      {{ label }}
                    </option>
                  </select> -->
                  <!-- ==
                  <select v-model="selectedValue">
                    <option v-for="value in values" :key="value">
                      {{ value }}
                    </option>
                  </select>
                  ?
                  <button @click="askQuestion" :disabled="selectedValue == ''">
                    ask question
                  </button> -->
                </v-flex>
              </v-layout>
            </v-card>
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
      characters: null,
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
    getAllCharacters() {
      axios.get("http://127.0.0.1:5000/getAllCharacters").then((res) => {
        this.characters = res.data;
      });
    },
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
          this.onTurnEnd()
          // this.$emit('onTurnEnd')
        });
      // this.getAllCharacters();
      // this.getAiQuestion();
      //ai is nu aan de beurt
    },
  },
  created() {
    this.getAllCharacters();
    this.getLabels();
  },
};
</script>

<style>
</style>