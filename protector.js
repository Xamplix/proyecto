// js/protector.js
(function() {
    // URL encriptada en base64 y dividida
    const urlParts = [
        'aHR0cHM6Ly9hcHAucG93ZX',
        'JiaS5jb20vdmlldz9yPWV5Sn',
        'JJam9pTURjMU16RmxZekF0WV',
        'RNNE55MDBPRGsyTFdFM1lqSXR',
        'OelZpTUROaE9EZ3laRE16SWl3',
        'aWRDSTZJbUZsVFRRMFlUVTNMV',
        '0ZsWTJJdE5HSm1PUzA0TWpo',
        'aExUWmlOVEl3TnpNeVlqRXhNQ0o5'
    ];

    function createIframe() {
        const container = document.getElementById('iframe-container');
        const iframe = document.createElement('iframe');
        
        Object.assign(iframe, {
            width: '1024',
            height: '1060',
            frameBorder: '0',
            allowFullscreen: true
        });

        iframe.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-popups allow-downloads');
        
        // Decodificar y asignar URL
        iframe.src = atob(urlParts.join(''));
        
        container.appendChild(iframe);
    }

    // Medidas de protección
    document.addEventListener('contextmenu', e => e.preventDefault());
    document.addEventListener('keydown', e => {
        // Deshabilitar F12, Ctrl+Shift+I, Ctrl+U
        if (
            e.keyCode === 123 || 
            (e.ctrlKey && e.shiftKey && e.keyCode === 73) ||
            (e.ctrlKey && e.keyCode === 85)
        ) {
            e.preventDefault();
        }
    });

    // Inicializar con retraso
    setTimeout(createIframe, 100);
})();