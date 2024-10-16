<!-- src/views/Nosotros.vue -->
<template>
  <div class="titulo">
    <h1 class="nos">Nosotros</h1>
  </div>
  <div class="nosotros">
  
    
    <div class="hotel-info">
      <div class="historia">
      <h2>Nuestra Historia</h2>
      <p>
        Fundado en 1995, el Hotel Skylord se ha convertido en un símbolo de elegancia y confort en la ciudad. Con una vista impresionante del horizonte urbano, nuestro hotel ha sido el lugar elegido por viajeros de todo el mundo. Desde nuestros inicios, hemos mantenido un compromiso inquebrantable con la calidad y el servicio al cliente, ofreciendo experiencias inolvidables a cada huésped.
      </p>
    </div>
       <div class="eventos">
      <h2>Eventos Especiales</h2>
      <p>
        A lo largo de los años, el Hotel Skylord ha sido sede de numerosos eventos importantes, incluyendo conferencias internacionales, bodas de lujo y celebraciones privadas. Nuestro equipo de eventos está dedicado a ayudar a nuestros clientes a planificar y ejecutar cada detalle, asegurando que cada evento sea un éxito rotundo. Algunos de los eventos destacados incluyen:
      </p>
      <ul>
        <li>Conferencia Anual de Innovación Tecnológica - 2023</li>
        <li>Feria Gastronómica Internacional - 2022</li>
        <li>Boda Real de la Familia Pérez - 2021</li>
      </ul>
    </div>
      <div class="info">
      
        <h2>Información del Hotel</h2>
      <p>
        El Hotel Skylord ofrece una variedad de comodidades para garantizar una estancia placentera:
      </p>
      <ul>
        <li>Habitaciones de lujo con vista al mar</li>
        <li>Gimnasio completamente equipado</li>
        <li>Restaurante gourmet con cocina internacional</li>
        <li>Piscina al aire libre con bar</li>
        <li>Servicio de spa y bienestar</li>
      </ul>
      <p>
        Nuestra ubicación estratégica permite fácil acceso a los principales puntos de interés de la ciudad, incluyendo museos, parques y centros comerciales. Ya sea que estés aquí por negocios o placer, el Hotel Skylord es tu mejor opción.
      </p>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nosotros',
};
</script>

<style scoped>
.nosotros {
  padding: 20px;
}

.hotel-info {
  max-width: 800px;
  margin: 0 auto;
  flex-direction: column;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

h2 {
  margin-top: 20px;
}

ul {
  margin: 10px 0;
  padding-left: 20px;
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
.historia{
  display:flex;
  justify-content: center;
  gap: 1rem;
  background: #287fc1;
  height: 20rem;
  flex-direction: column;
  text-align: center;
  font-size: 20px;
  border-radius: 5%;
  margin: 20px;
  align-self: flex-start; 

}
.nosotros{
  background-color: #08243a;
  display: flex;
  gap: 2rem;
}
.info{
  display:flex;
  justify-content: center;
  gap: 1rem;
  background: #287fc1;
  max-width: 100%;
  flex-direction: column;
  text-align: center;
  font-size: 20px;
  border-radius: 5%;
  margin: 20px;
 

}
.eventos{
  display:flex;
  justify-content: center;
  background: #287fc1;
  height: 20rem;
  flex-direction: column;
  text-align: center;
  font-size: 20px;
  border-radius: 5%;
  margin: 20px;

}

</style>

