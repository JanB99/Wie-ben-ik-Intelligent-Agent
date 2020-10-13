<template>
  <div class="character">
    <v-container> 
        <v-img max-width="160" :src="getImage(id)"/>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Character",
  data() {
    return {
      // get from other components
      id: 16,
    };
  },

  methods: {
    getImage(id) {
      return `http://127.0.0.1:5000/images?id=${id}`;
    }
  }
};
</script>