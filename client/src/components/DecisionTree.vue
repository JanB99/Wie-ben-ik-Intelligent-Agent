<template>
  <div class="DecisionTree">
    <v-container>
      <v-layout column justify-center>
        <v-flex
          shrink
          v-for="(awnser, index) in decisions"
          v-bind:key="index"
          md5
        >
          <v-layout class="d-flex justify-center">
            <v-card
              v-if="index == 0"
              outline
              block
              class="secondary text-center white--text text--lighten-5 mx-5 pa-2"
              column
            >
              <b>{{ getQuestion(index) }}</b>
            </v-card>
          </v-layout>

          <div v-if="index != 0" column>
            <v-layout class="d-flex justify-center">
              <v-card
                v-if="decisions[index - 1] == true"
                outline
                block
                class="secondary text-center white--text text--lighten-5 mx-5 pa-2"
                column
              >
                <b>{{ getQuestion(index) }}</b>
              </v-card>
            </v-layout>

            <v-layout class="d-flex justify-center">
              <v-card
                v-if="decisions[index - 1] == false"
                outline
                block
                class="secondary text-center white--text text--lighten-5 mx-5 pa-2"
                column
              >
                <b>{{ getQuestion(index) }}</b>
              </v-card>
            </v-layout>
          </div>

          <div class="d-flex justify-center mt-1 mb-3" column>
            <v-card
              outline
              block
              class="text-center white--text text--lighten-5 mx-2 pa-2"
              :class="awnser ? 'accent' : 'secondary'"
              column
            >
              <b>True</b>
            </v-card>
            <v-card
              outline
              block
              class="text-center white--text text--lighten-5 mx-2 pa-2"
              :class="!awnser ? 'accent' : 'secondary'"
              column
            >
              <b>False</b>
            </v-card>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "DecisionTree",
  data() {
    return {
      data: null,
      decisions: [true, false, true, false, true],
    };
  },

  created() {
    this.getTree();
  },

  methods: {
    getQuestion(depth) {
      let temp = this.data;
      let question;

      for (let index = 0; index <= depth; index++) {
        if (temp.question) {
          question = temp.question;
          if (this.decisions[index] == true) {
            temp = temp.true_branch;
          }
          if (this.decisions[index] == false) {
            temp = temp.false_branch;
          }
        } else {
          return temp.prob
        }
      }
      return question;
    },

    getTree() {
      axios.get(`http://127.0.0.1:5000/tree?compact=1`).then((res) => {
        this.data = res.data;
        console.log(this.data);
      });
    },
  },
};
</script>

<style scoped>
.scroll {
  overflow-y: scroll;
}
</style>