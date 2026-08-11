const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

async function processLeaf() {
  console.log("Iniciando procesamiento y estilización botánica de Mostaza Ruby Streaks...");
  
  const sourcePath = path.join(__dirname, 'hoja_ruby_streaks_raw.jpg');
  if (!fs.existsSync(sourcePath)) {
    throw new Error("No se encontró hoja_ruby_streaks_raw.jpg");
  }

  // 1. Cargar imagen y obtener datos en crudo (raw RGBA)
  const image = sharp(sourcePath).ensureAlpha();
  const { data, info } = await image.raw().toBuffer({ resolveWithObject: true });
  
  const width = info.width;
  const height = info.height;
  const channels = info.channels;
  
  // 2. Remover fondo blanco matemáticamente (R > 235, G > 235, B > 235 -> Alpha 0)
  for (let i = 0; i < data.length; i += channels) {
    const r = data[i];
    const g = data[i + 1];
    const b = data[i + 2];
    if (r > 235 && g > 235 && b > 235) {
      data[i + 3] = 0; // Transparente
    }
  }

  // 3. Reconstruir PNG con transparencia y recortar bordes vacíos
  const transparentPng = await sharp(data, {
    raw: { width, height, channels: 4 }
  })
  .png()
  .toBuffer();

  const trimmedPng = await sharp(transparentPng)
    .trim()
    .png()
    .toBuffer();

  // 4. Redimensionar hoja a altura elegante de 340px manteniendo proporción
  // 6. Realzar saturación (+40%) y contraste (+15%)
  const styledLeafBuffer = await sharp(trimmedPng)
    .resize({ height: 340, fit: 'inside' })
    .modulate({ saturation: 1.4, brightness: 1.02 })
    .linear(1.15, -(128 * 0.15))
    .png()
    .toBuffer();

  const leafMeta = await sharp(styledLeafBuffer).metadata();
  const leafW = leafMeta.width;
  const leafH = leafMeta.height;

  // 7. Generar Drop Shadow difuminada (tono carbón rgba(45, 49, 46, 0.15) con Gaussian blur)
  const leafRaw = await sharp(styledLeafBuffer).raw().toBuffer({ resolveWithObject: true });
  const shadowData = Buffer.alloc(leafRaw.data.length);
  for (let i = 0; i < leafRaw.data.length; i += 4) {
    const alpha = leafRaw.data[i + 3];
    if (alpha > 0) {
      shadowData[i] = 45;     // R carbón
      shadowData[i + 1] = 49; // G carbón
      shadowData[i + 2] = 46; // B carbón
      shadowData[i + 3] = Math.round(alpha * 0.18); // Opacidad de sombra
    } else {
      shadowData[i + 3] = 0;
    }
  }

  const shadowBuffer = await sharp(shadowData, {
    raw: { width: leafW, height: leafH, channels: 4 }
  })
  .png()
  .toBuffer();

  const shadowBlurred = await sharp(shadowBuffer)
    .blur(12)
    .png()
    .toBuffer();

  // 8. Crear lienzo 600x450 px tono gris-cálido premium (#F2F3F0)
  const canvasW = 600;
  const canvasH = 450;
  const posX = Math.round((canvasW - leafW) / 2);
  const posY = Math.round((canvasH - leafH) / 2);

  const background = sharp({
    create: {
      width: canvasW,
      height: canvasH,
      channels: 4,
      background: { r: 242, g: 243, b: 240, alpha: 1 }
    }
  });

  // 9. Componer sombra con offset (+8, +8) y hoja centrada
  const outPath = path.join(__dirname, 'assets', 'productos', 'mostaza_ruby_streaks.webp');
  
  await background
    .composite([
      { input: shadowBlurred, top: Math.min(canvasH - leafH, posY + 8), left: Math.min(canvasW - leafW, posX + 8) },
      { input: styledLeafBuffer, top: posY, left: posX }
    ])
    .webp({ quality: 90, effort: 6 })
    .toFile(outPath);

  const stats = fs.statSync(outPath);
  console.log(`¡Estilización botánica de Ruby Streaks completada con éxito!`);
  console.log(`Guardado en: ${outPath} (${Math.round(stats.size / 1024)} KB)`);
}

processLeaf().catch(console.error);
