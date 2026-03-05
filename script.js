// Intersection Observer for scroll animations
document.addEventListener('DOMContentLoaded', () => {
  // Config for observer
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15 // trigger when 15% visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // keep it active once revealed or unobserve to stop repeating
        // observer.unobserve(entry.target); 
      }
    });
  }, observerOptions);

  // Grab all elements with reveal-section class
  const revealElements = document.querySelectorAll('.reveal-section');
  revealElements.forEach(el => observer.observe(el));

  // Navbar background change on scroll
  const navbar = document.getElementById('navbar');
  const lightSections = document.querySelectorAll('.bg-light');

  // To truly match Apple's sophisticated nav color switching is complex, 
  // but a simple scroll threshold or intersection observer on light sections works
  const navObserverOptions = {
    rootMargin: '-50px 0px -90% 0px',
    threshold: 0
  };

  const navObserver = new IntersectionObserver((entries) => {
    let isLightSectionIntersecting = false;
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        isLightSectionIntersecting = true;
      }
    });

    if (isLightSectionIntersecting) {
      navbar.classList.add('light-mode');
    } else {
      navbar.classList.remove('light-mode');
    }
  }, navObserverOptions);

  lightSections.forEach(section => navObserver.observe(section));

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: 'smooth'
        });
      }
    });
  });

  // Parallax effect for hero video background
  const videoWrapper = document.querySelector('.video-background-wrapper');
  window.addEventListener('scroll', () => {
    if (window.scrollY < window.innerHeight) {
      const scrollPos = window.scrollY;
      videoWrapper.style.transform = `translateY(${scrollPos * 0.4}px)`;
    }
  });
});
