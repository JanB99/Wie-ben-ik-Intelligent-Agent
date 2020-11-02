<template>
  <div class="player">
    <v-card outlined rounded class="ma-2 pa-6 elevation-10 secondary">
      <v-layout column justify-space-around>
        <v-flex md6>
          <v-select
            class="mx-4 mt-3"
            v-model="selectedLabel"
            @change="getValues"
            :items="labels"
            color="accent"
            outlined
            item-color="accent"
            label="Feature"
          ></v-select>

          <v-select
            v-model="selectedValue"
            :items="values"
            color="accent"
            class="mx-4"
            outlined
            item-color="accent"
            label="Value"
            :disabled="!selectedLabel"
          >
          </v-select>

          <div class="text-center mb-2">
            <v-btn
              @click="askQuestion"
              class="accent"
              :disabled="selectedValue == ''"
            >
              Stel vraag
            </v-btn>
          </div>
        </v-flex>
      </v-layout>
    </v-card>
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