n# hotelreserva

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Run End-to-End Tests with [Playwright](https://playwright.dev)

```sh
# Install browsers for the first run
npx playwright install

# When testing on CI, must build the project first
npm run build

# Runs the end-to-end tests
npm run test:e2e
# Runs the tests only on Chromium
npm run test:e2e -- --project=chromium
# Runs the tests of a specific file
npm run test:e2e -- tests/example.spec.ts
# Runs the tests in debug mode
npm run test:e2e -- --debug
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
# Hotel Skylord

Este proyecto es una aplicación web para el Hotel Skylord, que permite a los usuarios navegar entre las diferentes secciones del sitio web, como "Inicio", "Nosotros" y "Reservas". Este proyecto utiliza Vue.js para la construcción de la interfaz de usuario.

## Tabla de contenidos
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Componentes](#componentes)
- [Estilos](#estilos)
- [Rutas](#rutas)
- [Personalización](#personalización)

## Instalación

1. Clona el repositorio.
   ```bash
   git clone https://github.com/usuario/hotel-skylord.git


Navega al directorio del proyecto.

cd hotel-skylord

Instala las dependencias.

npm install

Inicia el servidor de desarrollo.

npm run dev


App.vue

Es el componente principal de la aplicación. Contiene:

    Header: Un encabezado con el nombre del hotel y una barra de navegación.
    Router View: Muestra el contenido de la vista actual según la rut

main.js

El archivo main.js es el punto de entrada de la aplicación Vue. Configura Vue, registra las rutas y monta la aplicación en el DOM.

Hotel Skylord - Página de Inicio

Este archivo describe la estructura, funcionalidad y estilos de la página de inicio para el sitio web del Hotel Skylord. La página proporciona una descripción del hotel, un carrusel de habitaciones, una galería de imágenes y la información de contacto y dirección.
Estructura del Componente
Encabezado (<header class="header">)

    Contiene la sección hero, que muestra una imagen de fondo con el título "HOTEL SKYLORD".
    La imagen de fondo se ajusta para cubrir el área del encabezado y se oscurece para mejorar la visibilidad del título.

Sección de Información (<section class="info">)

    Incluye una breve introducción sobre el hotel.
    Texto centrado y estilizado para mejorar la legibilidad sobre el fondo oscuro.

Carrusel de Habitaciones (<div class="rooms-carousel">)

    Muestra información sobre las habitaciones del hotel en un carrusel.
    Cada habitación contiene:
        Imagen (<img class="room-image">)
        Nombre (<h2>{{ room.name }}</h2>)
        Descripción (<p>{{ room.description }}</p>)
        Botón Reservar (<button @click="reserveRoom(room)">Reservar</button>): activa un alert con el nombre de la habitación seleccionada.
    Puntos de navegación (<div class="dots">): permite al usuario cambiar entre las habitaciones.

Galería de Imágenes (<div class="galeria">)

    Incluye una galería de imágenes del hotel.
    Botones de navegación (@click="prev" y @click="next"): permiten desplazar las imágenes.
    Estilo dinámico: cambia la posición de las imágenes visibles usando el método galleryStyle.

Información de Contacto (<div class="informacion">)

    Muestra la información de contacto y dirección.
    Organizada en dos columnas:
        Contacto: números de WhatsApp y correo electrónico.
        Dirección: ubicación del hotel.

Métodos de Vue

    reserveRoom(room): muestra una alerta cuando se selecciona el botón "Reservar" de una habitación.
    next() y prev(): cambian el índice actual de la imagen en la galería para avanzar o retroceder.

Computed Properties

    galleryStyle: calcula la posición de la galería de imágenes, desplazando las visibles según el índice actual.

Estilos (CSS)

    Encabezado: ocupa el 80% de la altura de la pantalla, con un fondo oscuro superpuesto para resaltar el título.
    Barra de navegación: contiene enlaces estilizados y centrados; el color de los enlaces cambia en hover.
    Hero (Título del Hotel): texto centrado, con sombra para mejorar la visibilidad.
    Sección de Información: fondo oscuro, texto blanco, centrado y con márgenes.
    Carrusel de Habitaciones: muestra cada habitación con su imagen y descripción. Los puntos de navegación indican la habitación actual.
    Galería: muestra imágenes desplazables en un contenedor, con botones de flecha para navegar.
    Información de Contacto: secciones de contacto y dirección organizadas en columnas para mayor claridad.

Assets

    Imágenes de Habitaciones: individual.jpg, doble.jpg, deluxe.jpg.
    Imágenes de Galería: hotel1.jpg a hotel10.jpeg.

Configuración y Dependencias

    Asegúrate de tener configuradas las rutas en Vue Router para manejar las vistas.
    Las imágenes deben estar en la carpeta assets dentro del proyecto.

Componente Nosotros
Descripción General

Este componente presenta:

    Un encabezado "Nosotros" con una imagen de fondo.
    Secciones detalladas sobre la historia del hotel, eventos importantes, y la información general de servicios y comodidades.

Estructura del Componente
<template>

    Contiene tres bloques principales de información dentro de la clase hotel-info, cada uno con encabezados y contenido específicos:
        Nuestra Historia: Un párrafo que explica el origen y la trayectoria del hotel.
        Eventos Especiales: Sección donde se destacan algunos eventos importantes que han tenido lugar en el hotel, usando una lista.
        Información del Hotel: Una lista de comodidades que ofrece el hotel (habitaciones, gimnasio, restaurante, piscina, spa).

<script>

    El componente se llama Nosotros.
    No se define ninguna funcionalidad adicional, ya que este componente solo muestra contenido estático.

<style scoped>

    General: La página usa estilos en tonos de azul para el fondo, y el texto es blanco para una mejor legibilidad sobre el fondo oscuro.
    .nosotros: Define un padding para el componente y un fondo oscuro para toda la sección.
    .hotel-info: Define un ancho máximo para las secciones principales y centra el contenido horizontalmente.
    .titulo: Es el encabezado con la imagen de fondo. Ajusta el tamaño de la imagen, alinea el texto centrado y aplica un efecto de sombra al texto para que sea visible sobre la imagen.
    .nos: Da estilo al título "Nosotros", aplicando un tamaño grande, negritas, cursiva y sombra para resaltar sobre el fondo.
    .historia, .eventos, .info: Estas clases se aplican a las secciones de historia, eventos y comodidades. Incluyen:
        Background: Fondo en azul (#287fc1) para separar visualmente estas secciones.
        Texto: Alineación centrada, tamaño de fuente de 20px, y bordes redondeados para darle un estilo moderno.
        Dimensiones y espaciado: La altura de la historia y eventos es fija (20rem), mientras que info se adapta automáticamente a su contenido.

Componente reservas
Descripción General

Este componente incluye:

    Un formulario para seleccionar las fechas de entrada y salida.
    Un botón para buscar disponibilidad de habitaciones.
    Una lista de habitaciones disponibles con un botón para realizar la reserva.
    Un modal emergente para confirmar la reserva, donde se ingresan los datos del cliente.

Estructura del Componente
<template>

    Encabezado: El título "Reservas" con una imagen de fondo.
    Formulario de Búsqueda: Contiene dos campos de fecha (entrada y salida) y un botón de búsqueda.
    Lista de Habitaciones Disponibles: Se muestra cuando hay habitaciones disponibles. Cada habitación tiene un nombre, descripción y un botón "Reservar".
    Modal de Reserva: Aparece al seleccionar una habitación. Incluye campos para el nombre, correo, teléfono y notas adicionales del cliente. Un botón "Confirmar Reserva" completa el proceso de reserva.

<script>

    Importación de Imágenes: Importa imágenes de habitaciones.
    Data: Define el estado inicial del componente:
        checkInDate y checkOutDate: Fechas de entrada y salida seleccionadas por el usuario.
        availableRooms: Lista de habitaciones disponibles.
        searchPerformed: Indica si se ha realizado la búsqueda.
        isReservationModalOpen: Estado del modal de reserva.
        selectedRoom: Habitación seleccionada para reserva.
        newReservation: Contiene los datos del cliente.
        rooms: Información de las habitaciones disponibles en el hotel.
    Métodos:
        checkAvailability: Simula la disponibilidad, mostrando todas las habitaciones.
        openReservationModal: Abre el modal para confirmar la reserva.
        closeReservationModal: Cierra el modal y limpia la selección.
        confirmReservation: Muestra una alerta confirmando la reserva y cierra el modal.

<style scoped>

    .reservas: Define el contenedor de reservas con padding y un ancho máximo.
    .form-group: Estilo básico de margen para cada grupo de entrada en el formulario.
    label y input: Los campos de entrada se ajustan al ancho completo y tienen bordes redondeados.
    button: Estilo de botón con fondo azul, texto blanco, y cambio de color al pasar el cursor.
    .titulo: Imagen de fondo y texto con estilo de sombra para el encabezado.
    .modal: Estilo de modal con fondo semitransparente y centrado de contenido.
    .modal-content: Fondo blanco, bordes redondeados y alineación centrada.
    .close: Estilo del botón de cerrar el modal, situado en la esquina superior derecha.

Funcionalidad Completa

Este componente permite al usuario:

    Elegir fechas para buscar habitaciones disponibles.
    Ver una lista de habitaciones y reservar la que deseen.
    Completar el formulario de reserva en el modal, que incluye los datos del cliente.

Login
Descripción General

Este componente incluye:

    Un encabezado con el título "Iniciar Sesión" y una imagen de fondo.
    Un formulario de inicio de sesión con campos para el correo electrónico y la contraseña.
    Un botón para enviar el formulario.
    Un mensaje de error en caso de que las credenciales no sean correctas.

Estructura del Componente
<template>

    Encabezado: Título "Iniciar Sesión" con una imagen de fondo.
    Formulario de Inicio de Sesión: Contiene dos campos, uno para el correo electrónico (o nombre de usuario) y otro para la contraseña. El botón "Ingresar" envía el formulario y dispara la función login.
    Mensaje de Error: Aparece si las credenciales no coinciden con las establecidas.

<script>

    Data: Define el estado inicial:
        username y password: Capturan el valor de los campos de entrada.
        errorMessage: Muestra un mensaje de error si las credenciales no son correctas.
    Métodos:
        login: Verifica si las credenciales son correctas (admin y 123456). Si lo son:
            Guarda una marca de autenticación en localStorage.
            Redirige a la vista de administración.
            Si las credenciales no coinciden, muestra un mensaje de error.

<style scoped>

    .login: Define el contenedor del formulario con padding y un ancho máximo.
    .form-group: Define márgenes para cada grupo de entrada en el formulario.
    label e input: Estilo de los campos de entrada con bordes redondeados.
    button: Botón de envío con color de fondo azul, cambio de color al pasar el cursor.
    .titulo: Imagen de fondo y texto centrado para el encabezado, con sombra.
    .nos: Estilo de texto para el título, incluyendo fuente grande y sombreado.

Funcionalidad Completa

Este componente permite:

    Verificar credenciales y simular un sistema de autenticación.
    Almacenar el estado de autenticación en localStorage.
    Redirigir al usuario a la vista de administración si las credenciales son correctas.

Componente Admin
Este componente Vue representa la vista de administración del hotel, permitiendo gestionar habitaciones y reservas. Los administradores pueden ver listas de habitaciones y reservas, editar el estado de cada elemento, y eliminarlos si es necesario.
Descripción General

Este componente incluye:

    Encabezado de Administración: Botones de navegación para las secciones de habitaciones y reservas, y un botón de cierre de sesión.
    Tabla de Habitaciones: Lista de habitaciones con opciones para editar o eliminar cada una.
    Tabla de Reservas: Lista de reservas con opciones para editar el estado de cada reserva o eliminarlas.
    Modal de Edición: Modal para cambiar el estado de las habitaciones y de las reservas.

Estructura del Componente
<template>

    Encabezado (admin-header): Contiene botones para navegar entre las secciones de habitaciones y reservas, y un botón de cierre de sesión.
    Sección de Habitaciones (rooms-section): Muestra una tabla con las habitaciones, cada una con sus opciones de edición y eliminación.
    Sección de Reservas (reservations-section): Tabla similar para las reservas, con detalles de cada reserva y opciones para editar el estado o eliminar.
    Modal de Edición: Dos modales separados, uno para cambiar el estado de una reserva y otro para modificar el estado de una habitación.

<script>

    Data:
        activeSection: Indica la sección activa (habitaciones o reservas).
        rooms: Lista de habitaciones, cada una con su ID y estado.
        reservations: Lista de reservas, cada una con detalles del cliente, fechas y estado.
        showEditModal y showRoomEditModal: Controlan la visibilidad de los modales de edición para reservas y habitaciones.
        currentReservation y currentRoom: Objetos temporales que almacenan la reserva o habitación que se está editando.
        selectedStatus: Estado seleccionado para una reserva.
    Methods:
        bhabitaciones y breservas: Alternan entre las secciones de habitaciones y reservas.
        logout: Cierra la sesión y redirige a la página de inicio de sesión.
        editRoom y saveRoomStatus: Permiten editar y guardar el estado de una habitación.
        deleteRoom: Elimina una habitación tras confirmación.
        openEditModal y saveStatus: Permiten editar y guardar el estado de una reserva.
        closeEditModal y closeRoomEditModal: Cierran los modales de edición.

<style scoped>

    Estilos generales: Define los estilos básicos para la vista de administración, incluyendo el contenedor, encabezado, botones, y tablas.
    Modales: Estilos de los modales, incluyendo la estructura de modal-content, botones de acción y los estilos de los botones de confirmación y cancelación en los modales.

Funcionalidad Completa

Este componente facilita a los administradores:

    Cambiar entre la vista de habitaciones y la de reservas.
    Editar y eliminar habitaciones.
    Editar y eliminar reservas, incluyendo la modificación del estado de la reserva.
    Cerrar sesión y volver a la página de inicio.

Este componente es adecuado para gestionar habitaciones y reservas de un hotel, permitiendo una administración intuitiva de ambos elementos.
