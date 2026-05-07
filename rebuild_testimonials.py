"""
Rebuilds the entire testimonials section in index.html from scratch.
Top row: testimonials[0:23], Bottom row: testimonials[23:]
Each card: clean, no extra classes.
"""

testimonials = [
    {"author": "Alberto Valentín", "text": "En dos palabras Pau, espectacular como siempre."},
    {"author": "Carlos", "text": "Un crack este profe."},
    {"author": "Carlos Alejandro", "text": "Estupenda clase. Un ritmo algo rápido pero necesario para entenderlo todo de un plumazo. Pau lo ha dado todo. ¡Gracias!"},
    {"author": "Elizabeth Elvira", "text": "Estoy feliz con lo que estoy aprendiendo, gracias Pau!!!!"},
    {"author": "Estrella", "text": "Siempre me gustaron las clases, pero no podía practicar porque no sabía entrar a los sitios. Esta vez Pau mostró paso por paso y logré en dos veces de ver la clase 14 hacer mi presentación yo sola, sin ayuda, solo con la guía paso a paso de Pau. ¡Gracias por tu paciencia!"},
    {"author": "Fabiola", "text": "Excelente Pau. ¡Cómo se te extrañaba, eres un maestro, gracias!"},
    {"author": "Fabiola", "text": "Gracias Pau, te estás volviendo todo un súper maestro con cada clase que das. Te felicito, tienes un don muy natural."},
    {"author": "Francisco Javier", "text": "Gracias siempre por tu buen humor y alegría Pau. ¡Eres un grande!!"},
    {"author": "Hugo", "text": "Martí es un crack. La clase ha sido una verdadera pasada. Cada vez me sorprendo con el alcance de la IA. La mejor inversión que he hecho en mi vida."},
    {"author": "Irina", "text": "¡La clase más impresionante de todas! Muchas gracias Pau!!!"},
    {"author": "Juan David", "text": "Muy didácticas son las explicaciones de Pau Martí."},
    {"author": "Manuel Jesús", "text": "La verdad es que Pau hace todo con mucha alegría y tiene un muy alto conocimiento de la IA. Felicidades Pau."},
    {"author": "María", "text": "Me ha flipado la clase, Pau cada día me sorprende más. ¡Guau!"},
    {"author": "María del Carmen", "text": "Muchas gracias Pau, como siempre es un gusto tener la clase. Me encanta tu entusiasmo, lo contagias."},
    {"author": "Mónica", "text": "Pau es un profesional y es un gran comunicador, excelente profesor."},
    {"author": "Natalia", "text": "Increíble NotebookLM y IA Google Studio, ¡un súper descubrimiento! Gracias Pauuuu."},
    {"author": "Olga", "text": "Pau es genial. Lo explica todo muy bien, con mucha paciencia y muy didáctico. Además hace las clases divertidas y motivadoras."},
    {"author": "Pilar", "text": "Me gusta mucho cómo explica Pau y el curso. Gracias."},
    {"author": "Ramiro", "text": "Excelente predisposición y buena onda de Pau."},
    {"author": "Rosa", "text": "Lo mejor al final de la clase, muy buenos consejos de uso de herramientas diferentes. Gracias Pau."},
    {"author": "Sergio", "text": "Gracias Pau, crack total."},
    {"author": "Sergio Renán", "text": "Excelente, todo de 10. Felicidades a Pau quien está al frente en la enseñanza. ¡Buen fin de semana!"},
    {"author": "Tatiana Moreno", "text": "Pau qué clases tan fenomenales nos brindas, yo estoy muy agradecido. Y son GRATIS."},
    {"author": "Daniel Bianco", "text": "Ya estamos en el directo!!!"},
    {"author": "Fabián Gutiérrez", "text": "Excelente manera de enseñar y más la disposición. Grande Pau y gracias por tu tiempo."},
    {"author": "Luis Zapata", "text": "Gracias Pau por enseñarnos sobre IA de la mejor manera que existe con sus metáforas que son muy didácticas 👍💯"},
    {"author": "Natalia Torres", "text": "Espectacular tus clases gratuitas Pau!! Eres súper pedagógico! Mil graciassss 👏"},
    {"author": "Federico Fazzari", "text": "Genio, cómo va… ya estamos en directo."},
    {"author": "Carlos Martínez", "text": "Pau Martí Felip, el mejor profesor de IA y una excelente persona 100/100."},
    {"author": "Héctor Salas", "text": "Pau es el mejor profesor de IA, nadie explica los conceptos de forma más clara y sencilla. Tiene un entusiasmo y energía contagiosa, siempre alegre y con sentido del humor."},
    {"author": "Alonso Ochoa", "text": "Por cierto, estas 4 clases de Google Antigravity han sido más que fabulosas de buenas para nuestros proyectos."},
    {"author": "Miguel Oviedo", "text": "Pau, ¡la clase está muy bien! Se entiende todo perfecto 👌❤️"},
    {"author": "Lola Álvarez", "text": "Me encanta tu manera de enseñar. Haces que algo tan complicado como la IA sea entendible para personas como yo. 👏👏👏"},
    {"author": "Nessa Hiram", "text": "Gracias Pau, tus clases son pura práctica, ejercicios, retos y de valor para casos de uso. Es un honor estar en tus clases 😍👏"},
    {"author": "María Teresa de Paul", "text": "Felicidades, tus clases se entienden muy bien. Y transmites energía para dar y tomar. Qué vitalidad la tuya 👏"},
    {"author": "Sonia Soria", "text": "Muchas gracias por tus clases, son estupendas y muy prácticas. Me han encantado estas 4 clases. Geniales."},
    {"author": "Ricardo Federico", "text": "Excelente instructor. Sabe y le apasiona enseñar y logra engancharte. No se lo pierdan. Es súper, súper recomendable."},
    {"author": "Araque Secay", "text": "Pau, tus clases son geniales. Es increíble la cantidad de conocimiento sobre IA que transmites y de forma gratuita. Conocerte me ha cambiado la vida 🙌"},
    {"author": "Steve González", "text": "Excelentes clases Pau, muy didácticas y con ejemplos claros y fáciles de entender. Eres el mejor maestro de IA que hay."},
    {"author": "Rincón Nirvana", "text": "Muy bien!! Y además es genial la participación de la gente."},
    {"author": "Nieves Loinaz", "text": "Un buen comunicador."},
    {"author": "Rocío Cropp", "text": "Un verdadero cachaco! jajaja, y un extraordinario instructor de IA ❤️"},
    {"author": "Jordi Echevarría", "text": "Crack, el mejor formador de largo; ánimos y a seguir así."},
    {"author": "Heidi Chary", "text": "Sus clases en vivo son brutales. Y no se diga su escuela de IA. 1000% recomendable. Te aseguro que esto no es pérdida de tiempo ni de dinero. El mejor maestro de IA."}
]

