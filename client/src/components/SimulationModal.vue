<template>
  <div class="simulation">
    <v-card>
      <v-card-title>Simuleer intelligent agents</v-card-title>
      <v-card-subtitle
        >Simuleer twee agents die tegen elkaar het spel spelen op basis van
        verschillende strategiën.<br />
        Selecteer te hanteren strategiën en geef het aantal te spelen games.
      </v-card-subtitle>

      <v-select
        class="mx-16 mt-3"
        v-model="strategyAI1"
        :items="['gini index', 'entropy log2', 'entropy log10', 'entropy logE']"
        outlined
        color="accent"
        item-color="accent"
        label="Agent 1 strategie"
      ></v-select>

      <v-select
        v-model="strategyAI2"
        :items="['gini index', 'entropy log2', 'entropy log10', 'entropy logE']"
        class="mx-16"
        outlined
        color="accent"
        item-color="accent"
        label="Agent 2 strategie"
      >
      </v-select>

      <v-text-field
        class="mx-16"
        suffix="games"
        color="accent"
        label="Number of games"
        type="number"
        v-model="numberGames"
      ></v-text-field>

      <v-card v-if="result" outlines class="primary mx-5">
        <v-card-title> Resultaten </v-card-title>
        <v-card-subtitle class="py-0 accent--text font-weight-bold"
          >Aantal games gespeeld:
          {{ result ? result["num Games"] : null }}</v-card-subtitle
        >
        <v-card-subtitle class="py-0 accent--text font-weight-bold"
          >Gemiddeld aantal beurten:
          {{ result ? result["average turns"].toFixed(3) : null }}</v-card-subtitle
        >
        <v-layout>
          <v-flex class="ma-3 pa-3 accent flex-grow-1 rounded">
            <h3 class="primary--text">Intelligent agent 1:</h3>
            <p class="primary--text ma-0">
              Ratio: {{ result ? result["AI 1"].ratio.toFixed(3) : null }}
              <br />
            </p>
            <p class="primary--text ma-0">
              Strategie: {{ result ? result["AI 1"].strategy : null }} <br />
            </p>
            <p class="primary--text ma-0">
              Aantal wins: {{ result ? result["AI 1"]["total wins"] : null }}
              <br />
            </p>
          </v-flex>

          <v-flex class="ma-3 pa-3 accent flex-grow-1 rounded">
            <h3 class="primary--text">Intelligent agent 2:</h3>
            <p class="primary--text ma-0">
              Ratio: {{ result ? result["AI 2"].ratio.toFixed(3) : null }}
            </p>
            <p class="primary--text ma-0">
              Strategie: {{ result ? result["AI 2"].strategy : null }}
            </p>
            <p class="primary--text ma-0">
              Aantal wins: {{ result ? result["AI 2"]["total wins"] : null }}
            </p>
          </v-flex>
        </v-layout>
      </v-card>

      <v-progress-linear
        class="my-3"
        color="accent"
        indeterminate
        v-if="isLoading"
      ></v-progress-linear>

      <v-card-actions class="justify-center">
        <v-btn
          class="accent"
          :disabled="strategyAI1 == '' || strategyAI2 == '' || numberGames < 1 || isLoading"
          @click="simulate"
          >Simuleer</v-btn
        >
        <v-btn class="error" @click="cancel">Annuleer</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "simulationModal",
  props: {
    onCancel: Function,
  },
  data() {
    return {
      numberGames: 0,
      strategyAI1: "",
      strategyAI2: "",
      result: null,
      isLoading: false,
    };
  },
  methods: {
    simulate() {
      this.isLoading = true;
      axios
        .get(
          `http://127.0.0.1:5000/simulate?games=${this.numberGames}&strat1=${this.strategyAI1}&strat2=${this.strategyAI2}`
        )
        .then((res) => {
          this.result = res.data;
          this.isLoading = false;
        });
    },
    cancel() {
      this.numberGames = 0;
      this.strategyAI1 = "";
      this.strategyAI2 = "";
      this.result = null;
      this.isLoading = false;
      this.onCancel();
    },
  },
};
</script>

<style>
</style>