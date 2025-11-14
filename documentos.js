// documentos.js - Gestión y visualización de documentos

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

        this.setupEventListeners();
        this.loadDocuments();
    }

    setupEventListeners() {
        this.searchInput.addEventListener('input', (e) => {
            this.filterDocuments(e.target.value);
        });
    }

    async loadDocuments() {
        try {
            const response = await fetch('/api/files');

            if (!response.ok) {
                throw new Error('Error al cargar documentos');
            }

            const data = await response.json();
            this.documents = data.files || [];
            this.filteredDocuments = [...this.documents];

            this.updateStats();
            this.renderDocuments();
        } catch (error) {
            console.error('Error:', error);
            this.showStatus('Error: Asegúrate de que el servidor esté en ejecución (ejecuta: npm start)', 'error');
            this.renderEmptyState('Error al cargar documentos. Verifica que el servidor esté corriendo.');
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
        // Total archivos
        this.totalFiles.textContent = this.documents.length;

        // Tamaño total
        const totalBytes = this.documents.reduce((sum, doc) => sum + doc.size, 0);
        this.totalSize.textContent = this.formatFileSize(totalBytes);

        // Última actualización
        if (this.documents.length > 0) {
            const latestDate = new Date(
                Math.max(...this.documents.map(doc => new Date(doc.modified)))
            );
            this.lastUpdate.textContent = this.formatDate(latestDate);
        } else {
            this.lastUpdate.textContent = '-';
        }
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

        // Ordenar por fecha de modificación (más reciente primero)
        const sortedDocs = [...this.filteredDocuments].sort((a, b) =>
            new Date(b.modified) - new Date(a.modified)
        );

        this.documentsList.innerHTML = sortedDocs.map(doc => `
            <div class="document-item">
                <div class="document-info">
                    <div class="document-icon">${this.getFileIcon(doc.name)}</div>
                    <div class="document-details">
                        <div class="document-name">${doc.name}</div>
                        <div class="document-meta">
                            <span>📦 ${this.formatFileSize(doc.size)}</span>
                            <span>📅 ${this.formatDate(new Date(doc.modified))}</span>
                        </div>
                    </div>
                </div>
                <div class="document-actions">
                    <a href="${doc.path}" download class="btn btn-primary btn-small">
                        Descargar
                    </a>
                    <a href="${doc.path}" target="_blank" class="btn btn-secondary btn-small">
                        Ver
                    </a>
                    <button class="btn btn-danger btn-small" onclick="documentManager.deleteDocument('${doc.name}')">
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

    async deleteDocument(filename) {
        if (!confirm(`¿Estás seguro de que deseas eliminar "${filename}"?`)) {
            return;
        }

        try {
            const response = await fetch(`/api/files/${encodeURIComponent(filename)}`, {
                method: 'DELETE'
            });

            if (!response.ok) {
                throw new Error('Error al eliminar documento');
            }

            this.showStatus('Documento eliminado correctamente', 'success');
            this.loadDocuments();
        } catch (error) {
            console.error('Error:', error);
            this.showStatus('Error al eliminar el documento', 'error');
        }
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
            svg: '🖼️',
            zip: '📦',
            rar: '📦',
            '7z': '📦',
            txt: '📄',
            md: '📄',
            csv: '📊',
            json: '📋',
            xml: '📋',
            mp4: '🎥',
            avi: '🎥',
            mov: '🎥',
            mp3: '🎵',
            wav: '🎵',
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

    formatDate(date) {
        const now = new Date();
        const diff = now - date;
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));

        if (days === 0) {
            const hours = Math.floor(diff / (1000 * 60 * 60));
            if (hours === 0) {
                const minutes = Math.floor(diff / (1000 * 60));
                return minutes <= 1 ? 'Ahora' : `Hace ${minutes} min`;
            }
            return `Hace ${hours}h`;
        } else if (days === 1) {
            return 'Ayer';
        } else if (days < 7) {
            return `Hace ${days} días`;
        } else {
            return date.toLocaleDateString('es-ES', {
                year: 'numeric',
                month: 'short',
                day: 'numeric'
            });
        }
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
