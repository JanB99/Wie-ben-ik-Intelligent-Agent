<template>
  <div class="Question">
    <v-container class="d-flex justify-center" row>
      <v-card class="pa-3 ma-5 secondary white--text text--lighten-5"
        ><b> {{ question }} </b></v-card>
      <div justify-center>
        <v-btn class="ma-2 secondary" @click="postAiQuestion(1)"
          ><b> Ja </b></v-btn>
        <v-btn class="ma-2 secondary" @click="postAiQuestion(0)"
          ><b> Nee </b></v-btn>
      </div>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Question",
  data() {
    return {
      playerIndex: 16,
      //format question
      question: null,
      awnser: null,
    };
  },

  created() {
    // this.setCharacter(this.playerIndex);
    this.getAiQuestion();
  },

  methods: {
    getAiQuestion() {
      axios.get(`http://127.0.0.1:5000/aiquestion`).then((res) => {
        this.question = res.data.question;
      });
    },
    setCharacter(index) {
      axios.get(`http://127.0.0.1:5000/character?num=${index}`);
    },
    postAiQuestion(answer) {
      axios
        .get(`http://127.0.0.1:5000/aiquestion?answer=${answer}`)
        .then((res) => {
          if (res.data.type) {
            this.answer = res.data.prob;
          } else {
            this.question = res.data.question;
          }
        });
    },
  },
};
</script>
