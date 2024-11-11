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
/* Estilo para el contenedor principal */
.login {
  padding: 20px;
  max-width: 400px;
  margin: 0 auto;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  margin-top: 10px
}

/* Estilos para el título */
.titulo {
  position: relative;
  height: 50vh;
  background-image: url('@/assets/hotel.webp'); /* Imagen de fondo */
  background-position: center center;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  color: rgb(247, 247, 247);
}

.nos {
  font-size: 3em;
  font-weight: bold;
  font-style: italic;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
  text-align: center;
}

/* Estilo para cada grupo del formulario */
.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #333;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1em;
  box-sizing: border-box;
}

/* Botón de enviar */
button {
  width: 100%;
  padding: 12px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1em;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

/* Mensaje de error */
.error-message {
  color: #ff4d4d;
  font-size: 0.9em;
  margin-top: 10px;
  text-align: center;
}

/* Responsividad */
@media (max-width: 768px) {
  .nos {
    font-size: 2.5em;
  }

  .login {
    width: 90%;
    padding: 15px;
  }

  button {
    padding: 10px;
    font-size: 0.9em;
  }
}

@media (max-width: 480px) {
  .nos {
    font-size: 2em;
  }

  .login {
    width: 100%;
    padding: 10px;
  }

  input, button {
    font-size: 0.85em;
  }
}
</style>

  