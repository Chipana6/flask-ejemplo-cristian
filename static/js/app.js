// ============================================
// APP.JS - Script general de la app Flask
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('✅ Flask Ejemplo cargado correctamente');

    // Resaltar el enlace activo del navbar
    const enlaces = document.querySelectorAll('.navbar .menu a');
    const rutaActual = window.location.pathname;

    enlaces.forEach(enlace => {
        const href = enlace.getAttribute('href');
        if (href === rutaActual) {
            enlace.classList.add('activo');
        }
    });

    // Animación simple de entrada en las tarjetas
    const tarjetas = document.querySelectorAll('.tarjeta');
    tarjetas.forEach((tarjeta, i) => {
        tarjeta.style.opacity = '0';
        tarjeta.style.transform = 'translateY(20px)';
        setTimeout(() => {
            tarjeta.style.transition = 'all 0.5s ease';
            tarjeta.style.opacity = '1';
            tarjeta.style.transform = 'translateY(0)';
        }, i * 150);
    });

    // Confirmación al enviar formulario
    const form = document.querySelector('.formulario');
    if (form) {
        form.addEventListener('submit', (e) => {
            const boton = form.querySelector('button[type="submit"]');
            boton.textContent = 'Enviando...';
            boton.disabled = true;
        });
    }
});