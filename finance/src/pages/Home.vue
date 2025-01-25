<!-- src/pages/Home.vue -->

<template>
  <div class="home">
    <h2>Home Page</h2>
    <div class="user-info">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Phone Number:</strong> {{ user.phone_number }}</p>
      <p v-if="user.profile_picture"><strong>Profile Picture:</strong></p>
      <img v-if="user.profile_picture" :src="user.profile_picture" alt="Profile Picture" />
    </div>
    <button @click="handleLogout" class="btn">Logout</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  computed: {
    user() {
      return this.$store.getters['auth/user'];
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
.home {
  max-width: 600px;
  margin: auto;
  padding-top: 50px;
  text-align: center;
}

.user-info {
  text-align: left;
  margin-bottom: 30px;
}

.btn {
  padding: 10px 20px;
  cursor: pointer;
}

img {
  max-width: 150px;
  margin-top: 10px;
}
</style>
