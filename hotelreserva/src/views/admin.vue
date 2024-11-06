<.admin-view {
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
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.admin-header button:hover {
  background-color: #0056b3;
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
  color: #555;
  font-weight: bold;
  text-align: left;
}

.rooms-table td, .reservations-table td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
}

.rooms-table tr:hover, .reservations-table tr:hover {
  background-color: #f9fbfc;
}

.rooms-table th, .reservations-table th, 
.rooms-table td, .reservations-table td {
  border: none;
}

button {
  background-color: #28a745;
  color: #fff;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
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
  background-color: #007bff;
}

.modal-actions button:first-child:hover {
  background-color: #0056b3;
}

.modal-actions button:last-child {
  background-color: #dc3545;
}

.modal-actions button:last-child:hover {
  background-color: #c82333;
}
