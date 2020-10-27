<template>
  <div class="AI">
    <v-card outlined v-if="!answer" rounded class="ma-2 pa-6 elevation-10 secondary">
      <v-layout column justify-space-around>
        <v-flex class="text-center">
          <h2 class="white--text">{{ question }}</h2>
        </v-flex>

        <v-flex justify-center class="text-center">
          <v-btn
            class="ma-2 accent font-weight-bold"
            @click="postAiQuestion(1)"
            >Ja</v-btn
          >
          <v-btn
            class="ma-2 accent font-weight-bold"
            @click="postAiQuestion(0)"
            >Nee</v-btn
          >
        </v-flex>
      </v-layout>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  props: {
    onTurnEnd: Function,
    player: Array,
    onAIWin: Function,
  },
  data() {
    return {
      question: null,
      answer: null,
    };
  },
  methods: {
    getImage(id) {
      return `http://127.0.0.1:5000/images?id=${id}`;
    },
    getAiQuestion() {
      axios.get(`http://127.0.0.1:5000/aiquestion`).then((res) => {
        // console.log(res.data)
        if (res.data.type) {
          this.answer = res.data.prob;
          // this.onAIWin(this.answer)
          this.onAIWin(this.answer);
        } else {
          this.question = res.data.question;
        }
      });
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
          this.onTurnEnd();
        });
    },
  },
  created() {
    this.getAiQuestion();
  },
};
</script>