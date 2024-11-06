<template>
    <div class="home">
      <!-- Header con barra de navegación -->
      <header class="header">
        
        <div class="hero">
  
          <h2 class="hero-title">HOTEL SKYLORD</h2>
        </div>
      </header>
  
      <!-- Cuerpo de la página con información del hotel -->
      <section class="info">
        <h2>Bienvenidos al Hotel Skylord</h2>
        <p>
            Estamos encantados de recibirte en nuestra página web, donde comienza tu experiencia inolvidable en el Hotel Skylord, un lugar diseñado para ofrecerte el máximo confort y lujo en cada detalle. Ya sea que nos visites por negocios, para una escapada romántica, o simplemente para relajarte, nuestro hotel combina elegancia moderna con un servicio de clase mundial, garantizando una estadía que superarás tus expectativas.¡Reserva ahora y vive la experiencia
          Maravilla!
        </p>
      </section>
      <div class="rooms-carousel">
        <div class="room" v-for="(room, index) in rooms" :key="index" v-show="currentRoom === index">
          <!-- Contenedor de la imagen y descripción -->
          <div class="room-content">
            <img :src="room.image" :alt="room.name" class="room-image" />
            <div class="room-details">
              <h2>{{ room.name }}</h2>
              <p>{{ room.description }}</p>
              
            </div>
          </div>
        </div>
  
        <!-- Puntos de navegación -->
        <div class="dots">
          <span v-for="(room, index) in rooms" :key="index" @click="currentRoom = index"
            :class="{ active: currentRoom === index }"></span>
        </div>
    </div>
    <div class="galeria">
        <div class="gallery">
      <!-- Botón para retroceder -->
      <button @click="prev" class="arrow left-arrow">&lt;</button>
      
      <!-- Contenedor de imágenes visibles (tres a la vez) -->
      <div class="gallery-container">
        <div class="gallery-wrapper" :style="galleryStyle">
          <div v-for="(image, index) in images" :key="index" class="gallery-item">
            <img :src="image.src" :alt="image.alt">
          </div>
        </div>
      </div>
      
      <!-- Botón para avanzar -->
      <button @click="next" class="arrow right-arrow">&gt;</button>
    </div>
    </div>
        <div class="informacion">
         <h1>INFORMACION</h1>
         <div class="information">
          
          <div class="contacto">
          <h3>Contacto para reservas</h3>
          <ol class="lista">
              
            <p>WhatsApp Reservas (Recepción): (+58) 0414-4011273</p>
            <p>WhatsApp Reservas 2: (+58) 0424-4116268</p>
          <p>email para reservas:d.valdemar16@gmail.com</p>
          </ol>
        </div>
        <div class="direccion">
            <h3>Direccion</h3>
            <p class="tdirection"> Av. Salvador Feo la Cruz, Naguanagua, Carabobo</p>
        </div>
        </div>
        </div>
  
      </div>
  <router-view /> 
    
  
  </template>
  
  
  <script>
 import roomImage1 from '@/assets/individual.jpg';
import roomImage2 from '@/assets/doble.jpg';
import roomImage3 from '@/assets/deluxe.jpg';

// Importación de imágenes de la galería del hotel
import hotel1 from '@/assets/hotel1.jpg';
import hotel2 from '@/assets/hotel2.jpg';
import hotel3 from '@/assets/hotel3.jpg';
import hotel4 from '@/assets/hotel4.jpg';
import hotel5 from '@/assets/hotel5.jpg';
import hotel6 from '@/assets/hotel6.jpeg';
import hotel7 from '@/assets/hotel7.jpeg';
import hotel8 from '@/assets/hotel8.jpg';
import hotel9 from '@/assets/hotel9.jpg';
import hotel10 from '@/assets/hotel10.jpeg';

