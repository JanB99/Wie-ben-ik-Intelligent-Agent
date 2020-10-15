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
          <!-- Start question -->
          <v-layout class="d-flex flex-column" v-if="index == 0">
            <!-- Question -->
            <v-layout class="d-flex justify-center">
              <v-col cols="8" class="flex-grow-0 flex-shrink-0">
                <v-card
                  class="secondary text-center white--text text--lighten-5 pa-2"
                  column
                >
                  <b>{{ getQuestion(index) }}</b>
                </v-card>
              </v-col>
            </v-layout>

            <!-- True or False -->
            <v-layout class="d-flex justify-space-around pa-2 row">
              <v-card
                class="text-center white--text text--lighten-5 mx-2 pa-2"
                :class="awnser ? 'accent' : 'secondary'"
                column
              >
                <b>Ja</b>
              </v-card>
              <v-card
                class="text-center white--text text--lighten-5 mx-2 pa-2"
                :class="!awnser ? 'accent' : 'secondary'"
                column
              >
                <b>Nee</b>
              </v-card>
            </v-layout>
          </v-layout>

          <!-- Next questions -->
          <v-layout v-if="index != 0">
            <!-- True side -->
            <v-layout class="d-flex column align-center mt-2">
              <!-- Questions -->
              <v-col cols="8" class="flex-grow-0 flex-shrink-0">
                <v-card
                  align-start
                  class="text-center white--text text--lighten-5 mx-2 pa-2"
                  :class="awnser == true ? 'secondary' : 'grey'"
                  column
                >
                  <b>{{ getQuestion(index, true) }}</b>
                </v-card>
              </v-col>

              <!-- Awnsers -->
              <v-layout class="justify-center pa-2">
                <!-- True -->
                <v-card
                  class="text-center white--text text--lighten-5 mx-2 pa-2"
                  :class="awnser ? 'accent' : 'secondary'"
                  column
                >
                  <b>Ja</b>
                </v-card>
              </v-layout>
            </v-layout>

            <!-- False side -->
            <v-layout class="d-flex column align-center mt-2">
              <!-- Questions -->
              <v-col cols="8" class="flex-grow-0 flex-shrink-0">
                <v-card
                  block
                  class="text-center white--text text--lighten-5 mx-2 pa-2"
                  :class="awnser == false ? 'secondary' : 'grey'"
                  column
                >
                  <b>{{ getQuestion(index, false) }}</b>
                </v-card>
              </v-col>

              <!-- Awnsers -->
              <v-layout class="justify-center pa-2">
                <!-- True -->
                <v-card
                  class="text-center white--text text--lighten-5 mx-2 pa-2"
                  :class="!awnser ? 'accent' : 'secondary'"
                  column
                >
                  <b>Nee</b>
                </v-card>
              </v-layout>
            </v-layout>
          </v-layout>
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
      decisions: [false, false, true, true],
    };
  },

  created() {
    this.getTree();
  },

  methods: {
    getQuestion(depth, awnser) {
      let temp = this.data;
      let parent = temp;
      let question = this.data?.question;

      for (let i = 0; i <= depth; i++) {
        if (temp?.question) {
          if (depth == i && this.decisions[i] == awnser) {
            question = temp.question;
          }

          if (depth == i && this.decisions[i] != awnser) {
            if (awnser == true) {
              question = parent.true_branch.question;
              console.log(question, 'is true pik', this.decisions[i], awnser, i);
            }
            if (awnser == false) {
              question = parent.false_branch.question;
              console.log(question, 'is false pik', this.decisions[i], awnser, i);
            }
          }

          parent = temp;

          // If True
          if (this.decisions[i]) {
            temp = temp.true_branch;
          }

          // If False
          if (!this.decisions[i]) {
            temp = temp.false_branch;
          }
        } else {
          return temp?.prob;
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