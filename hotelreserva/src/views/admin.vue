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
      currentReservation: null,
      selectedStatus: '',
    };
  },
  methods: {
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
/* Estilo general para el sitio */
.admin-view {
  padding: 20px;
  font-family: 'Roboto', sans-serif; /* Fuente profesional y moderna */
  background-color: #f5f7fa; /* Fondo claro para un aspecto limpio */
}

/* Estilos para el encabezado */
.admin-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding: 15px;
  background-color: #2c3e50; /* Fondo oscuro para transmitir elegancia */
  color: #ecf0f1;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.admin-header h2 {
  font-size: 1.8rem;
  font-weight: bold;
  color: #ffffff;
}

.admin-header button {
  background-color: #2c3e50; ; /* Azul para contraste con el fondo oscuro */
  color: #ffffff;
  border: none;
  padding: 8px 16px;
  font-size: 1.5rem;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-left: 5px;
}

.admin-header button:hover {
  background-color: #2980b9; /* Azul más oscuro al pasar el cursor */
}

/* Estilos de tablas */
.rooms-section, .reservations-section {
  margin: 20px 0;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
}

.rooms-section h3, .reservations-section h3 {
  color: #2c3e50;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 15px;
}

.rooms-table, .reservations-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.rooms-table th, .reservations-table th {
  padding: 12px;
  background-color: #34495e; /* Fondo oscuro en encabezado de tabla */
  color: #ffffff;
  text-align: left;
  font-weight: bold;
  border-bottom: 3px solid #2c3e50;
}

.rooms-table td, .reservations-table td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
  color: #333333;
}

.rooms-table tr:hover, .reservations-table tr:hover {
  background-color: #eaf1f8; /* Efecto hover para filas */
}

button {
  background-color: #27ae60; /* Botón verde para acciones */
  color: #ffffff;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin: 5px;
}

button:hover {
  background-color: #2ecc71;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

/* Estilo para el modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6); /* Fondo semi-transparente */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 400px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
  text-align: center;
}

.modal-content h3 {
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: #333;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

.modal-actions button {
  padding: 8px 12px;
  border-radius: 5px;
}

.modal-actions button:first-child {
  background-color: #3498db; /* Botón de guardar en azul */
  color: #ffffff;
}

.modal-actions button:first-child:hover {
  background-color: #2980b9;
}

.modal-actions button:last-child {
  background-color: #e74c3c; /* Botón de cancelar en rojo */
  color: #ffffff;
}

.modal-actions button:last-child:hover {
  background-color: #c0392b;
}

/* Estilos responsivos */
@media (max-width: 768px) {
  .admin-header h2 {
    font-size: 1.5rem;
  }

  .admin-header button {
    font-size: 0.9rem;
    padding: 6px 12px;
  }

  .rooms-table th, .reservations-table th,
  .rooms-table td, .reservations-table td {
    font-size: 0.9rem;
    padding: 10px;
  }

  .modal-content {
    width: 100%;
    max-width: 350px;
  }
}

@media (max-width: 480px) {
  .admin-header h2 {
    font-size: 1.2rem;
  }

  .admin-header button {
    font-size: 0.8rem;
    padding: 5px 10px;
  }

  .rooms-table th, .reservations-table th,
  .rooms-table td, .reservations-table td {
    font-size: 0.8rem;
  }
}
</style>
