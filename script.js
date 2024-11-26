document.addEventListener('DOMContentLoaded', () => {
    const player = document.querySelector('.player');
    const playerLeg = document.querySelector('.player-leg');
    const ball = document.querySelector('.ball');
    const shotTrail = document.querySelector('.shot-trail');
    const aboutSection = document.querySelector('#about');
    
    let animationTriggered = false;

    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.top <= (window.innerHeight || document.documentElement.clientHeight)
        );
    }

    function startAnimation() {
        if (animationTriggered) return;
        
        // Set initial ball position
        ball.style.left = '200px';
        ball.style.opacity = '1';

        // Start the sequence
        player.classList.add('animate');
        
        setTimeout(() => {
            playerLeg.classList.add('animate');
        }, 1000);

        setTimeout(() => {
            ball.classList.add('animate');
            shotTrail.classList.add('animate');
        }, 1200);

        animationTriggered = true;
    }

    function handleScroll() {
        if (isElementInViewport(aboutSection)) {
            startAnimation();
        }
    }

    window.addEventListener('scroll', handleScroll);

    // Football animation
    const footballer = document.querySelector('.footballer-silhouette');
    const ballShadow = document.querySelector('.ball-shadow');

    let footballAnimationTriggered = false;

    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function animateFootballer() {
        if (!footballAnimationTriggered && isElementInViewport(aboutSection)) {
            footballAnimationTriggered = true;
            
            // Animate footballer
            footballer.style.transition = 'transform 1s ease-out';
            footballer.style.transform = 'scale(1.2) translateX(-100px)';
            
            // Animate ball
            ballShadow.style.transition = 'transform 1.5s cubic-bezier(0.17, 0.67, 0.83, 0.67)';
            ballShadow.style.transform = 'translateX(200px) rotate(720deg)';
            
            // Reset animation after completion
            setTimeout(() => {
                footballer.style.transition = 'transform 0.5s ease';
                footballer.style.transform = 'scale(1.2)';
                
                ballShadow.style.transition = 'transform 0.5s ease';
                ballShadow.style.transform = 'translateX(-50%)';
                
                footballAnimationTriggered = false;
            }, 2000);
        }
    }

    window.addEventListener('scroll', () => {
        requestAnimationFrame(animateFootballer);
    });
});
