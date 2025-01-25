// src/store/index.js

import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
    modules: {
        auth: {
            namespaced: true,
            state: () => ({
                token: localStorage.getItem('token') || '',
                user: {},
            }),
            getters: {
                isAuthenticated: (state) => !!state.token,
                user: (state) => state.user,
            },
            mutations: {
                SET_TOKEN(state, token) {
                    state.token = token;
                },
                SET_USER(state, user) {
                    state.user = user;
                },
                CLEAR_AUTH(state) {
                    state.token = '';
                    state.user = {};
                },
            },
            actions: {
                async register({ commit }, userData) {
                    try {
                        const response = await axios.post('http://localhost:8000/api/users/register/', userData);
                        const token = response.data.token;
                        localStorage.setItem('token', token);
                        axios.defaults.headers.common['Authorization'] = `Token ${token}`;
                        commit('SET_TOKEN', token);
                        commit('SET_USER', response.data.user);
                        return response;
                    } catch (error) {
                        console.error(error);
                        throw error;
                    }
                },
                async login({ commit }, credentials) {
                    try {
                        const response = await axios.post('http://localhost:8000/api/users/login/', credentials);
                        const token = response.data.token;
                        localStorage.setItem('token', token);
                        axios.defaults.headers.common['Authorization'] = `Token ${token}`;
                        commit('SET_TOKEN', token);
                        // Fetch user data after login
                        const userResponse = await axios.get('http://localhost:8000/api/users/profile/');
                        commit('SET_USER', userResponse.data);
                        return response;
                    } catch (error) {
                        console.error(error);
                        throw error;
                    }
                },
                async logout({ commit }) {
                    try {
                        await axios.post('http://localhost:8000/api/users/logout/');
                        commit('CLEAR_AUTH');
                        localStorage.removeItem('token');
                        delete axios.defaults.headers.common['Authorization'];
                    } catch (error) {
                        console.error(error);
                        throw error;
                    }
                },
                async fetchUser({ commit }) {
                    try {
                        const response = await axios.get('http://localhost:8000/api/users/profile/');
                        commit('SET_USER', response.data);
                        return response;
                    } catch (error) {
                        console.error(error);
                        throw error;
                    }
                },
            },
        },
    },
});

export default store;
