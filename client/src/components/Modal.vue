<template>
  <div class="modal">
    <v-card>
      <v-card-title>Je gekozen karakter</v-card-title>

      <v-layout justify-space-around>
        <v-flex md6 class="ma-3">
          <v-img
            :src="getImage(character ? character[character.length - 1] : 0)"
          ></v-img>
        </v-flex>

        <v-flex md6 class="ma-3">
          <v-layout column wrap>
            <v-flex v-for="(feature, index) in character" :key="index">
              <span class="font-weight-bold">{{ labels[index] }}</span> :
              {{ feature }}
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>

      <v-card-actions>
        <v-btn class="accent">Bevestig karakter</v-btn>
        <v-btn class="error">Annuleer</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Modal",
  props: {
    character: Array,
    getImage: Function,
  },
  data() {
    return {
      labels: [],
    };
  },
  methods: {
    getLabels() {
      axios.get("http://127.0.0.1:5000/labels").then((res) => {
        this.labels = res.data;
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