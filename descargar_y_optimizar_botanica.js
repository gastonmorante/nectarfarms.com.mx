const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const targetDir = path.join(__dirname, 'assets', 'productos');
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

const productosBotanica = [
  { id: 1, key: "porcini", name: "Porcini", sci: "Boletus sp.", url: "https://upload.wikimedia.org/wikipedia/commons/3/34/Boletus_edulis_IT.jpg" },
  { id: 2, key: "lobster", name: "Lobster", sci: "Hypomyces lactifluorum", url: "https://upload.wikimedia.org/wikipedia/commons/c/c7/Hypomyces_lactifluorum.JPG" },
  { id: 3, key: "hongo_azul", name: "Hongo Azul", sci: "Lactarius indigo", url: "https://upload.wikimedia.org/wikipedia/commons/8/86/Lactarius_indigo_48568_edit.jpg" },
  { id: 4, key: "duraznillo", name: "Duraznillo", sci: "Cantharellus cibarius", url: "https://upload.wikimedia.org/wikipedia/commons/9/9a/Chanterelle_Cantharellus_cibarius.jpg" },
  { id: 5, key: "rovellon", name: "Rovellón", sci: "Lactarius deliciosus", url: "https://upload.wikimedia.org/wikipedia/commons/8/89/Lactarius_deliciosus.jpg" },
  { id: 6, key: "clavito", name: "Clavito", sci: "Lyophyllum decastes", url: "https://upload.wikimedia.org/wikipedia/commons/2/22/Lyophyllum_decastes_071012.jpg" },
  { id: 7, key: "tecomate", name: "Tecomate", sci: "Amanita caesarea", url: "https://upload.wikimedia.org/wikipedia/commons/3/31/Oronges.jpg" },
  { id: 8, key: "mantecado", name: "Mantecado", sci: "Amanita rubescens", url: "https://upload.wikimedia.org/wikipedia/commons/b/b6/Amanita_rubescens.JPG" },
  { id: 9, key: "hongo_coral", name: "Hongo Coral", sci: "Ramaria sp.", url: "https://upload.wikimedia.org/wikipedia/commons/0/0d/Ramaria_stricta_171867.jpg" },
  { id: 10, key: "morilla", name: "Morilla", sci: "Morchella sp.", url: "https://upload.wikimedia.org/wikipedia/commons/e/e3/Morchella_esculenta_-_DE_-_TH_-_2013-05-01_-_01.JPG" },
  { id: 11, key: "matsutake", name: "Matsutake", sci: "Tricholoma magnivelare", url: "https://upload.wikimedia.org/wikipedia/commons/b/bf/2018-10-05_Tricholoma_magnivelare_%28Peck%29_Redhead_972957.jpg" },
  { id: 12, key: "anonna_san_pablo", name: "Anonna San Pablo", sci: "Annona reticulata", url: "https://upload.wikimedia.org/wikipedia/commons/f/f2/Annona_reticulata_fruit.JPG" },
  { id: 13, key: "saramuyo", name: "Saramuyo", sci: "Annona squamosa", url: "https://upload.wikimedia.org/wikipedia/commons/4/42/Sugar_apple_on_tree.jpg" },
  { id: 14, key: "naranja_sangria", name: "Naranja Sangría", sci: "Citrus sinensis", url: "https://upload.wikimedia.org/wikipedia/commons/5/5d/BloodOrange.jpg" },
  { id: 15, key: "manzana_pearly_pink", name: "Manzana Pearly Pink", sci: "Malus domestica", url: "https://upload.wikimedia.org/wikipedia/commons/3/3a/Pink_Pearl_%285207256521%29.jpg" },
  { id: 16, key: "kaniste", name: "Kaniste", sci: "Pouteria campechana", url: "https://upload.wikimedia.org/wikipedia/commons/7/7d/Canistel.jpg" },
  { id: 17, key: "mostaza_miz_america", name: "Mostaza Miz America", sci: "Brassica juncea", url: "https://upload.wikimedia.org/wikipedia/commons/c/cd/Mizuna_001.jpg" },
  { id: 18, key: "mostaza_fresse", name: "Mostaza Fresse", sci: "Brassica juncea", url: "https://upload.wikimedia.org/wikipedia/commons/4/42/Brassica_juncea_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-168.jpg" },
  { id: 19, key: "mostaza_ruby_streaks", name: "Mostaza Ruby Streaks", sci: "Brassica juncea", url: "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?auto=format&fit=crop&w=800&q=85" },
  { id: 20, key: "ube", name: "Ube", sci: "Dioscorea purpurea", url: "https://upload.wikimedia.org/wikipedia/commons/3/3c/Dioscorea_alata_-_Purple_yam_tuber_-_Mindanao%2C_Philippines.jpg" },
  { id: 21, key: "espinaca_okinawa", name: "Espinaca de Okinawa", sci: "Gynura bicolor", url: "https://upload.wikimedia.org/wikipedia/commons/6/60/Gynura_bicolor_vegetable_%28hongfeng_cai_%E7%B4%85%E9%B3%B3%E8%8F%9C%29.png" }
];

async function processAll() {
  console.log("Iniciando descarga y optimización de las 21 especies botánicas reales...");
  for (const item of productosBotanica) {
    try {
      console.log(`[${item.id}/21] Descargando ${item.name} (${item.sci})...`);
      const res = await fetch(item.url, {
        headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) NectarFarms/1.0' }
      });
      if (!res.ok) {
        throw new Error(`HTTP ${res.status} al descargar ${item.url}`);
      }
      const buffer = Buffer.from(await res.arrayBuffer());

      const outPath = path.join(targetDir, `${item.key}.webp`);

      // Procesamiento con sharp:
      // - Redimensionar y recortar inteligentemente con proporción limpia 4:3 (600x450px)
      // - Ligera mejora de contraste y nitidez para estética de catálogo gourmet
      // - Conversión a WebP con calidad 85 sin metadatos residuales
      await sharp(buffer)
        .resize(600, 450, { fit: 'cover', position: 'center' })
        .modulate({ brightness: 1.02, saturation: 1.08 })
        .sharpen()
        .webp({ quality: 85, effort: 6 })
        .toFile(outPath);

      const stats = fs.statSync(outPath);
      console.log(`  ✓ Guardado exitosamente: assets/productos/${item.key}.webp (${Math.round(stats.size / 1024)} KB)`);
    } catch (e) {
      console.error(`  ✗ Error procesando ${item.name}:`, e.message);
    }
  }
  console.log("¡Todas las 21 especies botánicas han sido procesadas a formato WebP!");
}

processAll();
