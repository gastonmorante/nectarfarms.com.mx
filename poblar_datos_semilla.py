"""
NectarCore - Módulo de Población de Datos Semilla
Carga los 20 productos oficiales de Nectar Farms y restaurantes pioneros de alta gastronomía.
"""

import json

PRODUCTOS_SEMILLA = [
    {
        "id": 1, "name": "Porcini", "sci": "Boletus sp.", "temp": "Julio - Septiembre",
        "origin": "Bosques del Altiplano Central",
        "desc": "Hongo silvestre de sabor terroso y a nuez profunda, textura carnosa codiciada en salsas y risottos.",
        "propiedades": "Alto en fibra prebiótica, soporte al microbioma digestivo.",
        "receta": "Risotto trufado al parmesano reggiano o costra deshidratada para solomillo.",
        "img": "https://images.unsplash.com/photo-1634045542718-45be5d36b802?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 2, "name": "Lobster", "sci": "Hypomyces lactifluorum", "temp": "Agosto - Octubre",
        "origin": "Bosques de Michoacán",
        "desc": "Hongo silvestre parasitado de color naranja brillante. Sabor que evoca mariscos y textura crujiente.",
        "propiedades": "Rico en antioxidantes y compuestos inmunomoduladores.",
        "receta": "Sauté de Lobster con mantequilla de avellana y tacos gourmet de autor.",
        "img": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 3, "name": "Hongo Azul", "sci": "Lactarius indigo", "temp": "Julio - Septiembre",
        "origin": "Sierras de Hidalgo",
        "desc": "Joya visual azul añil metálico. Sabor terroso suave y láminas firmes que mantienen su color al cocinarse.",
        "propiedades": "Antimicrobiano natural, rico en minerales esenciales.",
        "receta": "Carpaccio fúngico con emulsión de cítricos y flor de sal de Colima.",
        "img": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 4, "name": "Duraznillo", "sci": "Cantharellus cibarius", "temp": "Julio - Septiembre",
        "origin": "Sierra de Oaxaca",
        "desc": "Sabor sutilmente afrutado a chabacano. Color amarillo dorado y textura elástica preferida por chefs.",
        "propiedades": "Excelente fuente de vitamina D y complejo B.",
        "receta": "Reducción de Duraznillo con chalotas y tomillo para acompañar aves de caza.",
        "img": "https://images.unsplash.com/photo-1610444585141-8f5b89eb0df6?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 5, "name": "Rovellón", "sci": "Lactarius deliciosus", "temp": "Otoño (Octubre - Noviembre)",
        "origin": "Bosques templados del centro",
        "desc": "Hongo naranja encendido con círculos concéntricos. Textura muy consistente y umami profundo.",
        "propiedades": "Antiinflamatorio y protector cardiovascular.",
        "receta": "Asado a la parrilla de leña con chimichurri de hierbas locales.",
        "img": "https://images.unsplash.com/photo-1506084868230-bb9d95c24759?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 6, "name": "Clavito", "sci": "Lyophyllum decastes", "temp": "Agosto - Septiembre",
        "origin": "Sierra de Toluca",
        "desc": "Crece en densos racimos. Textura elástica y firme ideal para cocciones prolongadas.",
        "propiedades": "Soporte en la regulación de glucosa en sangre, adaptógeno inmune.",
        "receta": "Estofados de larga cocción o encurtido en vinagre de manzana y especias.",
        "img": "https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 7, "name": "Tecomate", "sci": "Amanita caesarea", "temp": "Junio - Septiembre",
        "origin": "Bosques húmedos de México",
        "desc": "El hongo de los césares. Sombrero naranja brillante y sabor dulce, delicado y ligeramente almendrado.",
        "propiedades": "Rico en aminoácidos esenciales, protector hepático leve.",
        "receta": "Carpaccio ultra fino en crudo con aceite extravirgen y lascas de queso curado.",
        "img": "https://images.unsplash.com/photo-1594911774802-8822a707cbb3?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 8, "name": "Mantecado", "sci: "Amanita rubescens", "temp": "Julio - Septiembre",
        "origin": "Bosques templados de pino",
        "desc": "Sombrero pardo que enrojece al corte. Textura sumamente mantecosa y perfil a frutos secos.",
        "propiedades": "Alto contenido mineral. Requiere cocción completa.",
        "receta": "Salteado a fuego vivo con mantequilla clarificada y ajo confitado.",
        "img": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 9, "name": "Hongo Coral", "sci": "Ramaria sp.", "temp": "Julio - Septiembre",
        "origin": "Zonas montañosas de México",
        "desc": "Estructura ramificada como coral marino. Textura tierna con puntas ligeramente crujientes.",
        "propiedades": "Alto en antioxidantes, promueve digestión saludable.",
        "receta": "Tempura crujiente con mayonesa de ajo negro y cítricos.",
        "img": "https://images.unsplash.com/photo-1628359419163-e380f6813e33?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 10, "name": "Morilla", "sci": "Morchella sp.", "temp": "Primavera (Marzo - Mayo)",
        "origin": "Faldas de los volcanes de México",
        "desc": "Estructura alveolar icónica. Sabor sumamente complejo, terroso y ahumado, rey de las salsas clásicas.",
        "propiedades": "Altísimo en hierro y vitamina D, refuerza sistema inmune.",
        "receta": "Salsa clásica de morillas a la crema y cognac para cortes finos.",
        "img": "https://images.unsplash.com/photo-1629814479904-80340c2627cb?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 11, "name": "Matsutake", "sci": "Tricholoma magnivelare", "temp": "Septiembre - Noviembre",
        "origin": "Bosques de Oaxaca",
        "desc": "Aroma especiado único con notas a canela y pino. Gran consistencia masticable y prestigio gastronómico.",
        "propiedades": "Potente adaptógeno milenario con inmunomodulación.",
        "receta": "Caldo tradicional Dobin Mushi o asado entero al grill con gotas de yuzu.",
        "img": "https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 12, "name": "Anonna San Pablo", "sci": "Annona reticulata", "temp": "Invierno - Primavera",
        "origin": "Huertos de Yucatán",
        "desc": "Fruta exótica de piel reticulada y pulpa cremosa dulce con notas ácidas sutiles.",
        "propiedades": "Rica en vitamina C y fibra prebiótica.",
        "receta": "Base para helados de autor y mousses frutales con albahaca.",
        "img": "https://images.unsplash.com/photo-1588691334812-bf9dd9d1877f?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 13, "name": "Saramuyo", "sci": "Annona squamosa", "temp": "Julio - Octubre",
        "origin": "Zonas tropicales de Yucatán",
        "desc": "Manzana de azúcar con pulpa segmentada dulce, aromática y tersa para repostería fina.",
        "propiedades": "Alto contenido de potasio y magnesio para salud cardiovascular.",
        "receta": "Sorbete refrescante con infusión de menta fresca.",
        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 14, "name": "Hongos de Recolección", "sci": "Boletus / Amanita sp.", "temp": "Temporada de lluvias",
        "origin": "Bosques y valles de México",
        "desc": "Selección artesanal de hongos silvestres frescos recolectados a mano por expertos locales.",
        "propiedades": "Sinergia de betaglucanos y soporte inmune natural.",
        "receta": "Estofado rústico tradicional con epazote y mantequilla de rancho.",
        "img": "https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 15, "name": "Naranja Sangría", "sci": "Citrus sinensis var. Sangria", "temp": "Noviembre - Febrero",
        "origin": "Huertos cítricos de Yucatán",
        "desc": "Naranja de pulpa rojiza rica en antocianinas con notas a frambuesa y acidez elegante.",
        "propiedades": "Altísima en antocianinas y antioxidantes celulares.",
        "receta": "Reducciones y adobos para pato glaseado o coctelería premium.",
        "img": "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 16, "name": "Manzana Pearly Pink", "sci": "Malus domestica", "temp": "Otoño",
        "origin": "Cultivos seleccionados",
        "desc": "Manzana de piel aperlada rosada y pulpa crujiente con balance agridulce perfecto.",
        "propiedades": "Rica en pectinas que apoyan la salud cardiovascular.",
        "receta": "Ensaladas gourmet Waldorf y maridajes con quesos maduros y miel.",
        "img": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 17, "name": "Kaniste", "sci": "Pouteria campechana", "temp": "Diciembre - Marzo",
        "origin": "Península de Yucatán",
        "desc": "Fruta huevo de pulpa amarilla cremosa que evoca camote dulce y yema de huevo.",
        "propiedades": "Alta concentración de betacarotenos y niacina.",
        "receta": "Cheesecake exótico sin cocción y cremas sedosas de autor.",
        "img": "https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 18, "name": "Mix de Mostazas", "sci": "Brassica juncea", "temp": "Todo el año",
        "origin": "Huertos verticales Nectar",
        "desc": "Mezcla de hojas jóvenes moradas y verdes con perfil picante y aromático.",
        "propiedades": "Alto aporte de clorofila, vitaminas A y C.",
        "receta": "Contraste estético y picante en platos fuertes y ensaladas de microgreens.",
        "img": "https://images.unsplash.com/photo-1506084868230-bb9d95c24759?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 19, "name": "Ube", "sci": "Dioscorea purpurea", "temp": "Otoño - Invierno",
        "origin": "Invernaderos NectarCore",
        "desc": "Tubérculo violeta brillante de sabor dulce con notas de vainilla y coco.",
        "propiedades": "Rico en almidón resistente como prebiótico natural.",
        "receta": "Purés dulces de autor y helados artesanales de tono violeta natural.",
        "img": "https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=400&q=75"
    },
    {
        "id": 20, "name": "Espinaca de Okinawa", "sci": "Gynura bicolor", "temp": "Todo el año",
        "origin": "Cultivo hidropónico Nectar",
        "desc": "Hojas bicolor verde y morado con sabor herbal y sutiles notas a piñón.",
        "propiedades": "Alta en hierro, calcio y flavonoides reguladores de glucosa.",
        "receta": "Tempuras bicolor ligeras y ensaladas de autor de alto impacto visual.",
        "img": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=400&q=75"
    }
]

def poblar():
    print(f"Poblando datos semilla: {len(PRODUCTOS_SEMILLA)} productos cargados.")
    with open("productos_semilla.json", "w", encoding="utf-8") as f:
        json.dump(PRODUCTOS_SEMILLA, f, indent=2, ensure_ascii=False)
    print("Archivo 'productos_semilla.json' generado con éxito.")

if __name__ == '__main__':
    poblar()
