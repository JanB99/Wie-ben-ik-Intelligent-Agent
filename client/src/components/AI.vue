<template>
  <div class="AI">
    <v-container class="ma-2 pa-6 primary elevation-10" rounded outlined>
      <v-layout row>
        <v-flex md3 class="d-flex align-center justify-center">
          <Character />
        </v-flex>
        <v-flex md3 class="d-flex align-center justify-center">
          <Question />
        </v-flex>
        <v-flex md6 class="pa-2">
          <DecisionTree />
          <v-btn @click="onTurnEnd">test to next turn</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import Character from "./Character";
import Question from "./Question";
// import DecisionTree from "./DecisionTree";

export default {
  name: "App",

  components: {
    Character,
    Question,
    DecisionTree,
  },
  props: {
    onTurnEnd: Function,
  }
};
</script>