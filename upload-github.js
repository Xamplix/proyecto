// upload-github.js - Gestión de subida de documentos usando GitHub API

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

        this.checkToken();
        this.setupEventListeners();
        this.renderFilesList();
    }

    checkToken() {
        if (!CONFIG.hasToken()) {
            this.showTokenPrompt();
        }
    }

    showTokenPrompt() {
        const modal = document.createElement('div');
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.8);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
        `;

        modal.innerHTML = `
            <div style="background: white; padding: 40px; border-radius: 10px; max-width: 600px; width: 90%;">
                <h2 style="margin-top: 0; color: #333;">🔑 Configurar Token de GitHub</h2>
                <p style="color: #666; margin-bottom: 20px;">
                    Para subir archivos, necesitas un token de acceso personal de GitHub.
                </p>
                <ol style="color: #666; text-align: left; margin-bottom: 20px;">
                    <li>Ve a <a href="https://github.com/settings/tokens" target="_blank" style="color: #667eea;">GitHub Settings → Tokens</a></li>
                    <li>Click en "Generate new token (classic)"</li>
                    <li>Marca el permiso <strong>repo</strong> (Full control)</li>
                    <li>Copia el token generado</li>
                    <li>Pégalo aquí abajo:</li>
                </ol>
                <input type="password" id="tokenInput" placeholder="ghp_xxxxxxxxxxxx"
                    style="width: 100%; padding: 12px; border: 2px solid #e9ecef; border-radius: 5px; margin-bottom: 20px; font-size: 14px;">
                <div style="display: flex; gap: 10px;">
                    <button id="saveToken" style="flex: 1; padding: 12px; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 14px;">
                        Guardar Token
                    </button>
                    <button id="cancelToken" style="padding: 12px 20px; background: #6c757d; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 14px;">
                        Cancelar
                    </button>
                </div>
                <p style="color: #999; font-size: 12px; margin-top: 15px;">
                    ⚠️ El token se guarda en tu navegador (localStorage)
                </p>
            </div>
        `;

        document.body.appendChild(modal);

        document.getElementById('saveToken').addEventListener('click', () => {
            const token = document.getElementById('tokenInput').value.trim();
            if (token) {
                CONFIG.setToken(token);
                document.body.removeChild(modal);
                this.showStatus('Token configurado correctamente', 'success');
            } else {
                alert('Por favor ingresa un token válido');
            }
        });

        document.getElementById('cancelToken').addEventListener('click', () => {
            document.body.removeChild(modal);
            this.showStatus('Necesitas configurar un token para subir archivos', 'error');
        });
    }

    setupEventListeners() {
        this.dropZone.addEventListener('click', () => {
            this.fileInput.click();
        });

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

        this.fileInput.addEventListener('change', (e) => {
            const files = Array.from(e.target.files);
            this.addFiles(files);
            e.target.value = '';
        });
    }

    addFiles(newFiles) {
        newFiles.forEach(file => {
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
            pdf: '📕', doc: '📘', docx: '📘', xls: '📗', xlsx: '📗',
            ppt: '📙', pptx: '📙', jpg: '🖼️', jpeg: '🖼️', png: '🖼️',
            gif: '🖼️', zip: '📦', rar: '📦', txt: '📄', default: '📄'
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

        const uploadButton = document.createElement('div');
        uploadButton.style.marginTop = '20px';
        uploadButton.style.textAlign = 'center';
        uploadButton.innerHTML = `
            <button class="btn btn-primary" onclick="uploader.uploadFiles()">
                📤 Subir ${this.files.length} archivo(s) a GitHub
            </button>
            <button class="btn btn-secondary" onclick="uploader.showTokenPrompt()" style="margin-left: 10px;">
                🔑 Cambiar Token
            </button>
        `;
        this.filesList.appendChild(uploadButton);
    }

    async uploadFiles() {
        if (this.files.length === 0) {
            this.showStatus('No hay archivos para subir', 'error');
            return;
        }

        if (!CONFIG.hasToken()) {
            this.showTokenPrompt();
            return;
        }

        this.uploadProgress.style.display = 'block';
        this.uploadProgressBar.style.width = '0%';

        let uploadedCount = 0;
        const totalFiles = this.files.length;

        for (let i = 0; i < this.files.length; i++) {
            const fileData = this.files[i];
            try {
                await this.uploadToGitHub(fileData.file);
                uploadedCount++;
                const progress = (uploadedCount / totalFiles) * 100;
                this.uploadProgressBar.style.width = progress + '%';
                this.showStatus(`Subiendo: ${uploadedCount}/${totalFiles} archivos...`, 'success');
            } catch (error) {
                console.error('Error subiendo archivo:', fileData.name, error);
                this.showStatus(`Error subiendo ${fileData.name}: ${error.message}`, 'error');
            }
        }

        if (uploadedCount === totalFiles) {
            this.showStatus(`✅ ${uploadedCount} archivo(s) subido(s) correctamente a GitHub`, 'success');
            this.files = [];
            this.renderFilesList();
        } else {
            this.showStatus(`⚠️ ${uploadedCount}/${totalFiles} archivos subidos. Algunos fallaron.`, 'error');
        }

        setTimeout(() => {
            this.uploadProgress.style.display = 'none';
            this.uploadProgressBar.style.width = '0%';
        }, 2000);
    }

    async uploadToGitHub(file) {
        // Leer archivo como base64
        const content = await this.fileToBase64(file);

        // Verificar si el archivo ya existe
        const filePath = `${CONFIG.docsPath}/${file.name}`;
        let sha = null;

        try {
            const checkResponse = await fetch(CONFIG.getContentsUrl(filePath), {
                headers: CONFIG.getHeaders()
            });

            if (checkResponse.ok) {
                const existingFile = await checkResponse.json();
                sha = existingFile.sha;
            }
        } catch (error) {
            // El archivo no existe, está bien
        }

        // Subir o actualizar archivo
        const body = {
            message: `Upload: ${file.name}`,
            content: content,
            branch: CONFIG.branch
        };

        if (sha) {
            body.sha = sha; // Necesario para actualizar archivo existente
        }

        const response = await fetch(CONFIG.getContentsUrl(filePath), {
            method: 'PUT',
            headers: CONFIG.getHeaders(),
            body: JSON.stringify(body)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.message || 'Error al subir archivo');
        }

        return await response.json();
    }

    fileToBase64(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => {
                const base64 = reader.result.split(',')[1];
                resolve(base64);
            };
            reader.onerror = reject;
            reader.readAsDataURL(file);
        });
    }

    showStatus(message, type) {
        this.statusMessage.textContent = message;
        this.statusMessage.className = `status-message ${type} show`;
        setTimeout(() => {
            this.statusMessage.classList.remove('show');
        }, 5000);
    }
}

// Inicializar
const uploader = new DocumentUploader();
