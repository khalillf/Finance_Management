// src/main.js

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

const app = createApp(App);

// Set Axios defaults
axios.defaults.baseURL = 'http://localhost:8000/'; // Adjust if your backend is hosted elsewhere
const token = localStorage.getItem('token');
if (token) {
    axios.defaults.headers.common['Authorization'] = `Token ${token}`;
    store.dispatch('auth/fetchUser');
}

app.use(store);
app.use(router);
app.mount('#app');
