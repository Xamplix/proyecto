const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

// Configurar almacenamiento de multer
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        const uploadPath = path.join(__dirname, 'documentos', 'MALLA_2025G');

        // Crear directorio si no existe
        if (!fs.existsSync(uploadPath)) {
            fs.mkdirSync(uploadPath, { recursive: true });
        }

        cb(null, uploadPath);
    },
    filename: function (req, file, cb) {
        // Decodificar el nombre del archivo para manejar caracteres especiales
        const decodedName = Buffer.from(file.originalname, 'latin1').toString('utf8');

        // Sanitizar el nombre del archivo
        const safeName = decodedName.replace(/[^a-zA-Z0-9áéíóúñÁÉÍÓÚÑ._\-\s]/g, '_');

        // Agregar timestamp si el archivo ya existe
        const ext = path.extname(safeName);
        const basename = path.basename(safeName, ext);
        const finalPath = path.join(__dirname, 'documentos', 'MALLA_2025G', safeName);

        if (fs.existsSync(finalPath)) {
            const timestamp = Date.now();
            cb(null, `${basename}_${timestamp}${ext}`);
        } else {
            cb(null, safeName);
        }
    }
});

const upload = multer({
    storage: storage,
    limits: {
        fileSize: 100 * 1024 * 1024 // 100MB límite
    }
});

// Endpoint para subir archivos
app.post('/upload', upload.array('files'), (req, res) => {
    try {
        if (!req.files || req.files.length === 0) {
            return res.status(400).json({ error: 'No se recibieron archivos' });
        }

        const uploadedFiles = req.files.map(file => ({
            originalName: file.originalname,
            savedName: file.filename,
            size: file.size,
            path: file.path
        }));

        console.log(`✅ ${req.files.length} archivo(s) subido(s) correctamente`);

        res.json({
            success: true,
            message: `${req.files.length} archivo(s) subido(s) correctamente`,
            files: uploadedFiles
        });
    } catch (error) {
        console.error('Error al subir archivos:', error);
        res.status(500).json({ error: 'Error al subir archivos' });
    }
});

// Endpoint para listar archivos
app.get('/api/files', (req, res) => {
    try {
        const docsPath = path.join(__dirname, 'documentos', 'MALLA_2025G');

        if (!fs.existsSync(docsPath)) {
            return res.json({ files: [] });
        }

        const files = fs.readdirSync(docsPath)
            .filter(file => file !== 'README.md')
            .map(filename => {
                const filePath = path.join(docsPath, filename);
                const stats = fs.statSync(filePath);

                return {
                    name: filename,
                    size: stats.size,
                    modified: stats.mtime,
                    path: `/documentos/MALLA_2025G/${filename}`
                };
            });

        res.json({ files });
    } catch (error) {
        console.error('Error al listar archivos:', error);
        res.status(500).json({ error: 'Error al listar archivos' });
    }
});

// Endpoint para eliminar archivos
app.delete('/api/files/:filename', (req, res) => {
    try {
        const filename = req.params.filename;
        const filePath = path.join(__dirname, 'documentos', 'MALLA_2025G', filename);

        if (!fs.existsSync(filePath)) {
            return res.status(404).json({ error: 'Archivo no encontrado' });
        }

        fs.unlinkSync(filePath);
        console.log(`🗑️  Archivo eliminado: ${filename}`);

        res.json({ success: true, message: 'Archivo eliminado correctamente' });
    } catch (error) {
        console.error('Error al eliminar archivo:', error);
        res.status(500).json({ error: 'Error al eliminar archivo' });
    }
});

// Servir archivos estáticos
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════════════════════╗
║                                                        ║
║   🚀 Servidor de Documentos MALLA 2025G               ║
║                                                        ║
║   📡 Servidor corriendo en: http://localhost:${PORT}    ║
║                                                        ║
║   Páginas disponibles:                                ║
║   • Dashboard:  http://localhost:${PORT}/               ║
║   • Subir:      http://localhost:${PORT}/upload.html   ║
║   • Documentos: http://localhost:${PORT}/documentos.html║
║                                                        ║
╚════════════════════════════════════════════════════════╝
    `);
});

// Manejo de errores
app.use((error, req, res, next) => {
    console.error('Error del servidor:', error);
    res.status(500).json({ error: 'Error interno del servidor' });
});
