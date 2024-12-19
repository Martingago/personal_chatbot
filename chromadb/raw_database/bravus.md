% title: BRAVUS - Demo tienda online.
% document: Readme proyecto
% url_source: https://github.com/Martingago/nuxt3-proyect
% web_source: https://bravus.vercel.app/
% date_publication: 20-11-2023
% content:

# BRAVUS - Demo Tienda Online

**BRAVUS** es un proyecto de tienda online desarrollado utilizando **NUXT3** como framework principal y **Firebase** como backend para el almacenamiento de datos de usuarios y productos. Además, el diseño visual fue realizado con la ayuda de **Bootstrap**.

## 🌟 Funcionalidades Principales

- **Carga de productos**: Los productos se cargan dinámicamente desde una base de datos en Firebase.
- **Autenticación de usuarios**: Permite a los usuarios registrarse mediante autenticación con Google.
- **Gestión de carritos**: Cada usuario puede gestionar su propio carrito de compras.
- **Registro de compras**: Historial de compras registrado para cada usuario.
- **Área administrativa**: Funcionalidad para añadir, eliminar o modificar productos y categorías.
- **Google Analytics**: Integración para el seguimiento del comportamiento de los usuarios.

## 🌐 Demo en Línea

Puedes acceder a la demo del proyecto a través del siguiente enlace:

[BRAVUS Demo](https://bravus.vercel.app/)

## 🚀 Ejecución Local

### Clonar el repositorio

```bash
https://github.com/Martingago/nuxt3-proyect
```

### Instalar dependencias

Elige tu gestor de paquetes preferido:

```bash
# Con Yarn
yarn install

# Con npm
npm install

# Con pnpm
pnpm install
```

### Iniciar el servidor de desarrollo

Ejecuta el siguiente comando para iniciar el servidor de desarrollo:

```bash
npm run dev
```

El proyecto estará disponible en: [http://localhost:3000](http://localhost:3000).

## ⚙️ Configuración de Firebase

Para habilitar la conexión con Firebase, es necesario crear un archivo `.env` en la raíz del proyecto con la siguiente estructura:

```env
FIREBASE_API_KEY=your.api.key.here
FIREBASE_PROJECT_ID=your.project.id.here
FIREBASE_STORAGE_BUCKET=your.storage.bucket.here
```

Reemplaza los valores con las credenciales de tu proyecto en Firebase.

---

**Autor**: [Martingago](https://www.linkedin.com/in/martin-gago-choren/)

© 2023 BRAVUS. Todos los derechos reservados.
