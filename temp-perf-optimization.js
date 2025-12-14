// Performance optimized functions
function initPerformanceOptimizations() {
  // Optimize animations using requestAnimationFrame
  const elementsWithAnimations = document.querySelectorAll('.animate-fadeInUp, .animate-on-scroll');
  
  // Use Intersection Observer API for efficient scroll detection
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.1,
    // Only trigger once
    once: true
  };

  const animationObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Add optimized animation classes
        entry.target.classList.add('animate-in');
        animationObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  elementsWithAnimations.forEach(el => {
    el.classList.add('animate-pending');
    animationObserver.observe(el);
  });

  // Optimize image loading
  optimizeImageLoading();

  // Optimize event listeners
  optimizeEventListeners();
}

function optimizeImageLoading() {
  // Use modern loading attributes and implement lazy loading for better performance
  const images = document.querySelectorAll('img[data-src]:not([src])');
  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        const src = img.getAttribute('data-src');
        if (src) {
          img.src = src;
          img.removeAttribute('data-src');
          img.classList.add('loaded');
        }
        imageObserver.unobserve(img);
      }
    });
  });

  images.forEach(img => {
    // Add loading="lazy" attribute if not present
    if (!img.hasAttribute('loading')) {
      img.setAttribute('loading', 'lazy');
    }
    imageObserver.observe(img);
  });
}

function optimizeEventListeners() {
  // Use event delegation for better performance
  document.body.addEventListener('click', function(e) {
    // Handle clicks on navigation with optimized performance
    if (e.target.closest('.nav-link')) {
      // Optimize nav link interactions
      const link = e.target.closest('.nav-link');
      // Add performance optimized routing
      setTimeout(() => {
        updateActiveNavigation();
      }, 10);
    }
  });

  // Optimize scroll events with throttling
  let ticking = false;
  function updateScrollAnimations() {
    // Update scroll-based animations efficiently
    updateHeaderOnScroll();
    updateScrollProgress();
    ticking = false;
  }

  window.addEventListener('scroll', function(e) {
    if (!ticking) {
      requestAnimationFrame(updateScrollAnimations);
      ticking = true;
    }
  });
}

// Initialize performance optimizations
document.addEventListener('DOMContentLoaded', function() {
  // Run performance optimizations after the page loads
  setTimeout(initPerformanceOptimizations, 500);
});