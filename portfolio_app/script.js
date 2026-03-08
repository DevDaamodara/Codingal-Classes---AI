/* ============================================
   PORTFOLIO WEBSITE - JAVASCRIPT
   Interactive Features & Animations
   ============================================ */

// ============================================
// DOM ELEMENTS
// ============================================

const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

// ============================================
// MOBILE MENU TOGGLE
// ============================================

/**
 * Toggle mobile navigation menu
 */
function toggleMobileMenu() {
    navMenu.classList.toggle('active');
    
    // Animate hamburger
    hamburger.style.transition = 'all 0.3s ease-in-out';
}

/**
 * Close mobile menu when a link is clicked
 */
function closeMobileMenu() {
    navMenu.classList.remove('active');
}

// Event listeners for mobile menu
hamburger.addEventListener('click', toggleMobileMenu);
navLinks.forEach(link => {
    link.addEventListener('click', closeMobileMenu);
});

// ============================================
// SMOOTH SCROLL NAVIGATION
// ============================================

/**
 * Smooth scroll to section with offset for fixed navbar
 */
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        
        if (targetSection) {
            const navHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = targetSection.offsetTop - navHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ============================================
// SCROLL ANIMATIONS
// ============================================

/**
 * Intersection Observer for scroll animations
 * Triggers animations when elements come into view
 */
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe skill cards and project cards
document.querySelectorAll('.skill-card, .project-card').forEach(card => {
    card.style.opacity = '0';
    observer.observe(card);
});

// ============================================
// PROGRESS BAR ANIMATION
// ============================================

/**
 * Animate progress bars when they come into view
 */
const progressObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const progressBar = entry.target.querySelector('.progress');
            if (progressBar) {
                progressBar.style.animation = 'fillProgress 1.5s ease-out forwards';
            }
            progressObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.skill-card').forEach(card => {
    progressObserver.observe(card);
});

// ============================================
// CONTACT FORM HANDLING
// ============================================

/**
 * Handle contact form submission
 * Validates form data and displays success/error message
 */
contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Get form values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const subject = document.getElementById('subject').value.trim();
    const message = document.getElementById('message').value.trim();
    
    // Validate form
    if (!name || !email || !subject || !message) {
        showFormMessage('Please fill in all fields', 'error');
        return;
    }
    
    // Validate email format
    if (!isValidEmail(email)) {
        showFormMessage('Please enter a valid email address', 'error');
        return;
    }
    
    // Simulate form submission (frontend only)
    // In a real application, this would send data to a backend server
    showFormMessage('Message sent successfully! I\'ll get back to you soon.', 'success');
    
    // Reset form
    contactForm.reset();
    
    // Clear message after 5 seconds
    setTimeout(() => {
        formMessage.classList.remove('success', 'error');
        formMessage.textContent = '';
    }, 5000);
});

/**
 * Display form message with styling
 * @param {string} message - Message text to display
 * @param {string} type - Message type: 'success' or 'error'
 */
function showFormMessage(message, type) {
    formMessage.textContent = message;
    formMessage.className = `form-message ${type}`;
}

/**
 * Validate email format
 * @param {string} email - Email address to validate
 * @returns {boolean} - True if email is valid
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// ============================================
// NAVBAR SCROLL EFFECT
// ============================================

/**
 * Add shadow to navbar on scroll
 */
let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop > 50) {
        navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
    } else {
        navbar.style.boxShadow = 'none';
    }
    
    lastScrollTop = scrollTop;
});

// ============================================
// ACTIVE NAV LINK HIGHLIGHTING
// ============================================

/**
 * Highlight active navigation link based on scroll position
 */
window.addEventListener('scroll', () => {
    let current = '';
    
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.style.color = 'var(--primary-color)';
        } else {
            link.style.color = 'var(--text-secondary)';
        }
    });
});

// ============================================
// SCROLL TO TOP BUTTON (Optional Enhancement)
// ============================================

/**
 * Create and manage scroll-to-top button
 */
function initScrollToTop() {
    // Create button element
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.innerHTML = '↑';
    scrollTopBtn.className = 'scroll-to-top';
    scrollTopBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        border: none;
        border-radius: 50%;
        font-size: 24px;
        cursor: pointer;
        display: none;
        z-index: 999;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    `;
    
    document.body.appendChild(scrollTopBtn);
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollTopBtn.style.display = 'flex';
            scrollTopBtn.style.alignItems = 'center';
            scrollTopBtn.style.justifyContent = 'center';
        } else {
            scrollTopBtn.style.display = 'none';
        }
    });
    
    // Scroll to top on click
    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Hover effect
    scrollTopBtn.addEventListener('mouseover', () => {
        scrollTopBtn.style.transform = 'translateY(-5px)';
    });
    
    scrollTopBtn.addEventListener('mouseout', () => {
        scrollTopBtn.style.transform = 'translateY(0)';
    });
}

// Initialize scroll-to-top button
initScrollToTop();

// ============================================
// PARALLAX EFFECT (Subtle)
// ============================================

/**
 * Add subtle parallax effect to hero section
 */
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero');
    const scrollPosition = window.pageYOffset;
    
    if (scrollPosition < window.innerHeight) {
        hero.style.backgroundPosition = `0 ${scrollPosition * 0.5}px`;
    }
});

// ============================================
// INTERSECTION OBSERVER FOR LAZY ANIMATIONS
// ============================================

/**
 * Animate stat cards when they come into view
 */
const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statCard = entry.target;
            statCard.style.animation = 'fadeInUp 0.6s ease-out forwards';
            statObserver.unobserve(statCard);
        }
    });
}, { threshold: 0.3 });

document.querySelectorAll('.stat-card').forEach(card => {
    card.style.opacity = '0';
    statObserver.observe(card);
});

// ============================================
// KEYBOARD NAVIGATION
// ============================================

/**
 * Handle keyboard navigation
 * Escape key closes mobile menu
 */
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeMobileMenu();
    }
});

// ============================================
// PERFORMANCE OPTIMIZATION
// ============================================

/**
 * Debounce function to optimize scroll events
 * @param {Function} func - Function to debounce
 * @param {number} wait - Wait time in milliseconds
 * @returns {Function} - Debounced function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ============================================
// INITIALIZATION
// ============================================

/**
 * Initialize all interactive features
 */
function init() {
    console.log('Portfolio website initialized successfully');
    
    // Add any additional initialization code here
    // For example: load external data, initialize plugins, etc.
}

// Run initialization when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

// ============================================
// UTILITY FUNCTIONS
// ============================================

/**
 * Check if element is in viewport
 * @param {Element} element - Element to check
 * @returns {boolean} - True if element is in viewport
 */
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

/**
 * Add class to element with animation
 * @param {Element} element - Element to animate
 * @param {string} className - Class name to add
 */
function animateElement(element, className) {
    element.classList.add(className);
    element.addEventListener('animationend', () => {
        element.classList.remove(className);
    }, { once: true });
}

// ============================================
// END OF SCRIPT
// ============================================