export default {
  data() {
    return {
      // Lista de habitaciones con nombres, descripciones e imágenes importadas
      rooms: [
        { 
          name: 'Habitación Simple', 
          description: 'Ofrece un espacio excepcional donde la elegancia y el confort están presentes, dispone de una sala de estar para una reunión de negocios, en donde podrá relajarse y disfrutar de las vistas de la ciudad. Esta habitación cuenta con una variedad de servicios para que se sienta como en casa, incluido el acceso a Wi-Fi, minibar, caja fuerte electrónica, televisión LCD de alta definición y un lujoso baño con ducha de hidromasaje, secador de cabello profesional y amenidades de lujo, además de una bata de baño y pantuflas.', 
          image: roomImage1 
        },
        { 
          name: 'Habitación Doble', 
          description: 'Las habitación triple ofrece un espacio excepcional donde la elegancia y el confort están presentes. Dispone de dos ambientes, uno con una cama king y otro con una cama individual. Esta habitación cuenta con una variedad de servicios para que se sienta como en casa, incluido el acceso a Wi-Fi, minibar, caja fuerte electrónica, televisión LCD de alta definición y un lujoso baño con ducha de hidromasaje, secador de cabello profesional y amenidades de lujo, además de una bata de baño y pantuflas', 
          image: roomImage2 
        },
        { 
          name: 'Suite Deluxe', 
          description: 'Ubicadas en un ala especial del hotel, las habitaciones Deluxe (Cama King) disponen de un área de 33 m². con grandes ventanales y excelentes vistas con una acertada combinación de colores cálidos y un estilo moderno que crean un ambiente acogedor en su estancia. Las habitaciones disponen de acceso Wi-Fi a Internet, minibar, caja fuerte electrónica, televisión LCD de alta definición y un lujoso baño con ducha de hidromasaje, secador de cabello profesional y amenidades de lujo.', 
          image: roomImage3 
        }
      ],

      // Lista de imágenes para la galería
      images: [
        { src: hotel1, alt: 'Imagen 1 del hotel' },
        { src: hotel2, alt: 'Imagen 2 del hotel' },
        { src: hotel3, alt: 'Imagen 3 del hotel' },
        { src: hotel4, alt: 'Imagen 4 del hotel' },
        { src: hotel5, alt: 'Imagen 5 del hotel' },
        { src: hotel6, alt: 'Imagen 6 del hotel' },
        { src: hotel7, alt: 'Imagen 7 del hotel' },
        { src: hotel8, alt: 'Imagen 8 del hotel' },
        { src: hotel9, alt: 'Imagen 9 del hotel' },
        { src: hotel10, alt: 'Imagen 10 del hotel'},
      ],

      currentRoom: 0,  // Controla la habitación actual mostrada en el carrusel
      currentIndex: 0  // Controla el índice de la primera imagen visible en la galería
    };
  },
  methods: {
    reserveRoom(room) {
      alert(`Has seleccionado reservar: ${room.name}`);
    },
    next() {
      if (this.currentIndex < this.images.length - 3) {
        this.currentIndex++;
      }
    },
    prev() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
      }
    }
  },
  computed: {
    // Estilo dinámico para desplazar las imágenes en la galería
    galleryStyle() {
      return {
        transform: `translateX(-${this.currentIndex * 100 / 3}%)`
      };
    }
  }
};

  
  </script>


<style scoped>
template{
  font-family: 'Roboto', sans-serif;
}
.home {
  font-family: 'Roboto', sans-serif;
  
}

/* Estilos del header */
.header {
  position: relative;
  height: 80vh;
  background-image: url('@/assets/hotel.webp'); /* Aquí va la imagen del hotel */
  background-position: center center;
  background-size: cover;
  color: rgb(247, 247, 247);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  
}
.header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.1); /* Capa oscura con 50% de opacidad */
  z-index: 1; /* Se asegura que la capa esté encima de la imagen de fondo */
}

/* Barra de navegación */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: rgba(39, 79, 117, 0.5); /* Fondo oscuro semi-transparente */
}

.hotel-name {
  margin: 0;
  font-size: 2.5em;
  font-style: italic;
}

.nav-links {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
  font-style: italic;
}

