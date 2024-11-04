<template>
  <div class="titulo">
    <h1 class="nos">iniciar Sesión</h1>
  </div>
  <div class="login">
    
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="email">Correo Electrónico:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Ingresar</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    
    };
  },
  methods: {
    login() {
      // Verifica las credenciales de inicio de sesión
      if (this.username === 'admin' && this.password === '123456') {
        // Guarda la autenticación en localStorage
        localStorage.setItem('isAuthenticated', true);
        this.$router.push({ name: 'Admin' }); // Redirige a la vista de administrador
      } else {
        // Mensaje de error si las credenciales no coinciden
        this.errorMessage = 'Usuario o clave incorrectos.';
      }
    }
  },
    
  
};
</script>

<style scoped>
.login {
  padding: 20px;
  max-width: 400px;
  margin: 0 auto;
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
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.links {
  margin-top: 10px;
}

.modal {
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
}

.close {
  cursor: pointer;
  float: right;
}
.titulo{
  
  position: relative;
  height: 50vh;
  background-image: url('@/assets/hotel.webp'); /* Aquí va la imagen del hotel */
  background-position: center center;
  background-size: cover;
  color: rgb(247, 247, 247);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.titulo {
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  
}

.nos {
  font-size: 4em;
  font-weight: bold;
  font-style: italic;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
}
</style>

  