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
      <div class="form-group">
        <label for="guests">Número de Personas:</label>
        <input type="number" id="guests" v-model="numberOfGuests" min="1" @change="updateAges" required />
      </div>

      <div v-if="numberOfGuests > 0">
        <h3>Ingrese la edad de cada huésped:</h3>
        <div v-for="index in numberOfGuests" :key="index" class="age-input-group">
          <label :for="'age' + index">Huésped {{ index }}:</label>
          <input type="number" :id="'age' + index" v-model="guestAges[index - 1]" min="0" required />
        </div>
      </div>

      <button type="submit">Buscar Habitaciones Disponibles</button>
    </form>

    <div v-if="availableRooms.length > 0">
      <h2>Habitaciones Disponibles</h2>
      <ul>
        <li v-for="(room, index) in availableRooms" :key="index">
          <h3>{{ room.name }}</h3>
          <p>{{ room.description }}</p>
          <button @click="reserveRoom(room)">Reservar</button>
        </li>
      </ul>
    </div>
    <div v-else-if="searchPerformed">
      <p>No hay habitaciones disponibles para esas fechas.</p>
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
      numberOfGuests: 1,
      guestAges: [],
      availableRooms: [],
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
      ],
      searchPerformed: false
    };
  },
  methods: {
    updateAges() {
      this.guestAges = Array.from({ length: this.numberOfGuests }, () => '');
    },
    checkAvailability() {
      this.searchPerformed = true;
      // Simulamos que todas las habitaciones están disponibles.
      this.availableRooms = this.rooms;
    },
    reserveRoom(room) {
      alert(`Has reservado: ${room.name}`);
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

.age-input-group {
  margin-bottom: 10px;
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



</style>

