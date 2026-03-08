import sys
import re

testimonials = [
    {"author": "Alberto Valentín", "text": "En dos palabras Pau, espectacular como siempre."},
    {"author": "Carlos", "text": "Un crack este profe."},
    {"author": "Carlos Alejandro", "text": "Estupenda clase. Un ritmo algo rápido pero necesario para entenderlo todo de un plumazo. Pau lo ha dado todo. ¡Gracias!"},
    {"author": "Elizabeth Elvira", "text": "Estoy feliz con lo que estoy aprendiendo, gracias Pau!!!!"},
    {"author": "Estrella", "text": "Siempre me gustaron las clases, pero no podía practicar porque no sabía entrar a los sitios. Esta vez Pau mostró paso por paso y logré en dos veces de ver la clase 14 hacer mi presentación yo sola, sin ayuda, solo con la guía paso a paso de Pau. Gracias por tu paciencia al bajarte a nivel de principiante querido Pau. Te quiero por eso!!!!"},
    {"author": "Fabiola", "text": "Excelente Pau. ¡Cómo se te extrañaba, eres un maestro, gracias!"},
    {"author": "Fabiola (2)", "text": "Gracias Pau, te estás volviendo todo un súper maestro con cada clase que das. Te felicito, tienes un don muy natural."},
    {"author": "Francisco Javier", "text": "Gracias siempre por tu buen humor y alegría Pau. ¡Eres un grande!!"},
    {"author": "Hugo", "text": "Martí es un crack. La clase ha sido una verdadera pasada. Cada vez me sorprendo con el alcance de la IA. La mejor inversión que he hecho en mi vida."},
    {"author": "Irina", "text": "¡La clase más impresionante de todas! Muchas gracias Pau!!!"},
    {"author": "Juan David", "text": "Muy didácticas son las explicaciones de Pau Martí."},
    {"author": "Manuel Jesús", "text": "La verdad es que Pau hace todo con mucha alegría y tiene un muy alto conocimiento de la IA y en su afán de dar el servicio a todos abarca mucho. Sin embargo lo he podido seguir con algo de trabajo, pero muy bien. Felicidades Pau."},
    {"author": "María", "text": "Me ha flipado la clase, Pau cada día me sorprende más. ¡Guau!"},
    {"author": "María del Carmen", "text": "Muchas gracias Pau, como siempre es un gusto tener la clase. Me encanta tu entusiasmo, lo contagias."},
    {"author": "Mónica", "text": "Pau es un profesional y es un gran comunicador, excelente profesor."},
    {"author": "Natalia", "text": "Increíble NotebookLM y IA Google Studio, ¡un súper descubrimiento! Gracias Pauuuu."},
    {"author": "Olga", "text": "Pau es genial. Lo explica todo muy bien, con mucha paciencia y muy didáctico. Además hace las clases divertidas y motivadoras. Un saludo, Olga."},
    {"author": "Pilar", "text": "Me gusta mucho cómo explica Pau y el curso. Gracias."},
    {"author": "Ramiro", "text": "Excelente predisposición y buena onda de Pau."},
    {"author": "Rosa", "text": "Lo mejor al final de la clase, muy buenos consejos de uso de herramientas diferentes. Gracias Pau."},
    {"author": "Sergio", "text": "Gracias Pau, crack total."},
    {"author": "Sergio Renán", "text": "Excelente, todo de 10. Felicidades a Pau quien está al frente en la enseñanza, pero extensivo a todo el equipo que está detrás y hace posible esto. ¡Buen fin de semana!"},
    {"author": "Tatiana Moreno", "text": "Pau qué clases tan fenomenales nos brindas, yo estoy muy agradecido. Y son GRATIS."},
    {"author": "Daniel Bianco", "text": "Ya estamos en el directo!!!"},
    {"author": "Fabián Gutiérrez", "text": "Excelente manera de enseñar y más la disposición. Grande Pau y gracias por tu tiempo."},
    {"author": "Luis Zapata", "text": "Gracias Pau por enseñarnos sobre IA de la mejor manera que existe con sus metáforas que son muy didácticas 👍💯"},
    {"author": "Natalia Torres", "text": "Espectacular tus clases gratuitas Pau!! Eres súper pedagógico! Mil graciassss 👏"},
    {"author": "Federico Fazzari", "text": "Genio, cómo va… ya estamos en directo."},
    {"author": "Carlos Martínez", "text": "Pau Martí Felip, el mejor profesor de IA y una excelente persona 100/100."},
    {"author": "Héctor Salas", "text": "Pau es el mejor profesor de IA, nadie explica los conceptos de forma más clara y sencilla y se preocupa porque sus estudiantes de verdad entiendan y puedan sacarle provecho. Tiene un entusiasmo y energía contagiosa, siempre alegre y con sentido del humor."},
    {"author": "Alonso Ochoa", "text": "Por cierto, estas 4 clases de Google Antigravity han sido más que fabulosas de buenas para nuestros proyectos."},
    {"author": "Miguel Oviedo", "text": "Pau, ¡la clase está muy bien! Se entiende todo perfecto 👌❤️"},
    {"author": "Lola Álvarez", "text": "Me encanta tu manera de enseñar. Haces que algo tan complicado como la IA sea entendible para personas como yo que no estamos familiarizados con la informática. 👏👏👏❤️❤️"},
    {"author": "Nessa Hiram", "text": "Gracias Pau, tus clases son pura práctica, ejercicios, retos y de valor para casos de uso. Sigue adelante, es un honor estar en tus clases 😍👏 pura dinámica 🧨"},
    {"author": "María Teresa de Paul", "text": "Felicidades, tus clases se entienden muy bien. Y transmites energía para dar y tomar. Qué vitalidad la tuya. Se ve que te gusta y disfrutas con la IA 👏"},
    {"author": "Sonia Soria", "text": "Muchas gracias por tus clases, son estupendas y muy prácticas. Me han encantado estas 4 clases. Geniales."},
    {"author": "Ricardo Federico", "text": "Excelente instructor. Sabe y le apasiona enseñar y logra engancharte. No se lo pierdan. Es súper, súper recomendable."},
    {"author": "Araque Secay", "text": "Pau, tus clases son geniales. Es increíble la cantidad de conocimiento sobre IA que transmites y de forma gratuita. Conocerte me ha cambiado la vida 🙌"},
    {"author": "Steve González", "text": "Excelentes clases Pau, muy didácticas y con ejemplos claros y fáciles de entender. Eres el mejor maestro de IA que hay."},
    {"author": "Rincón Nirvana", "text": "Muy bien!! Y además es genial la participación de la gente."},
    {"author": "Juventud Alboraya", "text": "Wow, estamos en directo."},
    {"author": "Nieves Loinaz", "text": "Un buen comunicador."},
    {"author": "Rocío Cropp", "text": "Un verdadero cachaco! jajaja, y un extraordinario instructor de IA ❤️"},
    {"author": "Jordi Echevarría", "text": "Crack, el mejor formador de largo; ánimos y a seguir así."},
    {"author": "Heidi Chary", "text": "Sus clases en vivo son brutales. Y no se diga su escuela de IA. 1000% recomendable. Te aseguro que esto no es pérdida de tiempo ni de dinero. El mejor maestro de IA."}
]

