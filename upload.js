// upload.js - Gestión de subida de documentos

class DocumentUploader {
    constructor() {
        this.files = [];
        this.init();
    }

    init() {
        this.dropZone = document.getElementById('dropZone');
        this.fileInput = document.getElementById('fileInput');
        this.filesList = document.getElementById('filesList');
        this.uploadProgress = document.getElementById('uploadProgress');
        this.uploadProgressBar = document.getElementById('uploadProgressBar');
        this.statusMessage = document.getElementById('statusMessage');

        this.setupEventListeners();
        this.renderFilesList();
    }

    setupEventListeners() {
        // Click en drop zone
        this.dropZone.addEventListener('click', () => {
            this.fileInput.click();
        });

        // Drag & Drop
        this.dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            this.dropZone.classList.add('drag-over');
        });

        this.dropZone.addEventListener('dragleave', () => {
            this.dropZone.classList.remove('drag-over');
        });

        this.dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            this.dropZone.classList.remove('drag-over');
            const files = Array.from(e.dataTransfer.files);
            this.addFiles(files);
        });

        // File input change
        this.fileInput.addEventListener('change', (e) => {
            const files = Array.from(e.target.files);
            this.addFiles(files);
            e.target.value = ''; // Reset input
        });
    }

    addFiles(newFiles) {
        newFiles.forEach(file => {
            // Verificar si el archivo ya existe
            const exists = this.files.some(f => f.name === file.name && f.size === file.size);
            if (!exists) {
                this.files.push({
                    file: file,
                    name: file.name,
                    size: file.size,
                    type: file.type,
                    id: Date.now() + Math.random()
                });
            }
        });
        this.renderFilesList();
        this.showStatus(`${newFiles.length} archivo(s) agregado(s)`, 'success');
    }

    removeFile(id) {
        this.files = this.files.filter(f => f.id !== id);
        this.renderFilesList();
        this.showStatus('Archivo eliminado', 'success');
    }

    formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
    }

    getFileIcon(filename) {
        const ext = filename.split('.').pop().toLowerCase();
        const icons = {
            pdf: '📕',
            doc: '📘',
            docx: '📘',
            xls: '📗',
            xlsx: '📗',
            ppt: '📙',
            pptx: '📙',
            jpg: '🖼️',
            jpeg: '🖼️',
            png: '🖼️',
            gif: '🖼️',
            zip: '📦',
            rar: '📦',
            txt: '📄',
            default: '📄'
        };
        return icons[ext] || icons.default;
    }

    renderFilesList() {
        if (this.files.length === 0) {
            this.filesList.innerHTML = `
                <div class="empty-state">
                    <div class="empty-state-icon">📭</div>
                    <div>No hay archivos seleccionados</div>
                </div>
            `;
            return;
        }

        this.filesList.innerHTML = this.files.map(fileData => `
            <div class="file-item">
                <div class="file-info">
                    <div class="file-icon">${this.getFileIcon(fileData.name)}</div>
                    <div class="file-details">
                        <div class="file-name">${fileData.name}</div>
                        <div class="file-size">${this.formatFileSize(fileData.size)}</div>
                    </div>
                </div>
                <div class="file-actions">
                    <button class="btn btn-danger btn-small" onclick="uploader.removeFile(${fileData.id})">
                        Eliminar
                    </button>
                </div>
            </div>
        `).join('');

        // Agregar botón de subir si hay archivos
        const uploadButton = document.createElement('div');
        uploadButton.style.marginTop = '20px';
        uploadButton.style.textAlign = 'center';
        uploadButton.innerHTML = `
            <button class="btn btn-primary" onclick="uploader.uploadFiles()">
                Subir ${this.files.length} archivo(s) al servidor
            </button>
        `;
        this.filesList.appendChild(uploadButton);
    }

    showStatus(message, type) {
        this.statusMessage.textContent = message;
        this.statusMessage.className = `status-message ${type} show`;
        setTimeout(() => {
            this.statusMessage.classList.remove('show');
        }, 5000);
    }

    async uploadFiles() {
        if (this.files.length === 0) {
            this.showStatus('No hay archivos para subir', 'error');
            return;
        }

        this.uploadProgress.style.display = 'block';
        this.uploadProgressBar.style.width = '0%';

        const formData = new FormData();
        this.files.forEach((fileData, index) => {
            formData.append('files', fileData.file);
        });

        try {
            // Simular progreso
            let progress = 0;
            const progressInterval = setInterval(() => {
                progress += 10;
                this.uploadProgressBar.style.width = progress + '%';
                if (progress >= 90) clearInterval(progressInterval);
            }, 100);

            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            clearInterval(progressInterval);
            this.uploadProgressBar.style.width = '100%';

            if (response.ok) {
                const result = await response.json();
                this.showStatus(`${this.files.length} archivo(s) subido(s) correctamente`, 'success');
                this.files = [];
                this.renderFilesList();

                setTimeout(() => {
                    this.uploadProgress.style.display = 'none';
                    this.uploadProgressBar.style.width = '0%';
                }, 2000);
            } else {
                throw new Error('Error al subir archivos');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showStatus('Error: Asegúrate de que el servidor esté en ejecución (ejecuta: node server.js)', 'error');
            this.uploadProgressBar.style.width = '0%';
            setTimeout(() => {
                this.uploadProgress.style.display = 'none';
            }, 2000);
        }
    }
}

// Inicializar
const uploader = new DocumentUploader();
