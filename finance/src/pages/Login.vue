<!-- src/pages/Login.vue -->

<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username or Email:</label>
        <input
            type="text"
            v-model="username"
            id="username"
            required
            placeholder="Enter your username or email"
        />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input
            type="password"
            v-model="password"
            id="password"
            required
            placeholder="Enter your password"
        />
      </div>
      <button type="submit" class="btn">Login</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      error: '',
    };
  },
  methods: {
    async handleLogin() {
      try {
        await this.$store.dispatch('auth/login', {
          username: this.username,
          password: this.password,
        });
        this.$router.push('/home');
      } catch (error) {
        this.error = 'Invalid credentials. Please try again.';
      }
    },
  },
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: auto;
  padding-top: 100px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

.btn {
  width: 100%;
  padding: 10px;
  cursor: pointer;
}

.error {
  color: red;
  margin-top: 10px;
  text-align: center;
}
</style>
