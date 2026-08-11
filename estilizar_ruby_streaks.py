import os
from PIL import Image, ImageFilter, ImageEnhance

# 1. Cargar la imagen de origen (convirtiendo a RGBA para transparencia)
source_path = os.path.join(os.path.dirname(__file__), "hoja_ruby_streaks_raw.jpg")
if not os.path.exists(source_path):
    # Buscar en rutas alternativas
    for candidate in ["hoja_ruby_streaks_raw.jpg", "ruby_streaks_leaf.jpg", "assets/productos/mostaza_ruby_streaks.jpg"]:
        if os.path.exists(candidate):
            source_path = candidate
            break

img = Image.open(source_path).convert("RGBA")

# 2. Remover matemáticamente el fondo blanco
datas = img.getdata()
newData = []
for item in datas:
    # Si los canales R, G, B son muy cercanos al blanco, los hacemos transparentes
    if item[0] > 235 and item[1] > 235 and item[2] > 235:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)

# 3. Recortar bordes vacíos sobrantes
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# 4. Crear un lienzo de fondo con proporción 4:3 (600x450 px) de tono gris-cálido premium
bg = Image.new("RGBA", (600, 450), (242, 243, 240, 255))

# 5. Redimensionar la hoja para que tenga una altura elegante de 340px manteniendo proporción
leaf_height = 340
h_percent = (leaf_height / float(img.size[1]))
w_size = int((float(img.size[0]) * float(h_percent)))
leaf_resized = img.resize((w_size, leaf_height), Image.Resampling.LANCZOS)

# 6. Realzar el color (hacer que el tono rubí/púrpura sea vibrante y fresco)
color_enhancer = ImageEnhance.Color(leaf_resized)
leaf_colored = color_enhancer.enhance(1.4)  # Boost de color del 40%
contrast_enhancer = ImageEnhance.Contrast(leaf_colored)
leaf_final = contrast_enhancer.enhance(1.15) # Ligero boost de contraste

# 7. Generar una sombra de gota (Drop Shadow) difuminada para efecto 3D
shadow = Image.new("RGBA", leaf_final.size, (0, 0, 0, 0))
shadow_data = []
for item in leaf_final.getdata():
    if item[3] > 0:
        # Sombra suave de tono carbón con opacidad ligera
        shadow_data.append((45, 49, 46, int(item[3] * 0.15)))
    else:
        shadow_data.append((0, 0, 0, 0))
shadow.putdata(shadow_data)
shadow_blurred = shadow.filter(ImageFilter.GaussianBlur(12)) # Desenfoque suave

# 8. Centrar y pegar los elementos en el lienzo
x = (600 - w_size) // 2
y = (450 - leaf_height) // 2

# Pegar sombra con un sutil desplazamiento (offset) hacia la derecha y abajo
bg.paste(shadow_blurred, (x + 8, y + 8), shadow_blurred)
# Pegar la hoja estilizada
bg.paste(leaf_final, (x, y), leaf_final)

# 9. Guardar en la carpeta local de productos en formato WebP de alta velocidad
os.makedirs("assets/productos", exist_ok=True)
bg.convert("RGB").save("assets/productos/mostaza_ruby_streaks.webp", "WEBP", quality=90)
print("¡Estilización botánica de Ruby Streaks completada con éxito!")
