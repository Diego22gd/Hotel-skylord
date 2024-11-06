<!-- App.vue -->
<template>
    <div id="app">
      <header class="header">
        <nav class="navbar">
          <div class="navbar-left">
            <h1 class="hotel-name">Hotel Skylord</h1>
          </div>
          <div class="navbar-right">
            <ul class="nav-links">
              <li><router-link to="/">Inicio</router-link></li>
              <li><router-link to="/nosotros">Nosotros</router-link></li>
              <li><router-link to="/reservas">Reservas</router-link></li>
              
            </ul>
          </div>
        </nav>
      </header>
      <!-- Aquí renderizamos la vista actual según la ruta -->
      <router-view></router-view>
    </div>
  </template>
  
  <script>
  export default {
    name: "App",
  };
  </script>
  
  <style>
  /* Puedes mover el CSS del header aquí o mantenerlo en un archivo separado */
  body{
    margin: 0;
  }
  .header {
    background-color: #333;
    color: white;
    padding: 1rem;
    
  }
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
  }
  .nav-links {
    list-style: none;
    display: flex;
    gap: 1rem;
  }
  .nav-links li {
    display: inline;
  }
  .nav-links a {
    color: white;
    text-decoration: none;
  }

  </style>
  