.nav-links li {
  margin-left: 20px;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1em;
}

.nav-links a:hover {
  text-decoration: underline;
}

/* Hero (Imagen de fondo y nombre del hotel centrado) */
.hero {
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
 
}

.hero-title {
  font-size: 4em;
  font-weight: bold;
  font-style: italic;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
}

/* Sección de información del hotel */
.info {
  padding: 40px 20px;
  text-align: center;
  background: #051c2d;
  color: #000000;
  height: 20rem;
  background-color: #ffffff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  margin: 20px;
  font-family: 'Roboto', sans-serif;
}

.info h2 {
  font-size: 2.5em;
  margin-bottom: 20px;
}

.info p {
  font-size: 1.2em;
  line-height: 1.6;
}
.rooms-carousel {
  text-align: center;
  margin-top: 0px;
  padding-bottom: 2rem;
  padding-top: 2rem;
  background: #dfe5e9;
}

.room-content {
  display: flex; /* Coloca la imagen y el contenido en línea */
  align-items: center;
  justify-content: center;
  font-family: 'Roboto', sans-serif;

}

.room-image {
  width: 350px;  /* Ajusta el tamaño de la imagen */
  height: auto;
  margin-right: 20px; 
  margin-left: 10px;/* Espacio entre la imagen y la descripción */
}

.room-details {
  text-align: left; /* Alinea el texto a la izquierda */
}

.room h2 {
  font-size: 20px;
  margin-bottom: 10px;
  text-align: center;
}

.room p {
  font-size: 20px;
  margin-bottom: 20px;
}

.room button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin-left: 29rem;
  

}
.room[v-show="true"] {
  display: block;
}

/* Estilos para los puntos de navegación */
.dots {
  margin-top: 50px;
  align-items: center;
  
}

.dots span {
  height: 15px;
  width: 15px;
  margin: 0 5px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  cursor: pointer;
  transition: background-color 0.3s;
}

.dots span.active {
  background-color: #717171;
}
.gallery {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 90%;
  margin: 20px auto;
  background-color: #051c2d;
  
}

.gallery-container {
  width: 100%; /* El contenedor mostrará tres imágenes */
  overflow: hidden;
  height: 50%;
  background-color: #ffffff;
  
 
}
.galeria{
    background-color: #051c2d;
    margin-top: -8px;
    padding-top: 1rem;
    padding-bottom: 1rem;
    background-color: #ffffff;
  
}
.gallery-wrapper {
  display: flex;
  transition: transform 0.3s ease-in-out;
  width: calc(100% * (4 / 3)); /* Ajustar el ancho en función del número total de imágenes */
}

.gallery-item {
  flex: 0 0 33.33%; /* Tres imágenes visibles al mismo tiempo */
  padding: 0 10px;
}

.gallery-item img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.arrow {
  background-color: rgba(0, 0, 0, 0.5);
  border: none;
  color: white;
  padding: 10px;
  cursor: pointer;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
}

.left-arrow {
  left: 10px;
}

.right-arrow {
  right: 10px;
}

.arrow:hover {
  background-color: rgba(0, 0, 0, 0.8);
}
.information{
    display: flex;
    flex-direction: row;
    gap: 3.5rem;
    justify-content: center;
    padding-bottom: 4rem;
    background: #dfe5e9;
    font-family: 'Roboto', sans-serif;
    
}
.informacion{
     align-items: center;
    background: #dfe5e9;
    text-align: center;
    padding-top: 1rem;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  margin: 20px;
  font-family: 'Roboto', sans-serif;
   
}
.lista{
    font-size: 1.5rem;
}
.tdirection{
   font-size: 25px;
}
.nav-links li {
  cursor: default;  /* Esto desactiva el puntero del ratón para los enlaces */
  text-decoration: none;  /* Puede quitar el subrayado del enlace */
  color: inherit;  /* El color del enlace podría hacer que parezca texto común */
}
.nav-links li {
  list-style: none;  /* Remueve el punto de lista */
}




</style>

