<template>
  <div class="hello">

    <img src="http://127.0.0.1:5000/image?id=10" >
    <div v-if="turn % 2 == 1">
      <h2>AI vraagt:</h2>
      <h3>{{ aiQuestion ? aiQuestion.question : null }}</h3>
      <button @click="postAiQuestion(1)">True</button>
      <button @click="postAiQuestion(0)">False</button>
    </div>

    <h1>{{ player }}</h1>
    <div v-if="turn % 2 == 0 && player">
      <select v-model="selectedLabel" @change="getValues">
        <option v-for="label in labels" :key="label">
          {{ label }}
        </option>
      </select>
      ==
      <select v-model="selectedValue">
        <option v-for="value in values" :key="value">
          {{ value }}
        </option>
      </select>
      ?
      <button @click="askQuestion" :disabled="selectedValue == ''">
        ask question
      </button>
    </div>

    <div v-if="player == null">
      <ul v-for="(char, index) in data" :key="index">
        <button @click="setCharacter(index)">
          {{ index }} {{ char[char.length - 2] }}
          <img :src="getImage(char[char.length - 1])" />
        </button>
      </ul>
    </div>

    <div>
      <ul v-for="(char, index) in data" :key="index">
        {{
          index + char[char.length - 2]
        }}
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data() {
    return {
      data: null,
      player: null,
      selectedLabel: "",
      selectedValue: "",
      labels: [],
      values: [],
      aiQuestion: null,
      turn: 0
    };
  },
  methods: {
    getAllCharacters() {
      axios.get("http://127.0.0.1:5000/getAllCharacters").then((res) => {
        this.data = res.data;
      });
    },
    setCharacter(index) {
      axios.get(`http://127.0.0.1:5000/character?num=${index}`).then((res) => {
        this.player = res.data;
      });
      this.getAllCharacters();
    },
    getLabels() {
      axios.get("http://127.0.0.1:5000/labels").then((res) => {
        this.labels = res.data;
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
          console.log(res.data);
          this.turn++;
        });
      this.getAllCharacters();
      this.getAiQuestion();
    },
    getAiQuestion() {
      axios.get(`http://127.0.0.1:5000/aiquestion`).then((res) => {
        this.aiQuestion = res.data;
      });
    },
    postAiQuestion(answer) {
      axios
        .get(`http://127.0.0.1:5000/aiquestion?answer=${answer}`)
        .then((res) => {
          console.log(res.data);
          this.aiQuestion = null
          this.turn++;
          this.selectedLabel = ""
          this.selectedValue = ""
          this.values = []
        });
    },
    getImage(id){
      return `http://127.0.0.1:5000/image?id=${id}`
    }
  },
  created() {
    this.getAllCharacters();
    this.getLabels();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
