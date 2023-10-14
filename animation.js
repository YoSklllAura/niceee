document.addEventListener('DOMContentLoaded', function() {
    animateText();
    
    // Add smooth scrolling to anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const target = document.querySelector(this.getAttribute('href'));
            target.scrollIntoView({
                behavior: 'smooth'
            });
            
            // Hide other sections
            document.querySelectorAll('section').forEach(section => {
                if (section !== target) {
                    section.classList.add('hidden');
                }
            });

            // Show the target section
            target.classList.remove('hidden');
        });
    });
});

function animateText() {
    const textElement = document.querySelector('.animated-text');
    const text = textElement.innerText;
    textElement.innerHTML = '';

    for (let i = 0; i < text.length; i++) {
        const char = text.charAt(i);
        const span = document.createElement('span');
        span.style.animationDelay = `${i * 0.1}s`;
        span.textContent = (char === ' ') ? '\u00A0' : char;
        textElement.appendChild(span);
    }
}
