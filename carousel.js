/**
 * Script pour le carousel automatique des services
 * Animation continue de droite à gauche
 */

document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('servicesCarousel');
    
    if (carousel) {
        // Dupliquer les cartes pour créer un effet de boucle infinie
        const cards = carousel.innerHTML;
        carousel.innerHTML = cards + cards + cards; // Triple pour effet infini fluide
        
        // Gérer la pause au survol (optionnel)
        const carouselWrapper = carousel.parentElement;
        let animationPaused = false;
        
        carouselWrapper.addEventListener('mouseenter', function() {
            if (!animationPaused) {
                carousel.style.animationPlayState = 'paused';
                animationPaused = true;
            }
        });
        
        carouselWrapper.addEventListener('mouseleave', function() {
            if (animationPaused) {
                carousel.style.animationPlayState = 'running';
                animationPaused = false;
            }
        });
        
        // Reset de l'animation quand elle atteint la fin (pour éviter les sauts)
        carousel.addEventListener('animationiteration', function() {
            // Cette fonction est appelée à chaque itération de l'animation
            // Le CSS gère déjà la répétition infinie, donc pas besoin d'action supplémentaire
        });
    }
});







