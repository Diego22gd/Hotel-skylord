<template>
  <div>
    <h1>Reservación de Habitación</h1>
    <form @submit.prevent="submitBooking">
      <div>
        <label>Nombre</label>
        <input type="text" v-model="name" required />
      </div>
      <div>
        <label>Fecha de Entrada</label>
        <input type="date" v-model="checkInDate" required />
      </div>
      <div>
        <label>Fecha de Salida</label>
        <input type="date" v-model="checkOutDate" required />
      </div>
      <button type="submit">Reservar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      roomId: null,
      name: '',
      checkInDate: '',
      checkOutDate: ''
    }
  },
  mounted() {
    // Obtener ID de la habitación de la URL
    this.roomId = this.$route.query.room;
  },
  methods: {
    submitBooking() {
      // Llamada a la API para enviar la reservación
      axios.post('https://api.hotel.com/reservations', {
        roomId: this.roomId,
        name: this.name,
        checkInDate: this.checkInDate,
        checkOutDate: this.checkOutDate
      }).then(response => {
        alert('Reservación exitosa');
        this.$router.push('/');
      }).catch(error => {
        alert('Error al hacer la reservación');
      });
    }
  }
}
</script>
