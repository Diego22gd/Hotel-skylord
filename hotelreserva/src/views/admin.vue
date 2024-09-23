<template>
  <div>
    <h1>Gestión de Reservaciones</h1>
    <ul>
      <li v-for="reservation in reservations" :key="reservation.id">
        {{ reservation.name }} - {{ reservation.room }} 
        - {{ reservation.status }}
        <button @click="markAsPaid(reservation.id)">Marcar como Pagado</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      reservations: []
    }
  },
  mounted() {
    // Obtener reservaciones de la API
    axios.get('https://api.hotel.com/reservations')
      .then(response => {
        this.reservations = response.data;
      });
  },
  methods: {
    markAsPaid(id) {
      // Actualizar el estado de la reservación
      axios.put(`https://api.hotel.com/reservations/${id}`, { status: 'Paid' })
        .then(() => {
          alert('Estado actualizado a pagado');
          this.reservations = this.reservations.map(reservation => {
            if (reservation.id === id) {
              reservation.status = 'Paid';
            }
            return reservation;
          });
        });
    }
  }
}
</script>
