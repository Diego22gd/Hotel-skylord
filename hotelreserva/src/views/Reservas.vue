<template>
  <div class="titulo">
    <h1 class="nos">Reservas</h1>
  </div>
  <div class="reservas">
    <form @submit.prevent="checkAvailability">
      <div class="form-group">
        <label for="checkIn">Fecha de Entrada:</label>
        <input type="date" id="checkIn" v-model="reservationData.check_in_date" required />
      </div>
      <div class="form-group">
        <label for="checkOut">Fecha de Salida:</label>
        <input type="date" id="checkOut" v-model="reservationData.check_out_date" required />
      </div>
      <button type="submit">Buscar Habitaciones Disponibles</button>
    </form>

    <div v-if="availableRooms.length > 0">
      <h2>Habitaciones Disponibles</h2>
      <ul>
        <li v-for="(room, index) in availableRooms" :key="index">
          <h3>{{ room.name }}</h3>
          <p>{{ room.description }}</p>
          <img :src="room.image" alt="Imagen de la habitación" class="room-image" />
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
          <input type="text" id="clientName" v-model="newReservation.client_name" required />
        </div>
        <div class="form-group">
          <label for="clientEmail">Correo Electrónico:</label>
          <input type="email" id="clientEmail" v-model="newReservation.client_email" required />
        </div>
        <div class="form-group">
          <label for="clientPhone">Número de Teléfono:</label>
          <input type="text" id="clientPhone" v-model="newReservation.client_phone" required />
        </div>
        <div class="form-group">
          <label for="additionalNotes">Notas Adicionales:</label>
          <textarea id="additionalNotes" v-model="newReservation.additional_notes"></textarea>
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
      reservationData: {
        check_in_date: '',  // Fecha de check-in
        check_out_date: '',
        client_name: '',
        client_email: '',
        client_phone: '',
        additional_notes: '',
        room_type: ''
         // Fecha de check-out
         // Fecha de check-out
      },
      availableRooms: [],  // Inicializamos availableRooms
      searchPerformed: false,
      isReservationModalOpen: false,
      selectedRoom: null,
      newReservation: {
        client_name: '',
        client_email: '',
        client_phone: '',
        additional_notes: '',
        room_type: ''
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
      // Se realiza la simulación de que todas las habitaciones están disponibles
      this.availableRooms = this.rooms;
      this.searchPerformed = true;
    },
    openReservationModal(room) {
      this.selectedRoom = room;
      this.isReservationModalOpen = true;
      // Establece los detalles de la habitación en newReservation
      this.newReservation.room_type = room.name;
      this.newReservation.check_in_date = this.reservationData.check_in_date;
      this.newReservation.check_out_date = this.reservationData.check_out_date;
    },
    closeReservationModal() {
      this.isReservationModalOpen = false;
      this.selectedRoom = null;
    },
    async confirmReservation() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/reservas/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.newReservation),
        });

        if (!response.ok) {
          const errorText = await response.text();
          console.error('Error en la solicitud:', errorText);
          alert('Error al confirmar la reserva');
          return;
        }

        const data = await response.json();
        console.log('Reserva confirmada:', data);
        alert('Reserva confirmada con éxito');
        this.closeReservationModal();
      } catch (error) {
        console.error('Error de red:', error);
        alert('Error al confirmar la reserva');
      }
    }
  }
};
</script>


<style scoped>
.reservas {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
  font-family: 'Roboto', sans-serif;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #555;
}

input, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
  transition: border-color 0.3s ease;
  font-size: 1em;
}

input:focus, textarea:focus {
  border-color: #d4a017; /* Dorado suave */
  outline: none;
}

button {
  padding: 12px 18px;
  background-color: #d4a017;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1.1em;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #b38c0a; /* Dorado más oscuro */
}

.titulo {
  position: relative;
  height: 60vh;
  background-image: url('@/assets/hotel.webp');
  background-position: center center;
  background-size: cover;
  color: #f7f7f7;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.nos {
  font-size: 4em;
  font-weight: 700;
  font-family: 'Playfair Display', serif; /* Fuente elegante */
  font-style: italic;
  text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.5);
  color: #fff;
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
  background-color: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(5px); /* Agrega un desenfoque elegante */
  transition: opacity 0.3s ease;
}

.modal-content {
  background-color: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  max-width: 500px;
  width: 100%;
  position: relative;
  font-family: 'Roboto', sans-serif;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 1.5em;
  color: #333;
}

.close:hover {
  color: #d4a017;
}
@media (max-width: 768px) {
  .titulo h1 {
    font-size: 2em;
  }

  .reservas {
    width: 90%;
    padding: 15px;
  }

  .room-item {
    flex-direction: column;
  }

  .modal-content {
    width: 90%;
  }
}

@media (max-width: 480px) {
  .titulo h1 {
    font-size: 1.8em;
  }

  .room-item {
    width: 100%;
  }

  .modal-content {
    width: 100%;
    padding: 15px;
  }

  input, textarea, button {
    font-size: 0.9em;
    padding: 10px;
  }
}

</style>
