// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import Welcome from '../pages/Welcome.vue';
import Login from '../pages/Login.vue';
import Register from '../pages/Register.vue';
import Home from '../pages/Home.vue';
import store from '../store';

const routes = [
    {
        path: '/',
        name: 'Welcome',
        component: Welcome,
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: { requiresGuest: true },
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
        meta: { requiresGuest: true },
    },
    {
        path: '/home',
        name: 'Home',
        component: Home,
        meta: { requiresAuth: true },
    },
    // Redirect any unknown routes to Welcome
    {
        path: '/:pathMatch(.*)*',
        redirect: '/',
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

// Navigation Guards
router.beforeEach((to, from, next) => {
    const isAuthenticated = store.getters['auth/isAuthenticated'];

    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (!isAuthenticated) {
            next('/login');
        } else {
            next();
        }
    } else if (to.matched.some((record) => record.meta.requiresGuest)) {
        if (isAuthenticated) {
            next('/home');
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router;
