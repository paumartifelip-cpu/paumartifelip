import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The masonry grid starts at line 260 and ends at 428 in the 1-indexed view (which means index 259 to 427)
# Let's dynamically find the block to be safer
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<div class="masonry-grid">' in line:
        start_idx = i
        break

if start_idx != -1:
    open_divs = 0
    for i in range(start_idx, len(lines)):
        open_divs += lines[i].count('<div')
        open_divs -= lines[i].count('</div')
        if open_divs == 0:
            end_idx = i
            break

if start_idx != -1 and end_idx != -1:
    new_html = """            <div class="testimonials-slider-wrapper">
                <!-- CARRIL SUPERIOR (Hacia la izquierda) -->
                <div class="testimonials-marquee-container top-row">
                    <div class="testimonials-marquee-content">
                        <!-- Mitad 1 -->
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">En dos palabras Pau, espectacular como siempre.</p>
                            <p class="testimonial-author">— Alberto Valentín</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Un crack este profe.</p>
                            <p class="testimonial-author">— Carlos</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Estupenda clase. Un ritmo algo rápido pero necesario para entenderlo todo de un plumazo. Pau lo ha dado todo. ¡Gracias!</p>
                            <p class="testimonial-author">— Carlos Alejandro</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Estoy feliz con lo que estoy aprendiendo, gracias Pau!!!!</p>
                            <p class="testimonial-author">— Elizabeth Elvira</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Excelente Pau. ¡Cómo se te extrañaba, eres un maestro, gracias!</p>
                            <p class="testimonial-author">— Fabiola</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Gracias Pau, te estás volviendo todo un súper maestro con cada clase que das. Te felicito, tienes un don muy natural.</p>
                            <p class="testimonial-author">— Fabiola</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Gracias siempre por tu buen humor y alegría Pau. ¡Eres un grande!!</p>
                            <p class="testimonial-author">— Francisco Javier</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Martí es un crack. La clase ha sido una verdadera pasada. Cada vez me sorprendo con el alcance de la IA. La mejor inversión que he hecho en mi vida.</p>
                            <p class="testimonial-author">— Hugo</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">¡La clase más impresionante de todas! Muchas gracias Pau!!!</p>
                            <p class="testimonial-author">— Irina</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Muy didácticas son las explicaciones de Pau Martí.</p>
                            <p class="testimonial-author">— Juan David</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">La verdad es que Pau hace todo con mucha alegría y tiene un muy alto conocimiento de la IA y en su afán de dar el servicio a todos abarca mucho.</p>
                            <p class="testimonial-author">— Manuel Jesús</p>
                        </div>
                    </div>
                    <!-- Duplicado del Carril Superior -->
                    <div class="testimonials-marquee-content" aria-hidden="true">
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">En dos palabras Pau, espectacular como siempre.</p>
                            <p class="testimonial-author">— Alberto Valentín</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Un crack este profe.</p>
                            <p class="testimonial-author">— Carlos</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Estupenda clase. Un ritmo algo rápido pero necesario para entenderlo todo de un plumazo. Pau lo ha dado todo. ¡Gracias!</p>
                            <p class="testimonial-author">— Carlos Alejandro</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Estoy feliz con lo que estoy aprendiendo, gracias Pau!!!!</p>
                            <p class="testimonial-author">— Elizabeth Elvira</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Excelente Pau. ¡Cómo se te extrañaba, eres un maestro, gracias!</p>
                            <p class="testimonial-author">— Fabiola</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Gracias Pau, te estás volviendo todo un súper maestro con cada clase que das. Te felicito, tienes un don muy natural.</p>
                            <p class="testimonial-author">— Fabiola</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Gracias siempre por tu buen humor y alegría Pau. ¡Eres un grande!!</p>
                            <p class="testimonial-author">— Francisco Javier</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Martí es un crack. La clase ha sido una verdadera pasada. Cada vez me sorprendo con el alcance de la IA. La mejor inversión que he hecho en mi vida.</p>
                            <p class="testimonial-author">— Hugo</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">¡La clase más impresionante de todas! Muchas gracias Pau!!!</p>
                            <p class="testimonial-author">— Irina</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Muy didácticas son las explicaciones de Pau Martí.</p>
                            <p class="testimonial-author">— Juan David</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">La verdad es que Pau hace todo con mucha alegría y tiene un muy alto conocimiento de la IA y en su afán de dar el servicio a todos abarca mucho.</p>
                            <p class="testimonial-author">— Manuel Jesús</p>
                        </div>
                    </div>
                </div>

                <!-- CARRIL INFERIOR (Hacia la derecha) -->
                <div class="testimonials-marquee-container bottom-row reverse">
                    <div class="testimonials-marquee-content">
                        <!-- Mitad 2 -->
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Me ha flipado la clase, Pau cada día me sorprende más. ¡Guau!</p>
                            <p class="testimonial-author">— María</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Muchas gracias Pau, como siempre es un gusto tener la clase. Me encanta tu entusiasmo, lo contagias.</p>
                            <p class="testimonial-author">— María del Carmen</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Pau es un profesional y es un gran comunicador, excelente profesor.</p>
                            <p class="testimonial-author">— Mónica</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Increíble NotebookLM y IA Google Studio, ¡un súper descubrimiento! Gracias Pauuuu.</p>
                            <p class="testimonial-author">— Natalia</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Pau es genial. Lo explica todo muy bien, con mucha paciencia y muy didáctico. Además hace las clases divertidas y motivadoras. Un saludo.</p>
                            <p class="testimonial-author">— Olga</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Me gusta mucho cómo explica Pau y el curso. Gracias.</p>
                            <p class="testimonial-author">— Pilar</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Excelente predisposición y buena onda de Pau.</p>
                            <p class="testimonial-author">— Ramiro</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Lo mejor al final de la clase, muy buenos consejos de uso de herramientas diferentes. Gracias Pau.</p>
                            <p class="testimonial-author">— Rosa</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Gracias Pau, crack total.</p>
                            <p class="testimonial-author">— Sergio</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Excelente, todo de 10. Felicidades a Pau quien está al frente en la enseñanza, pero extensivo a todo el equipo que está detrás y hace posible esto.</p>
                            <p class="testimonial-author">— Sergio Renán</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Siempre me gustaron las clases, pero no podía practicar porque no sabía entrar a los sitios. Logré hacer mi presentación yo sola con la guía de Pau.</p>
                            <p class="testimonial-author">— Estrella</p>
                        </div>
                    </div>
                    <!-- Duplicado del Carril Inferior -->
                    <div class="testimonials-marquee-content" aria-hidden="true">
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Me ha flipado la clase, Pau cada día me sorprende más. ¡Guau!</p>
                            <p class="testimonial-author">— María</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Muchas gracias Pau, como siempre es un gusto tener la clase. Me encanta tu entusiasmo, lo contagias.</p>
                            <p class="testimonial-author">— María del Carmen</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Pau es un profesional y es un gran comunicador, excelente profesor.</p>
                            <p class="testimonial-author">— Mónica</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Increíble NotebookLM y IA Google Studio, ¡un súper descubrimiento! Gracias Pauuuu.</p>
                            <p class="testimonial-author">— Natalia</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Pau es genial. Lo explica todo muy bien, con mucha paciencia y muy didáctico. Además hace las clases divertidas y motivadoras. Un saludo.</p>
                            <p class="testimonial-author">— Olga</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Me gusta mucho cómo explica Pau y el curso. Gracias.</p>
                            <p class="testimonial-author">— Pilar</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Excelente predisposición y buena onda de Pau.</p>
                            <p class="testimonial-author">— Ramiro</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Lo mejor al final de la clase, muy buenos consejos de uso de herramientas diferentes. Gracias Pau.</p>
                            <p class="testimonial-author">— Rosa</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Gracias Pau, crack total.</p>
                            <p class="testimonial-author">— Sergio</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Excelente, todo de 10. Felicidades a Pau quien está al frente en la enseñanza, pero extensivo a todo el equipo que está detrás y hace posible esto.</p>
                            <p class="testimonial-author">— Sergio Renán</p>
                        </div>
                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">Siempre me gustaron las clases, pero no podía practicar porque no sabía entrar a los sitios. Logré hacer mi presentación yo sola con la guía de Pau.</p>
                            <p class="testimonial-author">— Estrella</p>
                        </div>
                    </div>
                </div>
            </div>\n"""
    
    lines[start_idx:end_idx+1] = [new_html]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Replaced successfully")
else:
    print("Could not find the block")

