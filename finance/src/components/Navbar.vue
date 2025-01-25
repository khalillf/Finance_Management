<!-- src/components/Navbar.vue -->

<template>
  <nav class="navbar">
    <router-link to="/" class="logo">FinanceApp</router-link>
    <div class="nav-links">
      <router-link v-if="!isAuthenticated" to="/login">Login</router-link>
      <router-link v-if="!isAuthenticated" to="/register">Register</router-link>
      <router-link v-if="isAuthenticated" to="/home">Home</router-link>
      <button v-if="isAuthenticated" @click="handleLogout">Logout</button>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  computed: {
    isAuthenticated() {
      return this.$store.getters['auth/isAuthenticated'];
    },
  },
  methods: {
    async handleLogout() {
      try {
        await this.$store.dispatch('auth/logout');
        this.$router.push('/');
      } catch (error) {
        console.error('Logout failed:', error);
      }
    },
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #2c3e50;
  padding: 15px 30px;
}

.logo {
  color: #ecf0f1;
  font-size: 24px;
  text-decoration: none;
}

.nav-links a {
  color: #ecf0f1;
  margin-right: 15px;
  text-decoration: none;
}

.nav-links button {
  background: none;
  border: none;
  color: #ecf0f1;
  cursor: pointer;
  font-size: 16px;
}
</style>
