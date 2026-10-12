# paumartifelip.com

Landing page de Pau Martí Felip (conferencias y formación en inteligencia artificial).
Sitio estático, sin build ni dependencias — se despliega tal cual.

- **Live:** https://paumartifelip.com
- **Despliegue:** Cloudflare Pages, conectado al repo de GitHub. Cada `git push` a `main`
  dispara un deploy automático (normalmente tarda 30–60s en completarse).

## Estructura

```
index.html     Todo el contenido y las secciones de la página (una sola página)
style.css      Todos los estilos. Tiene un índice al principio del archivo (Cmd+F el nombre entre comillas)
script.js      JS mínimo: animaciones al hacer scroll, navbar que cambia de color, scroll suave
img/           Todas las fotografías, ya optimizadas (ver "Imágenes" abajo)
```

No hay build step: se edita `index.html` / `style.css` / `script.js` directamente y se sube.

## Orden de `index.html`

Cada sección tiene un comentario `<!-- NOMBRE -->` justo antes de abrir. De arriba a abajo:

Hero → fotos de Pau en acción → visión/intro → antes-después → qué hace la conferencia
espectacular → garantía "momentos WOW" → sobre Pau (biografía) → catálogo de conferencias
y workshops → comunidad Skool → comunidad WhatsApp → testimonios (marquee) → empresas que
confían en Pau → detrás de cámaras → CTA final.

## `style.css`

Son ~1850 líneas porque el sitio ha ido creciendo a base de encargos puntuales (fotos,
paleta de colores, responsive, hero, degradados…). Por eso el archivo tiene dos partes:

1. **Las reglas base** de cada componente, en el orden en que aparecen en la página
   (navbar, hero, fotos, programas, testimonios…).
2. **Bloques añadidos al final** con comentarios tipo `/* ===== TITULO ===== */` para
   cambios de diseño que se fueron pidiendo después (degradados del título, efecto
   "liquid glass", acentos de color). Antes de tocar un componente, busca primero si
   tiene un bloque posterior que lo sobrescriba — el índice del principio del archivo
   ayuda a encontrarlo.

El responsive para móvil (`@media (max-width: 768px)`) está casi todo junto cerca del
final del archivo. La regla de oro del móvil es que **nunca debe haber scroll horizontal**
(bloque "BLOQUEO DE SCROLL HORIZONTAL"): si añades algo ancho, dale `max-width: 100%`.

## Imágenes

Las fotos originales (del móvil/cámara de Pau) suelen pesar varios MB. Antes de subir una
foto nueva, se optimiza así (Python + Pillow):

```python
from PIL import Image, ImageOps
im = Image.open('original.jpg')
im = ImageOps.exif_transpose(im)   # corrige la rotación de fotos de móvil
im.thumbnail((1600, 1600))          # nunca más ancha/alta que esto
im.convert('RGB').save('img/nombre-descriptivo.jpg', quality=80, optimize=True, progressive=True)
```

Para una foto de perfil/avatar pequeña, usa `thumbnail((800, 800))` en vez de 1600.
Nombra el archivo describiendo la foto (`pau-conferencia-sala.jpg`, no `IMG_4821.jpg`).

## Caché del navegador

`style.css` y `script.js` se cargan con `?v=<timestamp>` en `index.html`
(`<link rel="stylesheet" href="style.css?v=...">`). **Cuando cambies `style.css` o
`script.js`, actualiza ese número de versión** (basta con la fecha en segundos,
`date +%s`), o el navegador de la gente puede seguir sirviendo la versión vieja en caché
aunque la página se recargue.

## Verificar un despliegue

```bash
git push origin main
# esperar ~30-60s, luego:
curl -s "https://paumartifelip.com/style.css?v=$(date +%s)" | grep "algo que acabas de añadir"
```

También se puede consultar el estado del Check Run de GitHub/Cloudflare:
```bash
curl -s https://api.github.com/repos/paumartifelip-cpu/paumartifelip/commits/<sha>/check-runs
```
