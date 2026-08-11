"""
Script de descarga y optimización botánica para Nectar Farms.
Descarga imágenes biológicamente correctas de Wikimedia Commons / fuentes botánicas,
las recorta a proporción 4:3 con calidad gourmet, ajusta iluminación/contraste y guarda como WebP.
"""
import os
import urllib.request
from PIL import Image, ImageEnhance

TARGET_DIR = os.path.join(os.path.dirname(__file__), 'assets', 'productos')
os.makedirs(TARGET_DIR, exist_ok=True)

PRODUCTOS_BOTANICA = [
    { "id": 1, "key": "porcini", "name": "Porcini", "sci": "Boletus edulis", "url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Boletus_edulis_IT.jpg" },
    { "id": 2, "key": "lobster", "name": "Lobster", "sci": "Hypomyces lactifluorum", "url": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Hypomyces_lactifluorum.JPG" },
    { "id": 3, "key": "hongo_azul", "name": "Hongo Azul", "sci": "Lactarius indigo", "url": "https://upload.wikimedia.org/wikipedia/commons/8/86/Lactarius_indigo_48568_edit.jpg" },
    { "id": 4, "key": "duraznillo", "name": "Duraznillo", "sci": "Cantharellus cibarius", "url": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Chanterelle_Cantharellus_cibarius.jpg" },
    { "id": 5, "key": "rovellon", "name": "Rovellón", "sci": "Lactarius deliciosus", "url": "https://upload.wikimedia.org/wikipedia/commons/8/89/Lactarius_deliciosus.jpg" },
    { "id": 6, "key": "clavito", "name": "Clavito", "sci": "Lyophyllum decastes", "url": "https://upload.wikimedia.org/wikipedia/commons/2/22/Lyophyllum_decastes_071012.jpg" },
    { "id": 7, "key": "tecomate", "name": "Tecomate", "sci": "Amanita caesarea", "url": "https://upload.wikimedia.org/wikipedia/commons/3/31/Oronges.jpg" },
    { "id": 8, "key": "mantecado", "name": "Mantecado", "sci": "Amanita rubescens", "url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Amanita_rubescens.JPG" },
    { "id": 9, "key": "hongo_coral", "name": "Hongo Coral", "sci": "Ramaria stricta", "url": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Ramaria_stricta_171867.jpg" },
    { "id": 10, "key": "morilla", "name": "Morilla", "sci": "Morchella esculenta", "url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Morchella_esculenta_-_DE_-_TH_-_2013-05-01_-_01.JPG" },
    { "id": 11, "key": "matsutake", "name": "Matsutake", "sci": "Tricholoma magnivelare", "url": "https://upload.wikimedia.org/wikipedia/commons/b/bf/2018-10-05_Tricholoma_magnivelare_%28Peck%29_Redhead_972957.jpg" },
    { "id": 12, "key": "anonna_san_pablo", "name": "Anonna San Pablo", "sci": "Annona reticulata", "url": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Annona_reticulata_fruit.JPG" },
    { "id": 13, "key": "saramuyo", "name": "Saramuyo", "sci": "Annona squamosa", "url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Sugar_apple_on_tree.jpg" },
    { "id": 14, "key": "naranja_sangria", "name": "Naranja Sangría", "sci": "Citrus sinensis Blood Orange", "url": "https://upload.wikimedia.org/wikipedia/commons/5/5d/BloodOrange.jpg" },
    { "id": 15, "key": "manzana_pearly_pink", "name": "Manzana Pearly Pink", "sci": "Malus domestica Pink Pearl", "url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Pink_Pearl_%285207256521%29.jpg" },
    { "id": 16, "key": "kaniste", "name": "Kaniste", "sci": "Pouteria campechana", "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Canistel.jpg" },
    { "id": 17, "key": "mostaza_miz_america", "name": "Mostaza Miz America", "sci": "Brassica juncea Mizuna", "url": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Mizuna_001.jpg" },
    { "id": 18, "key": "mostaza_fresse", "name": "Mostaza Fresse", "sci": "Brassica juncea", "url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Brassica_juncea_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-168.jpg" },
    { "id": 19, "key": "mostaza_ruby_streaks", "name": "Mostaza Ruby Streaks", "sci": "Brassica juncea Ruby", "url": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?auto=format&fit=crop&w=800&q=85" },
    { "id": 20, "key": "ube", "name": "Ube", "sci": "Dioscorea alata / purpurea", "url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Dioscorea_alata_-_Purple_yam_tuber_-_Mindanao%2C_Philippines.jpg" },
    { "id": 21, "key": "espinaca_okinawa", "name": "Espinaca de Okinawa", "sci": "Gynura bicolor", "url": "https://upload.wikimedia.org/wikipedia/commons/6/60/Gynura_bicolor_vegetable_%28hongfeng_cai_%E7%B4%85%E9%B3%B3%E8%8F%9C%29.png" }
]

def procesar_imagenes():
    print("Iniciando procesamiento de imágenes botánicas con Pillow...")
    for item in PRODUCTOS_BOTANICA:
        try:
            print(f"Descargando y optimizando {item['name']} ({item['sci']})...")
            req = urllib.request.Request(item['url'], headers={'User-Agent': 'Mozilla/5.0 NectarFarms/1.0'})
            temp_path = os.path.join(TARGET_DIR, f"temp_{item['key']}.jpg")
            with urllib.request.urlopen(req) as resp, open(temp_path, 'wb') as f:
                f.write(resp.read())
            
            # Procesar con Pillow
            with Image.open(temp_path) as img:
                img = img.convert('RGB')
                
                # Proporción 4:3 (600x450)
                target_w, target_h = 600, 450
                w, h = img.size
                scale = max(target_w / w, target_h / h)
                new_w, new_h = int(w * scale), int(h * scale)
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                
                left = (new_w - target_w) // 2
                top = (new_h - target_h) // 2
                img = img.crop((left, top, left + target_w, top + target_h))
                
                # Mejora sutil de contraste y saturación
                img = ImageEnhance.Color(img).enhance(1.08)
                img = ImageEnhance.Contrast(img).enhance(1.05)
                
                out_path = os.path.join(TARGET_DIR, f"{item['key']}.webp")
                img.save(out_path, format='WEBP', quality=85, method=6)
                print(f"  ✓ Generado con éxito: {out_path}")
            
            if os.path.exists(temp_path):
                os.remove(temp_path)
        except Exception as e:
            print(f"  ✗ Error en {item['name']}: {e}")

if __name__ == '__main__':
    procesar_imagenes()
