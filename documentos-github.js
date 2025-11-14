// documentos-github.js - Gestión y visualización de documentos usando GitHub API

class DocumentManager {
    constructor() {
        this.documents = [];
        this.filteredDocuments = [];
        this.init();
    }

    init() {
        this.documentsList = document.getElementById('documentsList');
        this.searchInput = document.getElementById('searchInput');
        this.statusMessage = document.getElementById('statusMessage');
        this.totalFiles = document.getElementById('totalFiles');
        this.totalSize = document.getElementById('totalSize');
        this.lastUpdate = document.getElementById('lastUpdate');

        this.checkToken();
        this.setupEventListeners();
        this.loadDocuments();
    }

    checkToken() {
        if (!CONFIG.hasToken()) {
            this.showStatus('⚠️ Token de GitHub no configurado. Ve a la página de Subir para configurarlo.', 'error');
        }
    }

    setupEventListeners() {
        this.searchInput.addEventListener('input', (e) => {
            this.filterDocuments(e.target.value);
        });
    }

    async loadDocuments() {
        try {
            if (!CONFIG.hasToken()) {
                this.renderEmptyState('Por favor configura tu token de GitHub en la página de Subir.');
                return;
            }

            this.documentsList.innerHTML = '<div class="loading">Cargando documentos desde GitHub...</div>';

            const response = await fetch(CONFIG.getContentsUrl(CONFIG.docsPath), {
                headers: CONFIG.getHeaders()
            });

            if (!response.ok) {
                if (response.status === 404) {
                    this.documents = [];
                    this.filteredDocuments = [];
                    this.updateStats();
                    this.renderEmptyState('La carpeta de documentos aún no existe. Sube tu primer archivo para crearla.');
                    return;
                }
                throw new Error(`Error ${response.status}: ${response.statusText}`);
            }

            const contents = await response.json();

            // Filtrar solo archivos (no directorios) y excluir README
            this.documents = contents
                .filter(item => item.type === 'file' && item.name !== 'README.md')
                .map(item => ({
                    name: item.name,
                    size: item.size,
                    sha: item.sha,
                    path: item.path,
                    downloadUrl: item.download_url,
                    htmlUrl: item.html_url
                }));

            this.filteredDocuments = [...this.documents];
            this.updateStats();
            this.renderDocuments();

        } catch (error) {
            console.error('Error:', error);
            this.showStatus(`Error al cargar documentos: ${error.message}`, 'error');
            this.renderEmptyState(`Error al cargar documentos: ${error.message}`);
        }
    }

    filterDocuments(searchTerm) {
        const term = searchTerm.toLowerCase();
        this.filteredDocuments = this.documents.filter(doc =>
            doc.name.toLowerCase().includes(term)
        );
        this.renderDocuments();
    }

    updateStats() {
        this.totalFiles.textContent = this.documents.length;

        const totalBytes = this.documents.reduce((sum, doc) => sum + doc.size, 0);
        this.totalSize.textContent = this.formatFileSize(totalBytes);

        this.lastUpdate.textContent = 'Ahora';
    }

    renderDocuments() {
        if (this.filteredDocuments.length === 0) {
            if (this.documents.length === 0) {
                this.renderEmptyState('No hay documentos aún. ¡Sube tu primer documento!');
            } else {
                this.renderEmptyState('No se encontraron documentos con ese criterio de búsqueda.');
            }
            return;
        }

        // Ordenar alfabéticamente
        const sortedDocs = [...this.filteredDocuments].sort((a, b) =>
            a.name.localeCompare(b.name)
        );

        this.documentsList.innerHTML = sortedDocs.map(doc => `
            <div class="document-item">
                <div class="document-info">
                    <div class="document-icon">${this.getFileIcon(doc.name)}</div>
                    <div class="document-details">
                        <div class="document-name">${doc.name}</div>
                        <div class="document-meta">
                            <span>📦 ${this.formatFileSize(doc.size)}</span>
                            <span>💾 GitHub</span>
                        </div>
                    </div>
                </div>
                <div class="document-actions">
                    <a href="${doc.downloadUrl}" download class="btn btn-primary btn-small">
                        Descargar
                    </a>
                    <a href="${doc.htmlUrl}" target="_blank" class="btn btn-secondary btn-small">
                        Ver en GitHub
                    </a>
                    <button class="btn btn-danger btn-small" onclick="documentManager.deleteDocument('${doc.name}', '${doc.sha}')">
                        Eliminar
                    </button>
                </div>
            </div>
        `).join('');
    }

    renderEmptyState(message) {
        this.documentsList.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">📭</div>
                <div class="empty-state-text">${message}</div>
                <div class="empty-state-hint">
                    <a href="upload.html" class="btn btn-success" style="margin-top: 20px;">
                        Subir Documentos
                    </a>
                </div>
            </div>
        `;
    }

    async deleteDocument(filename, sha) {
        if (!confirm(`¿Estás seguro de que deseas eliminar "${filename}"?`)) {
            return;
        }

        if (!CONFIG.hasToken()) {
            this.showStatus('Necesitas configurar tu token de GitHub', 'error');
            return;
        }

        try {
            const filePath = `${CONFIG.docsPath}/${filename}`;

            const response = await fetch(CONFIG.getContentsUrl(filePath), {
                method: 'DELETE',
                headers: CONFIG.getHeaders(),
                body: JSON.stringify({
                    message: `Delete: ${filename}`,
                    sha: sha,
                    branch: CONFIG.branch
                })
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.message || 'Error al eliminar documento');
            }

            this.showStatus('✅ Documento eliminado correctamente de GitHub', 'success');
            this.loadDocuments();
        } catch (error) {
            console.error('Error:', error);
            this.showStatus(`Error al eliminar el documento: ${error.message}`, 'error');
        }
    }

    getFileIcon(filename) {
        const ext = filename.split('.').pop().toLowerCase();
        const icons = {
            pdf: '📕', doc: '📘', docx: '📘', xls: '📗', xlsx: '📗',
            ppt: '📙', pptx: '📙', jpg: '🖼️', jpeg: '🖼️', png: '🖼️',
            gif: '🖼️', svg: '🖼️', zip: '📦', rar: '📦', '7z': '📦',
            txt: '📄', md: '📄', csv: '📊', json: '📋', xml: '📋',
            mp4: '🎥', avi: '🎥', mov: '🎥', mp3: '🎵', wav: '🎵',
            default: '📄'
        };
        return icons[ext] || icons.default;
    }

    formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
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
const documentManager = new DocumentManager();
