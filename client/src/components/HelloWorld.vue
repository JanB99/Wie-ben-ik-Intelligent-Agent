<template>
  <div class="hello">
    <h1>{{ player }}</h1>
    <div>
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
          {{ index }} {{ char[char.length - 1] }}
        </button>
      </ul>
    </div>

    <div>
      <ul v-for="(char, index) in data" :key="index">
        {{index + char[char.length - 1]}}
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
        });
      this.getAllCharacters()
    },
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
