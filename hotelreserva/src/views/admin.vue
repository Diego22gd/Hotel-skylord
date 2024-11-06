elreserva\src\views\admin.vue
@@ -1,217 +1,82 @@
<template>
  <div class="admin-view">
    <header class="admin-header">
      <h2>Administradores</h2>
      <button @click="bhabitaciones">Habitaciones</button>
      <button @click="breservas">Reservas</button>
      <button @click="logout">Cerrar sesión</button>
    </header>

    <!-- Tabla de Habitaciones -->
    <section v-if="activeSection === 'habitaciones'" class="rooms-section">
      <h3>Habitaciones</h3>
      <table class="rooms-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Estado</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="room in rooms" :key="room.id">
            <td>{{ room.id }}</td>
            <td>{{ room.status }}</td>
            <td>
              <button @click="editRoom(room)">Editar</button>
              <button @click="deleteRoom(room.id)">Borrar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- Tabla de Reservas -->
    <section v-if="activeSection === 'reservas'" class="reservations-section">
      <h3>Reservas</h3>
      <table class="reservations-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Cliente</th>
            <th>Fecha de Entrada</th>
            <th>Fecha de Salida</th>
            <th>Estado</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="reservation in reservations" :key="reservation.id">
            <td>{{ reservation.id }}</td>
            <td>{{ reservation.client }}</td>
            <td>{{ reservation.checkInDate }}</td>
            <td>{{ reservation.checkOutDate }}</td>
            <td>{{ reservation.status }}</td>
            <td>
              <button @click="openEditModal(reservation)">Editar</button>
              <button @click="deleteReservation(reservation.id)">Borrar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- Modal de edición de reserva -->
    <div v-if="showEditModal" class="modal">
      <div class="modal-content">
        <h3>Editar Estado de Reserva</h3>
        <p>Selecciona un nuevo estado para la reserva de {{ currentReservation.client }}</p>
        
        <select v-model="selectedStatus">
          <option value="Confirmada">Confirmada</option>
          <option value="En espera">En espera</option>
          <option value="Rechazada">Rechazada</option>
        </select>

        <div class="modal-actions">
          <button @click="saveStatus">Guardar</button>
          <button @click="closeEditModal">Cancelar</button>
        </div>
      </div>
    </div>
    
    <!-- Modal de edición de habitación -->
    <div v-if="showRoomEditModal" class="modal">
      <div class="modal-content">
        <h3>Editar Estado de Habitación</h3>
        <p>Selecciona un nuevo estado para la habitación {{ currentRoom.id }}</p>
        
        <select v-model="currentRoom.status">
          <option value="Disponible">Disponible</option>
          <option value="Ocupada">Ocupada</option>
          <option value="En Mantenimiento">En Mantenimiento</option>
        </select>

        <div class="modal-actions">
          <button @click="saveRoomStatus">Guardar</button>
          <button @click="closeRoomEditModal">Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeSection: 'habitaciones', // Valor inicial para mostrar la tabla de habitaciones
      rooms: [
        { id: 1, status: 'Disponible' },
        { id: 2, status: 'Ocupada' },
        { id: 3, status: 'En Mantenimiento' },
      ],
      reservations: [
        {
          id: 1,
          client: 'Juan Pérez',
          checkInDate: '2024-11-10',
          checkOutDate: '2024-11-15',
          status: 'Confirmada',
        },
        {
          id: 2,
          client: 'Maria González',
          checkInDate: '2024-11-12',
          checkOutDate: '2024-11-20',
          status: 'Pendiente',
        },
      ],
      showEditModal: false,
      currentReservation: null,
      selectedStatus: '',
      showRoomEditModal: false,
      currentRoom: null,
    };
  },
  methods: {
    bhabitaciones() {
      this.activeSection = 'habitaciones';
    },
    breservas() {
      this.activeSection = 'reservas';
    },
    logout() {
      localStorage.removeItem('isAuthenticated');
      this.$router.push({ name: 'Login' });
    },
    editRoom(room) {
      this.currentRoom = { ...room }; // Copia el objeto de la habitación
      this.showRoomEditModal = true;
    },
    saveRoomStatus() {
      const roomIndex = this.rooms.findIndex(r => r.id === this.currentRoom.id);
      if (roomIndex !== -1) {
        this.rooms[roomIndex].status = this.currentRoom.status;
      }
      this.closeRoomEditModal();
    },
    closeRoomEditModal() {
      this.showRoomEditModal = false;
      this.currentRoom = null;
    },
    deleteRoom(id) {
      if (confirm(`¿Estás seguro de que deseas eliminar la habitación ${id}?`)) {
        this.rooms = this.rooms.filter(room => room.id !== id);
        alert(`Habitación ${id} eliminada exitosamente.`);
      }
    },
    openEditModal(reservation) {
      this.currentReservation = reservation;
      this.selectedStatus = reservation.status;
      this.showEditModal = true;
    },
    saveStatus() {
      if (this.currentReservation) {
        this.currentReservation.status = this.selectedStatus;
        this.closeEditModal();
      }
    },
    closeEditModal() {
      this.showEditModal = false;
      this.currentReservation = null;
      this.selectedStatus = '';
    },
    deleteReservation(id) {
      if (confirm(`¿Estás seguro de que deseas eliminar la reserva ${id}?`)) {
        this.reservations = this.reservations.filter((res) => res.id !== id);
        alert(`Reserva ${id} eliminada exitosamente.`);
      }
    },
  },
};
</script>

<style scoped>


.admin-view {
  padding: 20px;
  font-family: Arial, sans-serif;
}

.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.admin-header h2 {
  font-size: 24px;
  color: #333;
}

.admin-header button {
  background-color: #333;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.admin-header button:hover {
  background-color: #333;
}

.rooms-table, .reservations-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.rooms-table th, .reservations-table th {
  padding: 12px;
  background-color: #f4f6f8;
  color: #050404;
  font-weight: bold;
  text-align: left;
}

.rooms-table td, .reservations-table td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
}

.rooms-table tr:hover, .reservations-table tr:hover {
  background-color: #aae2e2;
}

.rooms-table th, .reservations-table th, 
.rooms-table td, .reservations-table td {
  border:#110e0e;
}

button {
  background-color: #13441f;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin: 5px;
}

button:hover {
  background-color: #218838;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  width: 350px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.modal-content h3 {
  font-size: 18px;
  margin-bottom: 15px;
  color: #333;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

.modal-actions button {
  margin-left: 10px;
  padding: 8px 12px;
  border-radius: 5px;
}

.modal-actions button:first-child {
  background-color: #072647;
}

.modal-actions button:first-child:hover {
  background-color: #072647;
}

.modal-actions button:last-child {
  background-color: #5e1b22;
}

.modal-actions button:last-child:hover {
  background-color: #5a181e;
}
</style>