mid = len(testimonials) // 2
top_row = testimonials[:mid]
bottom_row = testimonials[mid:]

def make_card(t):
    return f'''                        <div class="testimonial-card">
                            <div class="quote-icon">\u201c</div>
                            <p class="testimonial-text">{t['text']}</p>
                            <p class="testimonial-author">\u2014 {t['author']}</p>
                        </div>'''

def make_row_html(items):
    cards_html = "\n".join(make_card(t) for t in items)
    return cards_html

top_html = make_row_html(top_row)
bottom_html = make_row_html(bottom_row)

new_section = f'''    <!-- TESTIMONIOS (Lo que dicen de Pau) -->
    <section class="section testimonials-section bg-light pt-8 pb-8">
        <div class="container reveal-section">
            <h2 class="section-heading center-text mb-6">Lo que dicen de Pau</h2>

            <div class="testimonials-slider-wrapper">
                <!-- CARRIL SUPERIOR (Hacia la izquierda) -->
                <div class="testimonials-marquee-container top-row">
                    <div class="testimonials-marquee-content">
                        <!-- Mitad 1 -->
{top_html}
                    </div>
                    <!-- Duplicado del Carril Superior -->
                    <div class="testimonials-marquee-content" aria-hidden="true">
{top_html}
                    </div>
                </div>

                <!-- CARRIL INFERIOR (Hacia la derecha) -->
                <div class="testimonials-marquee-container bottom-row reverse">
                    <div class="testimonials-marquee-content">
                        <!-- Mitad 2 -->
{bottom_html}
                    </div>
                    <!-- Duplicado del Carril Inferior -->
                    <div class="testimonials-marquee-content" aria-hidden="true">
{bottom_html}
                    </div>
                </div>

            </div>
        </div>
    </section>'''

with open('/Users/polo/paumartifelip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the testimonials section
import re
pattern = r'    <!-- TESTIMONIOS \(Lo que dicen de Pau\) -->.*?</section>'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + new_section + content[match.end():]
    with open('/Users/polo/paumartifelip/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"SUCCESS: rebuilt section with {len(top_row)} top + {len(bottom_row)} bottom testimonials.")
else:
    print("ERROR: Could not find the testimonials section to replace.")
