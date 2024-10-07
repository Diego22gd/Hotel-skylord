<template>
  <div class="login">
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Ingresar</button>
    </form>
    <div class="links">
      <a @click.prevent="openForgotPasswordModal">Olvidé mi Contraseña</a>
      <a @click.prevent="openRegisterModal">Registrarse</a>
    </div>

    <!-- Modal para Olvidé mi Contraseña -->
    <div v-if="showForgotPasswordModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeForgotPasswordModal">&times;</span>
        <h2>Olvidé mi Contraseña</h2>
        <form @submit.prevent="handleForgotPassword">
          <div class="form-group">
            <label for="forgotEmail">Correo Electrónico:</label>
            <input type="email" id="forgotEmail" v-model="forgotEmail" required />
          </div>
          <button type="submit">Enviar</button>
        </form>
      </div>
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      showForgotPasswordModal: false,
      showRegisterModal: false,
      forgotEmail: '',
      firstName: '',
      lastName: '',
      registerEmail: '',
      registerPassword: '',
      phoneNumber: '',
      age: null,
      idNumber: ''
    };
  },
  methods: {
    handleLogin() {
      alert(`Iniciando sesión con: ${this.email}`);
      // Aquí puedes agregar la lógica para el inicio de sesión.
    },
    openForgotPasswordModal() {
      this.showForgotPasswordModal = true;
    },
    closeForgotPasswordModal() {
      this.showForgotPasswordModal = false;
      this.forgotEmail = ''; // Resetear el campo
    },
    handleForgotPassword() {
      alert(`Instrucciones enviadas a: ${this.forgotEmail}`);
      this.closeForgotPasswordModal();
    },
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
    }
  }
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
</style>

  