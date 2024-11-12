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
    <a @click.prevent="openRegisterModal">Registrarse</a>
    </div>

   <!-- Modal para Registrarse -->
   <div v-if="showRegisterModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeRegisterModal">&times;</span>
        <h2>Registrarse</h2>
        <form @submit.prevent="handleRegister">
          <div class="form-group">
            <label for="firstName">Nombre:</label>
            <input type="text" id="firstName" v-model="firstName" required />
          </div>
          <div class="form-group">
            <label for="lastName">Apellido:</label>
            <input type="text" id="lastName" v-model="lastName" required />
          </div>
          <div class="form-group">
            <label for="registerEmail">Correo Electrónico:</label>
            <input type="email" id="registerEmail" v-model="registerEmail" required />
          </div>
          <div class="form-group">
            <label for="registerPassword">Contraseña:</label>
            <input type="password" id="registerPassword" v-model="registerPassword" required />
          </div>
          <div class="form-group">
            <label for="phoneNumber">Número de Teléfono:</label>
            <input type="text" id="phoneNumber" v-model="phoneNumber" required />
          </div>
          <div class="form-group">
            <label for="age">Edad:</label>
            <input type="number" id="age" v-model="age" min="1" required />
          </div>
          <div class="form-group">
            <label for="idNumber">Cédula:</label>
            <input type="text" id="idNumber" v-model="idNumber" required />
          </div>
          <button type="submit">Registrarse</button>
        </form>
      </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
      showRegisterModal: false,
      firstName: '',
      lastName: '',
      registerEmail: '',
      registerPassword: '',
      phoneNumber: '',
      age: null,
      idNumber: '',
      errorMessage: ''
    
    };
  },
  methods: {
    openRegisterModal() {
      this.showRegisterModal = true;
    },
    closeRegisterModal() {
      this.showRegisterModal = false;
      this.clearRegisterFields();
    },
    handleRegister() {
      alert(`Registrando usuario: ${this.firstName} ${this.lastName}`);
      // Aquí puedes agregar la lógica para el registro.
      this.closeRegisterModal();
    },
    clearRegisterFields() {
      this.firstName = '';
      this.lastName = '';
      this.registerEmail = '';
      this.registerPassword = '';
      this.phoneNumber = '';
      this.age = null;
      this.idNumber = '';
    },

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
.modal {
  position: fixed; /* Fija el modal en la pantalla */
  top: 50%; /* Centra verticalmente */
  left: 50%; /* Centra horizontalmente */
  transform: translate(-50%, -50%); /* Ajusta el centro */
  width: 100%; /* Ajusta el ancho al 100% del viewport */
  height: 100%; /* Ajusta la altura al 100% del viewport */
  background: rgba(0, 0, 0, 0.5); /* Fondo semitransparente */
  display: flex; /* Usa flexbox para centrar contenido */
  align-items: center; /* Centra verticalmente el contenido */
  justify-content: center; /* Centra horizontalmente el contenido */
  z-index: 1000; /* Asegura que esté sobre otros elementos */
}

.modal-content {
  background: #fff; /* Fondo blanco para el contenido */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  width: 90%; /* Ancho adaptable */
  max-width: 400px; /* Ancho máximo */
  max-height: 90%; /* Altura máxima */
  overflow-y: auto; /* Permite scroll si el contenido es demasiado grande */
  position: relative; /* Necesario para posicionar el botón de cierre */
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 1.5rem;
  cursor: pointer;
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

  