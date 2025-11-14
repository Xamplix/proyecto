# Sistema de Gestión de Documentos - MALLA 2025G

Sistema web para visualizar un dashboard de Power BI y gestionar documentos de forma fácil con interfaz drag & drop.

## 🚀 Características

- **Dashboard Power BI**: Visualización de datos integrada
- **Subida de Documentos**: Interfaz drag & drop moderna y fácil de usar
- **Gestión de Archivos**: Visualiza, busca, descarga y elimina documentos
- **Estadísticas**: Información sobre total de archivos y espacio usado

## 📋 Requisitos

- Node.js (versión 14 o superior)
- npm (incluido con Node.js)

## 🔧 Instalación

1. Clona este repositorio o descarga los archivos

2. Instala las dependencias:
```bash
npm install
```

## ▶️ Uso

1. Inicia el servidor:
```bash
npm start
```

2. Abre tu navegador y visita:
   - Dashboard: `http://localhost:3000`
   - Subir documentos: `http://localhost:3000/upload.html`
   - Ver documentos: `http://localhost:3000/documentos.html`

## 📁 Estructura del Proyecto

```
proyecto/
├── index.html          # Página principal con dashboard
├── upload.html         # Interfaz de subida de documentos
├── upload.js           # Lógica de subida
├── documentos.html     # Visualizador de documentos
├── documentos.js       # Lógica de gestión de documentos
├── server.js           # Servidor Node.js
├── package.json        # Configuración de npm
├── documentos/
│   └── MALLA_2025G/   # Carpeta de almacenamiento
└── README.md          # Este archivo
```

## 🎯 Cómo Subir Documentos

1. Ve a `http://localhost:3000/upload.html`
2. Arrastra archivos a la zona de drop o haz clic para seleccionar
3. Haz clic en "Subir archivos al servidor"
4. Los archivos se guardarán en `documentos/MALLA_2025G/`

## 📚 Cómo Ver Documentos

1. Ve a `http://localhost:3000/documentos.html`
2. Navega por tus documentos
3. Usa la barra de búsqueda para filtrar
4. Descarga, visualiza o elimina archivos

## 🛠️ Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Node.js, Express
- **Upload**: Multer
- **CORS**: cors

## 📝 Notas

- El límite de tamaño de archivo es de 100MB
- Los archivos se almacenan en `documentos/MALLA_2025G/`
- El servidor corre en el puerto 3000 por defecto

## 👤 Autor

Proyecto MALLA 2025G
