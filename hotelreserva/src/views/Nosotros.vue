<!-- src/views/Nosotros.vue -->
<template>
  <div class="nosotros">
    <h1>Nosotros</h1>
    
    <div class="hotel-info">
      <h2>Nuestra Historia</h2>
      <p>
        Fundado en 1995, el Hotel Skylord se ha convertido en un símbolo de elegancia y confort en la ciudad. Con una vista impresionante del horizonte urbano, nuestro hotel ha sido el lugar elegido por viajeros de todo el mundo. Desde nuestros inicios, hemos mantenido un compromiso inquebrantable con la calidad y el servicio al cliente, ofreciendo experiencias inolvidables a cada huésped.
      </p>

      <h2>Eventos Especiales</h2>
      <p>
        A lo largo de los años, el Hotel Skylord ha sido sede de numerosos eventos importantes, incluyendo conferencias internacionales, bodas de lujo y celebraciones privadas. Nuestro equipo de eventos está dedicado a ayudar a nuestros clientes a planificar y ejecutar cada detalle, asegurando que cada evento sea un éxito rotundo. Algunos de los eventos destacados incluyen:
      </p>
      <ul>
        <li>Conferencia Anual de Innovación Tecnológica - 2023</li>
        <li>Feria Gastronómica Internacional - 2022</li>
        <li>Boda Real de la Familia Pérez - 2021</li>
      </ul>

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
</style>

