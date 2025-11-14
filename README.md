# Sistema de Gestión de Documentos - MALLA 2025G

Sistema web para visualizar un dashboard de Power BI y gestionar documentos de forma fácil con interfaz drag & drop.

**✨ Ahora funciona 100% en la web con GitHub Pages - ¡No necesitas servidor!**

> 🚀 **[Ver Guía de Inicio Rápido (3 pasos)](INICIO-RAPIDO.md)**

## 🌐 Acceso Web

**URL**: https://xamplix.github.io/proyecto/

- 🏠 Dashboard: https://xamplix.github.io/proyecto/
- 📤 Subir: https://xamplix.github.io/proyecto/upload.html
- 📚 Documentos: https://xamplix.github.io/proyecto/documentos.html

> **Nota**: Para usar la versión web, necesitas configurar un token de GitHub. Lee [SETUP-GITHUB-PAGES.md](SETUP-GITHUB-PAGES.md) para instrucciones.

## 🚀 Características

- **Dashboard Power BI**: Visualización de datos integrada
- **Subida de Documentos**: Interfaz drag & drop moderna y fácil de usar
- **Gestión de Archivos**: Visualiza, busca, descarga y elimina documentos
- **Estadísticas**: Información sobre total de archivos y espacio usado

## 📋 Dos Formas de Usar

### Opción 1: GitHub Pages (Recomendado) 🌐

✅ **Sin instalación**
✅ **Sin servidor**
✅ **Acceso desde cualquier lugar**

Lee [SETUP-GITHUB-PAGES.md](SETUP-GITHUB-PAGES.md) para activarlo.

### Opción 2: Servidor Local 💻

Para desarrollo local o uso sin internet.

**Requisitos:**
- Node.js (versión 14 o superior)
- npm (incluido con Node.js)

## 🔧 Instalación (Solo para uso local)

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
