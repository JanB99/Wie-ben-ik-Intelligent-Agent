<template>
  <div class="AI">
    <v-container>
      <v-card class="primary" elevation="10" outlined rounded>
        <v-layout row>
          <v-flex class="d-flex flex-grow-1 flex-shrink-0 align-center justify-center">
            <Character />
          </v-flex>
          <v-flex class="d-flex flex-grow-1 flex-shrink-0 align-center justify-center">
            <Question />
          </v-flex>
          <v-flex class="d-flex flex-grow-1 flex-shrink-0 align-center justify-center">
            <DecisionTree />
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import Character from "./Character";
import Question from "./Question";
import DecisionTree from "./DecisionTree";

export default {
  name: "App",

  components: {
    Character,
    Question,
    DecisionTree
  },
};
</script>