/**
 * ENTRAMADOS ESTUDIO - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
  initMobileMenu();
  initSmoothScroll();
  initFormValidation();
  initBackToTop();
  initNewsletterForm();
});

/**
 * Mobile Menu Toggle
 */
function initMobileMenu() {
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('.nav-mobile');

  if (!menuToggle || !mobileNav) return;

  menuToggle.addEventListener('click', function() {
    this.classList.toggle('active');
    mobileNav.classList.toggle('active');
    document.body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
  });

  // Close mobile menu when clicking a link
  const mobileLinks = mobileNav.querySelectorAll('a');
  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      menuToggle.classList.remove('active');
      mobileNav.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

  // Close mobile menu on resize (desktop breakpoint)
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 1024) {
      menuToggle.classList.remove('active');
      mobileNav.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
}

/**
 * Smooth Scroll for anchor links
 */
function initSmoothScroll() {
  const links = document.querySelectorAll('a[href^="#"]');

  links.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');

      if (href === '#') return;

      const target = document.querySelector(href);

      if (target) {
        e.preventDefault();
        const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
        const targetPosition = target.getBoundingClientRect().top + window.scrollY - headerHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

/**
 * Contact Form Validation & Submission
 */
function initFormValidation() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    const name = form.querySelector('[name="name"]');
    const email = form.querySelector('[name="email"]');
    const message = form.querySelector('[name="message"]');
    
    let isValid = true;

    // Basic required validation
    [name, email, message].forEach(field => {
      if (!field || !field.value.trim()) {
        isValid = false;
        field && field.classList.add('error');
      } else {
        field && field.classList.remove('error');
      }
    });

    // Email format validation
    if (email && email.value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email.value)) {
        isValid = false;
        email.classList.add('error');
      }
    }

    if (isValid) {
      // Show success message
      const successEl = document.getElementById('formSuccess');
      form.style.display = 'none';
      if (successEl) {
        successEl.classList.add('show');
      }

      // Reset after 5 seconds
      setTimeout(() => {
        form.reset();
        form.style.display = 'block';
        if (successEl) {
          successEl.classList.remove('show');
        }
      }, 5000);
    }
  });

  // Remove error styling on input
  const inputs = form.querySelectorAll('input, textarea');
  inputs.forEach(input => {
    input.addEventListener('input', () => {
      input.classList.remove('error');
    });
  });
}

/**
 * Newsletter Form
 */
function initNewsletterForm() {
  const form = document.getElementById('newsletterForm');
  if (!form) return;

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    const emailInput = form.querySelector('input[type="email"]');
    if (!emailInput || !emailInput.value.trim()) return;

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailInput.value)) return;

    // Visual feedback
    const btn = form.querySelector('button');
    const originalText = btn.textContent;
    btn.textContent = '¡Listo!';
    btn.style.background = '#25D366';
    btn.style.borderColor = '#25D366';

    setTimeout(() => {
      form.reset();
      btn.textContent = originalText;
      btn.style.background = '';
      btn.style.borderColor = '';
    }, 3000);
  });
}

/**
 * Back to Top Button
 */
function initBackToTop() {
  const backToTopBtn = document.getElementById('backToTop');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  }, { passive: true });

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}
