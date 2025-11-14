# 🌐 Configurar GitHub Pages - Guía Paso a Paso

Esta guía te ayudará a configurar tu proyecto para que funcione en la web usando GitHub Pages.

## Paso 1: Activar GitHub Pages

1. Ve a tu repositorio en GitHub: https://github.com/Xamplix/proyecto
2. Haz clic en **Settings** (Configuración)
3. En el menú lateral, busca **Pages**
4. En **Source**, selecciona:
   - Branch: `main` (o la rama que uses)
   - Folder: `/ (root)`
5. Haz clic en **Save**
6. ¡Listo! Tu sitio estará disponible en: **https://xamplix.github.io/proyecto/**

⏱️ Puede tomar 1-2 minutos en estar listo.

## Paso 2: Crear Token de Acceso Personal de GitHub

Para que la aplicación pueda subir archivos a tu repositorio, necesitas un token:

### 2.1 Generar el Token

1. Ve a: https://github.com/settings/tokens
2. Haz clic en **"Generate new token"** → **"Generate new token (classic)"**
3. Dale un nombre descriptivo, por ejemplo: "MALLA 2025G Upload"
4. En **Select scopes**, marca **SOLO**:
   - ✅ **repo** (Full control of private repositories)
     - Esto incluye: repo:status, repo_deployment, public_repo, repo:invite, security_events
5. Scroll hasta abajo y haz clic en **"Generate token"**
6. **⚠️ IMPORTANTE**: Copia el token que aparece (comienza con `ghp_...`)
   - Solo se muestra UNA VEZ
   - Guárdalo en un lugar seguro

### 2.2 Configurar el Token en la Aplicación

1. Ve a tu sitio: https://xamplix.github.io/proyecto/upload.html
2. Te aparecerá automáticamente un modal pidiendo el token
3. Pega el token y haz clic en **"Guardar Token"**
4. ✅ ¡Listo! Ya puedes subir archivos

**Nota**: El token se guarda en el localStorage de tu navegador. Si limpias el caché o usas otro navegador, tendrás que volver a ingresarlo.

## Paso 3: Usar tu Aplicación en la Web

### URLs de tu Aplicación

Una vez que GitHub Pages esté activo:

- 🏠 **Dashboard**: https://xamplix.github.io/proyecto/
- 📤 **Subir Documentos**: https://xamplix.github.io/proyecto/upload.html
- 📚 **Ver Documentos**: https://xamplix.github.io/proyecto/documentos.html

### Cómo Funciona

1. **Subir archivos**:
   - Los archivos se suben directamente a tu repositorio en GitHub
   - Se guardan en la carpeta `documentos/MALLA_2025G/`
   - Cada subida hace un commit automático

2. **Ver documentos**:
   - La aplicación lee los archivos desde GitHub usando la API
   - Puedes descargarlos o verlos en GitHub
   - Puedes eliminarlos (hace un commit de eliminación)

3. **Completamente en la nube**:
   - No necesitas servidor
   - Todo funciona desde GitHub
   - Los archivos están en tu repositorio

## 🔒 Seguridad

### ¿Es seguro el token?

- ✅ El token se guarda solo en tu navegador (localStorage)
- ✅ No se envía a ningún servidor externo
- ✅ Solo tú tienes acceso desde tu navegador
- ⚠️ No compartas tu token con nadie
- ⚠️ Si lo pierdes, genera uno nuevo y revoca el anterior

### Revocar un Token

Si necesitas revocar un token:
1. Ve a https://github.com/settings/tokens
2. Busca tu token
3. Haz clic en **Delete**

## 🎯 Migrar Archivos desde SharePoint

1. Descarga los archivos de SharePoint a tu computadora
2. Ve a https://xamplix.github.io/proyecto/upload.html
3. Arrastra y suelta todos los archivos
4. Haz clic en "Subir archivos a GitHub"
5. Espera a que todos se suban
6. ¡Listo! Los archivos ahora están en GitHub

## 📝 Diferencias con Servidor Local

| Característica | Servidor Local | GitHub Pages |
|----------------|----------------|--------------|
| Requiere `npm start` | ✅ Sí | ❌ No |
| Funciona sin internet | ✅ Sí | ❌ No |
| Archivos en GitHub | ❌ Manual | ✅ Automático |
| Necesita token | ❌ No | ✅ Sí |
| Acceso desde cualquier lugar | ❌ No | ✅ Sí |
| URL pública | ❌ No | ✅ Sí |

## 🐛 Solución de Problemas

### Error: "401 Bad credentials"
- Tu token es inválido o expiró
- Genera un nuevo token y vuelve a configurarlo

### Error: "403 Forbidden"
- Tu token no tiene permisos suficientes
- Asegúrate de haber marcado el permiso **repo**

### Error: "404 Not Found"
- La carpeta de documentos no existe aún
- Sube tu primer archivo para crearla automáticamente

### Los cambios no aparecen en GitHub Pages
- GitHub Pages puede tardar 1-2 minutos en actualizar
- Intenta refrescar la página con Ctrl+F5 (forzar recarga)

### El modal de token no aparece
- Abre la consola del navegador (F12)
- Escribe: `CONFIG.setToken("tu-token-aqui")`
- Presiona Enter

## ✅ Verificar que Todo Funciona

1. Ve a https://xamplix.github.io/proyecto/
2. Deberías ver el dashboard de Power BI
3. Haz clic en "Subir Archivos"
4. Configura tu token
5. Sube un archivo de prueba
6. Ve a "Mis Documentos"
7. Deberías ver el archivo que subiste
8. Verifica en GitHub que el archivo está en `documentos/MALLA_2025G/`

## 🎉 ¡Todo Listo!

Ahora tu aplicación funciona completamente en la web sin necesidad de servidor. Puedes acceder desde cualquier dispositivo con internet.

---

**Repositorio**: https://github.com/Xamplix/proyecto
**Sitio Web**: https://xamplix.github.io/proyecto/
