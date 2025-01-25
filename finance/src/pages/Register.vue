<!-- src/pages/Register.vue -->

<template>
  <div class="register">
    <h2>Register</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">Username:</label>
        <input
            type="text"
            v-model="username"
            id="username"
            required
            placeholder="Choose a username"
        />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input
            type="email"
            v-model="email"
            id="email"
            required
            placeholder="Enter your email"
        />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input
            type="password"
            v-model="password"
            id="password"
            required
            placeholder="Create a password"
        />
      </div>
      <div class="form-group">
        <label for="phone_number">Phone Number:</label>
        <input
            type="text"
            v-model="phone_number"
            id="phone_number"
            required
            placeholder="Enter your phone number"
        />
      </div>
      <button type="submit" class="btn">Register</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      phone_number: '',
      error: '',
    };
  },
  methods: {
    async handleRegister() {
      try {
        await this.$store.dispatch('auth/register', {
          username: this.username,
          email: this.email,
          password: this.password,
          phone_number: this.phone_number,
        });
        this.$router.push('/home');
      } catch (error) {
        this.error = 'Registration failed. Please try again.';
      }
    },
  },
};
</script>

<style scoped>
.register {
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