# Split roughly in half
mid = len(testimonials) // 2
top_row = testimonials[:mid]
bottom_row = testimonials[mid:]

def generate_html(row):
    html = []
    for t in row:
        name = t['author']
        if name == "Fabiola (2)": name = "Fabiola" # Clean up duplicate name identifier
        html.append(f'''                        <div class="testimonial-card glass hover-lift">
                            <div class="quote-icon">“</div>
                            <p class="testimonial-text">{t['text']}</p>
                            <p class="testimonial-author">— {name}</p>
                        </div>''')
    return "\n".join(html)

top_html = generate_html(top_row)
bottom_html = generate_html(bottom_row)

with open('/Users/polo/paumartifelip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the regex more flexible by using [^>]* to match any additional classes like 'top-row' or 'bottom-row reverse'
pattern_top = r'(<div class="testimonials-marquee-container[^>]*>.*?<div class="testimonials-marquee-content">)(.*?)(</div>.*?<!-- Duplicado del Carril Superior -->.*?<div class="testimonials-marquee-content" aria-hidden="true">)(.*?)(</div>.*?</div>.*?<!-- Carril Inferior)'
def replacer_top(match):
    return match.group(1) + "\n" + top_html + "\n                    " + match.group(3) + "\n" + top_html + "\n                    " + match.group(5)
content = re.sub(pattern_top, replacer_top, content, flags=re.DOTALL)

pattern_bottom = r'(<div class="testimonials-marquee-container[^>]*>.*?<div class="testimonials-marquee-content">)(.*?)(</div>.*?<!-- Duplicado del Carril Inferior -->.*?<div class="testimonials-marquee-content" aria-hidden="true">)(.*?)(</div>.*?</div>.*?</div>)'
def replacer_bottom(match):
    return match.group(1) + "\n" + bottom_html + "\n                    " + match.group(3) + "\n" + bottom_html + "\n                    " + match.group(5)
content = re.sub(pattern_bottom, replacer_bottom, content, flags=re.DOTALL)

with open('/Users/polo/paumartifelip/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Injected {len(top_row)} items into top row and {len(bottom_row)} into bottom row.")
