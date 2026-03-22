/**
 * ENTRAMADOS ESTUDIO - Main JavaScript
 * =====================================
 */

document.addEventListener('DOMContentLoaded', function() {
  initHeader();
  initMobileMenu();
  initSmoothScroll();
  initScrollAnimations();
  initFormValidation();
  initBackToTop();
});

/**
 * Header scroll effect
 */
function initHeader() {
  const header = document.querySelector('.header');
  if (!header) return;

  let lastScrollY = window.scrollY;

  const handleScroll = () => {
    const currentScrollY = window.scrollY;

    if (currentScrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    lastScrollY = currentScrollY;
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
}

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

      // Skip if it's just "#"
      if (href === '#') return;

      const target = document.querySelector(href);

      if (target) {
        e.preventDefault();
        const headerHeight = document.querySelector('.header')?.offsetHeight || 80;
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
 * Scroll Animations using Intersection Observer
 */
function initScrollAnimations() {
  const animatedElements = document.querySelectorAll('.animate-on-scroll');

  if (!animatedElements.length) return;

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -80px 0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  animatedElements.forEach(el => observer.observe(el));
}

/**
 * Form Validation
 */
function initFormValidation() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const inputs = form.querySelectorAll('input, textarea');

  // Real-time validation
  inputs.forEach(input => {
    input.addEventListener('blur', () => validateField(input));
    input.addEventListener('input', () => {
      if (input.parentElement.classList.contains('error')) {
        validateField(input);
      }
    });
  });

  // Form submission
  form.addEventListener('submit', function(e) {
    e.preventDefault();

    let isValid = true;

    inputs.forEach(input => {
      if (!validateField(input)) {
        isValid = false;
      }
    });

    if (isValid) {
      // Simulate form submission
      const formContent = form.querySelector('.form-content');
      const formSuccess = form.querySelector('.form-success');

      if (formContent && formSuccess) {
        formContent.style.display = 'none';
        formSuccess.classList.add('show');

        // Reset form after delay (optional)
        setTimeout(() => {
          form.reset();
          formContent.style.display = 'block';
          formSuccess.classList.remove('show');
        }, 5000);
      }
    }
  });
}

function validateField(field) {
  const parent = field.parentElement;
  const errorElement = parent.querySelector('.form-error');
  let isValid = true;
  let errorMessage = '';

  // Remove existing error state
  parent.classList.remove('error');

  // Check if required and empty
  if (field.hasAttribute('required') && !field.value.trim()) {
    isValid = false;
    errorMessage = 'Este campo es requerido';
  }

  // Email validation
  if (field.type === 'email' && field.value.trim()) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(field.value)) {
      isValid = false;
      errorMessage = 'Ingresa un correo electrónico válido';
    }
  }

  // Phone validation
  if (field.type === 'tel' && field.value.trim()) {
    const phoneRegex = /^[\d\s\-\+\(\)]{8,}$/;
    if (!phoneRegex.test(field.value)) {
      isValid = false;
      errorMessage = 'Ingresa un número de teléfono válido';
    }
  }

  // Apply error state if invalid
  if (!isValid) {
    parent.classList.add('error');
    if (errorElement) {
      errorElement.textContent = errorMessage;
    }
  }

  return isValid;
}

/**
 * Back to Top Button
 */
function initBackToTop() {
  const backToTopBtn = document.querySelector('.back-to-top');
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

/**
 * Optional: Lazy loading images
 */
function initLazyLoading() {
  const lazyImages = document.querySelectorAll('img[data-src]');

  if (!lazyImages.length) return;

  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
        imageObserver.unobserve(img);
      }
    });
  });

  lazyImages.forEach(img => imageObserver.observe(img));
}

/**
 * Optional: Parallax effect for hero
 */
function initParallax() {
  const hero = document.querySelector('.hero');
  const heroBg = document.querySelector('.hero-bg img');

  if (!hero || !heroBg) return;

  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    if (scrolled < window.innerHeight) {
      heroBg.style.transform = `translateY(${scrolled * 0.3}px)`;
    }
  }, { passive: true });
}
