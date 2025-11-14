# 📖 Instrucciones de Uso - Sistema de Documentos MALLA 2025G

## 🚀 Inicio Rápido

### 1. Iniciar el Servidor

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
npm start
```

Deberías ver este mensaje:
```
╔════════════════════════════════════════════════════════╗
║   🚀 Servidor de Documentos MALLA 2025G               ║
║   📡 Servidor corriendo en: http://localhost:3000    ║
╚════════════════════════════════════════════════════════╝
```

### 2. Acceder al Sistema

El servidor debe estar corriendo para usar el sistema. Abre tu navegador en:

- **Dashboard Principal**: http://localhost:3000
- **Subir Documentos**: http://localhost:3000/upload.html
- **Ver Documentos**: http://localhost:3000/documentos.html

## 📤 Cómo Subir Documentos desde SharePoint

### Opción A: Descarga y Arrastra (Recomendado)

1. Ve a tu SharePoint: https://educorpperu-my.sharepoint.com/...
2. Selecciona los archivos que quieres migrar
3. Descárgalos a tu computadora
4. Abre http://localhost:3000/upload.html
5. Arrastra los archivos a la zona de drop (o haz clic para seleccionar)
6. Presiona "Subir archivos al servidor"
7. ¡Listo! Los archivos están en el proyecto

### Opción B: Descarga Masiva

1. En SharePoint, selecciona toda la carpeta MALLA 2025G
2. Descarga como ZIP
3. Extrae los archivos
4. Sube todos a la vez usando el sistema de drag & drop

## 🔧 Gestión de Documentos

### Ver Documentos
- Ve a http://localhost:3000/documentos.html
- Usa la barra de búsqueda para filtrar
- Haz clic en "Descargar" para obtener un archivo
- Haz clic en "Ver" para abrirlo en el navegador
- Haz clic en "Eliminar" para borrarlo

### Desde el Dashboard
- El dashboard principal tiene botones de navegación arriba
- Puedes moverte entre Dashboard, Documentos y Upload

## 📁 Donde se Guardan los Archivos

Los archivos se almacenan en:
```
proyecto/documentos/MALLA_2025G/
```

Estos archivos están incluidos en el repositorio Git, por lo que se subirán junto con el código.

## ⚠️ Importante

1. **El servidor debe estar corriendo**: Siempre ejecuta `npm start` primero
2. **Puerto 3000**: Si ese puerto está ocupado, edita `server.js` línea 6
3. **Límite de archivo**: 100MB por archivo (configurable en `server.js`)
4. **Navegadores compatibles**: Chrome, Firefox, Edge, Safari modernos

## 🐛 Solución de Problemas

### "Error: Asegúrate de que el servidor esté en ejecución"
- Ejecuta `npm start` en la terminal del proyecto

### "Cannot find module 'express'"
- Ejecuta `npm install` para instalar dependencias

### El puerto 3000 ya está en uso
- Edita `server.js` línea 6: cambia `PORT = 3000` a otro número (ej: 3001)

### Los archivos no aparecen
- Haz clic en "🔄 Actualizar" en la página de documentos
- Verifica que el servidor esté corriendo

## 💡 Consejos

1. Mantén el servidor corriendo mientras trabajas
2. Los archivos se suben automáticamente a Git (están en documentos/MALLA_2025G/)
3. Puedes organizar los archivos en subcarpetas manualmente si lo deseas
4. La búsqueda funciona por nombre de archivo
5. Los archivos duplicados se renombran automáticamente

## 🎯 Flujo de Trabajo Recomendado

1. Inicia el servidor (`npm start`)
2. Descarga archivos de SharePoint
3. Ve a http://localhost:3000/upload.html
4. Arrastra y suelta archivos
5. Sube al servidor
6. Verifica en http://localhost:3000/documentos.html
7. Cuando termines, haz Ctrl+C en la terminal para detener el servidor

¡Ya está todo listo para usar! 🎉
