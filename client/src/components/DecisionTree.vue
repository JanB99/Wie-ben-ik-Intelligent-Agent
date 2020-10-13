<template>
  <div class="DecisionTree">
    <v-container class="blue">
      <!-- <v-img src="../assets/logo.png" /> -->
      <v-card> 
          
      </v-card>
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
      decisions: [true, false, true, true],
    };
  },

  created() {
    this.getTree();
  },

  methods: {
    getTree() {
      axios.get(`http://127.0.0.1:5000/tree?compact=1`).then((res) => {
        this.data = res.data;
        console.log(this.data);
      });
    },
  },
};
</script>