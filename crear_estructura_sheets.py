"""
NectarCore - Módulo de Estructuración de Base de Datos Google Sheets
Crea la arquitectura de hojas de cálculo para Leads, Catálogo de 20 Productos, Pedidos y Muestras de Cortesía.
"""

import json

SHEET_TABS = {
    "LEADS_RESTAURANTES": [
        "ID_Lead", "Fecha_Registro", "Nombre_Contacto", "Restaurante_Hotel", 
        "Tipo_Perfil", "Email", "Telefono_WhatsApp", "Ciudad_Ubicacion", 
        "Productos_Interes", "Estado_Seguimiento", "Muestra_Enviada", "Notas_Chano_IA"
    ],
    "CATALOGO_20_PRODUCTOS": [
        "ID_Producto", "Nombre_Comun", "Nombre_Cientifico", "Categoria", 
        "Origen_Geografico", "Temporada", "Perfil_Organoleptico", "Propiedades_Funcionales", 
        "Sugerencia_Culinaria", "Disponibilidad", "URL_Imagen"
    ],
    "ORDENES_PEDIDOS": [
        "ID_Pedido", "Fecha", "ID_Lead", "Nombre_Cliente", "Productos_Solicitados", 
        "Monto_Total_MXN", "Metodo_Entrega", "Estado_Orden", "Comprobante_Pago"
    ],
    "LOG_CHANO_IA": [
        "ID_Sesion", "Timestamp", "Mensaje_Usuario", "Respuesta_Chano", "Lead_Capturado", "Token_Usage"
    ]
}

def generar_definicion_estructura():
    print("==========================================================")
    print("  NECTAR FARMS (NectarCore) - ARQUITECTURA GOOGLE SHEETS  ")
    print("==========================================================")
    for tab, columns in SHEET_TABS.items():
        print(f"\n[HOJA] {tab} ({len(columns)} columnas):")
        print("  " + " | ".join(columns))
    
    with open("estructura_sheets_nectarcore.json", "w", encoding="utf-8") as f:
        json.dump(SHEET_TABS, f, indent=2, ensure_ascii=False)
    print("\nEstructura guardada exitosamente en 'estructura_sheets_nectarcore.json'.")

if __name__ == '__main__':
    generar_definicion_estructura()
