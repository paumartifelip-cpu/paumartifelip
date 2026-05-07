import sys

with open('style.css', 'r', encoding='utf-8') as f:
    orig = f.read()

target = """/* TESTIMONIOS (Masonry Layout) */
.testimonials-section {
  position: relative;
  z-index: 1;
}

.masonry-grid {
  column-count: 3;
  column-gap: 2rem;
  width: 100%;
}

.testimonial-card {
  break-inside: avoid;
  margin-bottom: 2rem;
  padding: 2.5rem;
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.03);
  /* Ligeramente más translúcido */
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  position: relative;
  overflow: hidden;
}

/* Brillo sutil superior en las tarjetas */
.testimonial-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), transparent);
}

.quote-icon {
  font-size: 4rem;
  color: var(--color-accent);
  opacity: 0.2;
  position: absolute;
  top: -10px;
  left: 1.5rem;
  font-family: serif;
  user-select: none;
}

.testimonial-text {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #e5e5e5;
  margin-bottom: 1.5rem;
  position: relative;
  z-index: 2;
  font-weight: 300;
}

.testimonial-author {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-accent);
  position: relative;
  z-index: 2;
}"""

replacement = """/* TESTIMONIOS (Double Marquee Layout) */
.testimonials-section {
  position: relative;
  z-index: 1;
  overflow: hidden;
}

.testimonials-slider-wrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  width: 100%;
  overflow: hidden;
  /* Mascara para difuminar los bordes laterales y dar efecto infinito elegante */
  mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
}

.testimonials-marquee-container {
  display: flex;
  width: max-content;
}

.testimonials-marquee-content {
  display: flex;
  gap: 2rem;
  padding-right: 2rem; /* Espaciado con el duplicado */
  animation: scroll-left 50s linear infinite;
}

.testimonials-marquee-container.reverse .testimonials-marquee-content {
  animation: scroll-right 50s linear infinite;
  animation-direction: reverse;
}

.testimonials-marquee-container:hover .testimonials-marquee-content {
  animation-play-state: paused;
}

.testimonial-card {
  width: 380px;
  flex-shrink: 0;
  padding: 2.5rem;
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.testimonial-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), transparent);
}

.quote-icon {
  font-size: 4rem;
  color: var(--color-accent);
  opacity: 0.2;
  position: absolute;
  top: -10px;
  left: 1.5rem;
  font-family: serif;
  user-select: none;
}

.testimonial-text {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #e5e5e5;
  margin-bottom: 1.5rem;
  position: relative;
  z-index: 2;
  font-weight: 300;
}

.testimonial-author {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-accent);
  position: relative;
  z-index: 2;
  margin-top: auto;
}

@keyframes scroll-left {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-100%);
  }
}

@keyframes scroll-right {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}"""

if target in orig:
    new_css = orig.replace(target, replacement)
    
    # We also need to remove the mobile/tablet media queries for masonry
    mobile_target = """.masonry-grid {
    column-count: 2; /* Para tablet */
  }"""
    if mobile_target in new_css:
        new_css = new_css.replace(mobile_target, "")
        
    mobile_target_2 = """.masonry-grid {
    column-count: 1; /* Para móvil una sola columna */
  }"""
    if mobile_target_2 in new_css:
        new_css = new_css.replace(mobile_target_2, "")
        
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(new_css)
    print("CSS updated successfully")
else:
    print("Could not find the target CSS block")

