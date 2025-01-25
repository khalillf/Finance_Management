<!-- src/pages/Welcome.vue -->

<template>
  <div class="welcome">
    <h1>Welcome to Finance Management App</h1>
    <div class="buttons">
      <router-link to="/login">
        <button class="btn">Login</button>
      </router-link>
      <router-link to="/register">
        <button class="btn">Register</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
};
</script>

<style scoped>
.welcome {
  text-align: center;
  margin-top: 100px;
}

.buttons {
  margin-top: 30px;
}

.btn {
  margin: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
