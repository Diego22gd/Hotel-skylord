<template>
  <div>
    <h1>Habitaciones Disponibles</h1>
    <ul>
      <li v-for="room in rooms" :key="room.id">
        {{ room.name }} - {{ room.price }} $
        <router-link :to="'/booking?room=' + room.id">Reservar</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rooms: [
        { id: 1, name: "Estándar", price: 50 },
        { id: 2, name: "Deluxe", price: 100 },
        { id: 3, name: "Suite", price: 150 }
      ]
    }
  }
}
</script>
