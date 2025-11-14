// Configuración para GitHub API
const CONFIG = {
    // Configuración del repositorio
    owner: 'Xamplix',
    repo: 'proyecto',
    branch: 'main', // o 'master' según tu rama principal
    docsPath: 'documentos/MALLA_2025G',

    // Token de acceso de GitHub
    // IMPORTANTE: Obtén tu token en https://github.com/settings/tokens
    // Necesitas permisos: repo (Full control of private repositories)
    githubToken: localStorage.getItem('github_token') || '',

    // API de GitHub
    apiBase: 'https://api.github.com',

    // Métodos auxiliares
    setToken(token) {
        this.githubToken = token;
        localStorage.setItem('github_token', token);
    },

    hasToken() {
        return !!this.githubToken;
    },

    getHeaders() {
        return {
            'Authorization': `token ${this.githubToken}`,
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        };
    },

    getRepoUrl() {
        return `${this.apiBase}/repos/${this.owner}/${this.repo}`;
    },

    getContentsUrl(path) {
        return `${this.getRepoUrl()}/contents/${path}`;
    }
};

// Verificar si hay token al cargar
if (!CONFIG.hasToken()) {
    console.warn('No hay token de GitHub configurado. Usa CONFIG.setToken("tu-token") o configúralo en la interfaz.');
}
