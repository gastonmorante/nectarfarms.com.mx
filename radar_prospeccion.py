"""
NectarCore - Radar de Prospección de Alta Gastronomía & Chefs
Módulo para identificar y perfilar restaurantes Fine Dining y Directores F&B en Riviera Maya, CDMX y Oaxaca.
"""

import json

RESTAURANTES_PROSPECCION = [
    {
        "nombre": "Restaurante Arca Tulum",
        "chef": "José Luis Hinostroza",
        "ubicacion": "Tulum, Quintana Roo",
        "categoria": "Cocina a la leña / Botánica Silvestre",
        "productos_potenciales": ["Lobster Mushroom", "Morillas", "Matsutake", "Naranja Sangría"]
    },
    {
        "nombre": "Hartwood Tulum",
        "chef": "Eric Werner",
        "ubicacion": "Tulum, Quintana Roo",
        "categoria": "Sustentable / 100% Producto Local y Cero Huella",
        "productos_potenciales": ["Porcini", "Hongo Azul", "Duraznillo", "Espinaca de Okinawa"]
    },
    {
        "nombre": "Pujol",
        "chef": "Enrique Olvera / Jesús Durón",
        "ubicacion": "Ciudad de México",
        "categoria": "Alta Cocina Mexicana de Autor",
        "productos_potenciales": ["Tecomate", "Mantecado", "Hongo Coral", "Saramuyo", "Kaniste"]
    },
    {
        "nombre": "Criollo Oaxaca",
        "chef": "Luis Arellano",
        "ubicacion": "Oaxaca de Juárez",
        "categoria": "Cocina de Origen & Etnobotánica",
        "productos_potenciales": ["Matsutake", "Duraznillo", "Hongos de Recolección", "Mix de Mostazas"]
    }
]

def ejecutar_radar():
    print("==========================================================")
    print("      NECTAR FARMS - RADAR DE PROSPECCIÓN GASTRONÓMICA    ")
    print("==========================================================")
    print(f"Detectados {len(RESTAURANTES_PROSPECCION)} prospectos prioritarios:")
    for r in RESTAURANTES_PROSPECCION:
        print(f"• {r['nombre']} ({r['ubicacion']}) - Chef: {r['chef']}")
        print(f"  Ingredientes afines: {', '.join(r['productos_potenciales'])}\n")
    
    with open("radar_prospeccion.json", "w", encoding="utf-8") as f:
        json.dump(RESTAURANTES_PROSPECCION, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    ejecutar_radar()
