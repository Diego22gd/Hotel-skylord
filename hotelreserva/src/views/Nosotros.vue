<template>
  <div class="nosotros-page">
    <div class="hero-section">
      <h1 class="hero-title">Nosotros</h1>
    </div>
    <div class="content-section">
      <section class="section historia">
        <h2>Nuestra Historia</h2>
        <p>
          Fundado en 1995, el Hotel Skylord se ha convertido en un símbolo de elegancia y confort en la ciudad. Con una vista impresionante del horizonte urbano, nuestro hotel ha sido el lugar elegido por viajeros de todo el mundo. Desde nuestros inicios, hemos mantenido un compromiso inquebrantable con la calidad y el servicio al cliente, ofreciendo experiencias inolvidables a cada huésped.
        </p>
      </section>
      <section class="section eventos">
        <h2>Eventos Especiales</h2>
        <p>
          A lo largo de los años, el Hotel Skylord ha sido sede de numerosos eventos importantes, incluyendo conferencias internacionales, bodas de lujo y celebraciones privadas. Nuestro equipo de eventos está dedicado a ayudar a nuestros clientes a planificar y ejecutar cada detalle, asegurando que cada evento sea un éxito rotundo.
        </p>
        <ul class="event-list">
          <li>Conferencia Anual de Innovación Tecnológica - 2023</li>
          <li>Feria Gastronómica Internacional - 2022</li>
          <li>Boda Real de la Familia Pérez - 2021</li>
        </ul>
      </section>
      <section class="section info">
        <h2>Información del Hotel</h2>
        <p>
          El Hotel Skylord ofrece una variedad de comodidades para garantizar una estancia placentera:
        </p>
        <ul class="amenities-list">
          <li>Habitaciones de lujo con vista al mar</li>
          <li>Gimnasio completamente equipado</li>
          <li>Restaurante gourmet con cocina internacional</li>
          <li>Piscina al aire libre con bar</li>
          <li>Servicio de spa y bienestar</li>
        </ul>
        <p>
          Nuestra ubicación estratégica permite fácil acceso a los principales puntos de interés de la ciudad, incluyendo museos, parques y centros comerciales. Ya sea que estés aquí por negocios o placer, el Hotel Skylord es tu mejor opción.
        </p>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Nosotros',
};
</script>

<style scoped>
.nosotros-page {
  font-family: 'Roboto', sans-serif;
  color: #444;
  background-color: #f9f9f9;
  padding: 0;
  margin: 0;
}

.hero-section {
  height: 50vh;
  background-image: url('@/assets/hotel.webp');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  text-align: center;
}

.hero-title {
  font-size: 4em;
  font-weight: 700;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
  margin: 0;
}

.content-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.section {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
}


.section h2 {
  font-size: 2em;
  font-weight: 600;
  color: #333;
  margin-bottom: 20px;
}

.section p {
  font-size: 1.1em;
  color: #555;
  line-height: 1.6;
}

.event-list,
.amenities-list {
  list-style: none;
  padding: 0;
  margin: 20px 0;
}

.event-list li,
.amenities-list li {
  font-size: 1em;
  color: #666;
  padding: 10px;
  border-bottom: 1px solid #eaeaea;
}

.event-list li:last-child,
.amenities-list li:last-child {
  border-bottom: none;
}

.historia {
  background-color: #f2f7fa;
}

.eventos {
  background-color: #e8f5fe;
}

.info {
  background-color: #f2f7fa;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-title {
    font-size: 3em;
  }
  .content-section {
    padding: 20px;
  }
  .section h2 {
    font-size: 1.5em;
  }
}
</style>
