import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            dark: { 
                primary: '#a7d9ed', 
                secondary: '#80cbde', 
                accent: '#0f7593', 
            },
            light: {
                primary: '#a7d9ed', 
                secondary: '#80cbde', 
                accent: '#0f7593', 
            }
        }
    }
});