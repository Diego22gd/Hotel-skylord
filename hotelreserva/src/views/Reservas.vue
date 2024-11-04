<template>
  <div class="titulo">
    <h1 class="nos">Reservas</h1>
  </div>
  <div class="reservas">
    <form @submit.prevent="checkAvailability">
      <div class="form-group">
        <label for="checkIn">Fecha de Entrada:</label>
        <input type="date" id="checkIn" v-model="checkInDate" required />
      </div>
      <div class="form-group">
        <label for="checkOut">Fecha de Salida:</label>
        <input type="date" id="checkOut" v-model="checkOutDate" required />
      </div>
      <button type="submit">Buscar Habitaciones Disponibles</button>
    </form>

    <div v-if="availableRooms.length > 0">
      <h2>Habitaciones Disponibles</h2>
      <ul>
        <li v-for="(room, index) in availableRooms" :key="index">
          <h3>{{ room.name }}</h3>
          <p>{{ room.description }}</p>
          <button @click="openReservationModal(room)">Reservar</button>
        </li>
      </ul>
    </div>
    <div v-else-if="searchPerformed">
      <p>No hay habitaciones disponibles para esas fechas.</p>
    </div>
  </div>

  <!-- Modal -->
  <div v-if="isReservationModalOpen" class="modal">
    <div class="modal-content">
      <span class="close" @click="closeReservationModal">&times;</span>
      <h2>Realizar Reserva</h2>
      <form @submit.prevent="confirmReservation">
        <div class="form-group">
          <label for="clientName">Nombre del Cliente:</label>
          <input type="text" id="clientName" v-model="newReservation.clientName" required />
        </div>
        <div class="form-group">
          <label for="clientEmail">Correo Electrónico:</label>
          <input type="email" id="clientEmail" v-model="newReservation.clientEmail" required />
        </div>
        <div class="form-group">
          <label for="clientPhone">Número de Teléfono:</label>
          <input type="text" id="clientPhone" v-model="newReservation.clientPhone" required />
        </div>
        <div class="form-group">
          <label for="additionalNotes">Notas Adicionales:</label>
          <textarea id="additionalNotes" v-model="newReservation.additionalNotes"></textarea>
        </div>
        <button type="submit">Confirmar Reserva</button>
      </form>
    </div>
  </div>
</template>

<script>
import roomImage1 from '@/assets/individual.jpg';
import roomImage2 from '@/assets/doble.jpg';
import roomImage3 from '@/assets/deluxe.jpg';

export default {
  data() {
    return {
      checkInDate: '',
      checkOutDate: '',
      availableRooms: [],
      searchPerformed: false,
      isReservationModalOpen: false,
      selectedRoom: null,
      newReservation: {
        clientName: '',
        clientEmail: '',
        clientPhone: '',
        additionalNotes: ''
      },
      rooms: [
        {
          name: 'Habitación Simple',
          description: 'Habitación ideal para una persona.',
          image: roomImage1
        },
        {
          name: 'Habitación Doble',
          description: 'Ideal para parejas o pequeñas familias.',
          image: roomImage2
        },
        {
          name: 'Suite Deluxe',
          description: 'Amplia y lujosa suite para disfrutar de su estadía.',
          image: roomImage3
        }
      ]
    };
  },
  methods: {
    checkAvailability() {
      this.searchPerformed = true;
      this.availableRooms = this.rooms; // Asumimos que todas las habitaciones están disponibles
    },
    openReservationModal(room) {
      this.selectedRoom = room;
      this.isReservationModalOpen = true;
    },
    closeReservationModal() {
      this.isReservationModalOpen = false;
      this.selectedRoom = null;
    },
    confirmReservation() {
      alert(`Reserva confirmada para ${this.selectedRoom.name} por ${this.newReservation.clientName}.`);
      this.closeReservationModal();
    }
  }
};
</script>

<style scoped>
.reservas {
  padding: 20px;
  max-width: 800px;
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

.titulo {
  position: relative;
  height: 50vh;
  background-image: url('@/assets/hotel.webp');
  background-position: center center;
  background-size: cover;
  color: rgb(247, 247, 247);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.nos {
  font-size: 4em;
  font-weight: bold;
  font-style: italic;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  max-width: 500px;
  width: 100%;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
}
</style>
