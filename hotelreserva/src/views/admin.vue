<template>
  <div class="admin-view">
    <header class="admin-header">
      <h2>Administradores</h2>
      <button @click="bhHabitaciones">Habitaciones</button>
      <button @click="bhReservas">Reservas</button>
      <button @click="logout">Cerrar sesión</button>
    </header>

    <!-- Tabla de Habitaciones -->
     <section v-if="activeSection === 'habitaciones'" class="rooms-section">
      <h3>Habitaciones</h3>
      <button @click="openAddRoomModal">Agregar Habitación</button>
      <table class="rooms-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Estado</th>
            <th>Tipo</th>
            <th>Precio</th>
            <th>Capacidad</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="room in rooms" :key="room.id">
            <td>{{ room.id }}</td>
            <td>{{ room.status }}</td>
            <td>{{ room.tipo }}</td>
            <td>{{ room.precio }}</td>
            <td>{{ room.capacidad }}</td>
            <td>
              <button @click="editRoom(room)">Editar</button>
              <button @click="deleteRoom(room.id)">Borrar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </section>
    <div v-if="showAddRoomModal" class="modal">
      <div class="modal-content">
        <h3>Agregar Nueva Habitación</h3>
        <label>Estado:</label>
        <input v-model="newRoom.status" type="text" placeholder="Estado de la habitación" />
        
        <label>Tipo:</label>
        <input v-model="newRoom.tipo" type="text" placeholder="Tipo de habitación" />
        
        <label>Precio:</label>
        <input v-model="newRoom.precio" type="number" placeholder="Precio de la habitación" />
        
        <label>Capacidad:</label>
        <input v-model="newRoom.capacidad" type="number" placeholder="Capacidad de personas" />

        <div class="modal-actions">
          <button @click="saveRoom">Guardar</button>
          <button @click="closeAddRoomModal">Cancelar</button>
        </div>
      </div>
    </div>
 
    <!-- Tabla de Reservas -->
<section v-if="activeSection === 'reservas'" class="reservations-section">
  <h3>Reservas</h3>
  <table class="reservations-table">
    <thead>
      <tr>
        <th>Nombre del Cliente</th>
        <th>Correo</th>
        <th>Teléfono</th>
        <th>Check-In</th>
        <th>Check-Out</th>
        <th>Notas</th>
        <th>Estado</th>
        <th>Acción</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="reservation in reservations" :key="reservation.id">
        <td>{{ reservation.client_name }}</td>
        <td>{{ reservation.client_email }}</td>
        <td>{{ reservation.client_phone }}</td>
        <td>{{ reservation.check_in_date }}</td>
        <td>{{ reservation.check_out_date }}</td>
        <td>{{ reservation.additional_notes }}</td>
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
        <p>Selecciona un nuevo estado para la reserva de {{ currentReservation.clientName }}</p>
        
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
 </div>
</template>

<script>
export default {
  data() {
    return {
      activeSection: 'habitaciones',
      rooms: [], // Arreglo para almacenar habitaciones
      reservations: [], // Arreglo para almacenar reservas
      showEditModal: false,
      showAddRoomModal: false,
      currentReservation: null,
      selectedStatus: '',
      newRoom: {
        status: '',
        tipo: '',
        precio: '',
        capacidad: ''
      },
    };
  },
  methods: {
    async fetchRooms() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/habitaciones/');
        if (response.ok) {
          this.rooms = await response.json();
        } else {
          console.error("Error al cargar las habitaciones");
        }
      } catch (error) {
        console.error('Error al cargar habitaciones:', error);
      }
    },
    openAddRoomModal() {
      this.showAddRoomModal = true;
    },
    closeAddRoomModal() {
      this.showAddRoomModal = false;
      this.newRoom = { status: '', tipo: '', precio: '', capacidad: '' };
    },
    async saveRoom() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/habitaciones/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.newRoom),
        });

        if (response.ok) {
          alert("Habitación creada exitosamente");
          this.closeAddRoomModal();
          this.fetchRooms(); // Actualiza la lista de habitaciones
        } else {
          const errorData = await response.json();
          console.error("Error en la creación de la habitación:", errorData);
        }
      } catch (error) {
        console.error('Error al crear la habitación:', error);
      }
    },
    async deleteRoom(id) {
      if (confirm(`¿Estás seguro de que deseas eliminar la habitación ${id}?`)) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/api/habitaciones/${id}/`, {
            method: 'DELETE',
          });

          if (response.ok) {
            this.rooms = this.rooms.filter((room) => room.id !== id);
            alert(`Habitación ${id} eliminada exitosamente.`);
          } else {
            console.error("Error al eliminar la habitación");
          }
        } catch (error) {
          console.error('Error al eliminar la habitación:', error);
        }
      }
    },
    async createReservation(newReservation) {
      try {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Obtén el token CSRF de tu HTML, si usas sesiones

        const response = await fetch('http://127.0.0.1:8000/api/reservas/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken, // Token CSRF
            'Authorization': `Bearer ${localStorage.getItem('token')}`, // Token de autenticación (si aplica)
          },
          body: JSON.stringify(newReservation),
        });
        
        if (response.ok) {
          alert("Reserva creada exitosamente");
          this.fetchReservas(); // Actualiza la lista de reservas
        } else {
          const errorData = await response.json();
          console.error("Error en la creación de la reserva:", errorData);
        }
      } catch (error) {
        console.error('Error al crear la reserva:', error);
      }
    },
    async fetchReservas() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/reservas/');
        if (response.ok) {
          this.reservations = await response.json();
        } else {
          console.error("Error al cargar las reservas");
        }
      } catch (error) {
        console.error('Error al cargar reservas:', error);
      }
    },
    bhHabitaciones() {
      this.activeSection = 'habitaciones';
    },
    bhReservas() {
      this.activeSection = 'reservas';
    },
    logout() {
      localStorage.removeItem('isAuthenticated');
      this.$router.push({ name: 'Login' });
    },
    openEditModal(reservation) {
      this.currentReservation = reservation;
      this.selectedStatus = reservation.status;
      this.showEditModal = true;
    },
    async saveStatus() {
      if (this.currentReservation) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/api/reservas/${this.currentReservation.id}/`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ status: this.selectedStatus }),
          });

          if (response.ok) {
            this.currentReservation.status = this.selectedStatus;
            this.fetchReservas(); // Actualizar lista
            alert("Reserva actualizada con éxito");
            this.closeEditModal();
          } else {
            console.error("Error al actualizar la reserva");
          }
        } catch (error) {
          console.error('Error al guardar el estado:', error);
        }
      }
    },
    closeEditModal() {
      this.showEditModal = false;
      this.currentReservation = null;
      this.selectedStatus = '';
    },
    async deleteReservation(id) {
      if (confirm(`¿Estás seguro de que deseas eliminar la reserva ${id}?`)) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/api/reservas/${id}/`, {
            method: 'DELETE',
          });

          if (response.ok) {
            this.reservations = this.reservations.filter((res) => res.id !== id);
            alert(`Reserva ${id} eliminada exitosamente.`);
          } else {
            console.error("Error al eliminar la reserva");
          }
        } catch (error) {
          console.error('Error al eliminar la reserva:', error);
        }
      }
    },
  },
  mounted() {
    this.fetchReservas();
  }
};
</script>

<style scoped>
/* Aquí va el estilo, basado en tu código original */
</style>


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
  background-color: rgb(13, 34, 54);
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