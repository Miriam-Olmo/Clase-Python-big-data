from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml
from lib.limpieza import procesar_artistas, procesar_programa, procesar_ventas, procesar_patrocinadores

def main():
    print("=== FASE 1: CARGA DE FICHEROS ===")
    # 2. Carga de datos originales en memoria
    artistas = cargar_csv('datos/artistas.csv')
    programa = cargar_excel('datos/escenarios_horarios.xlsx')
    ventas = cargar_json('datos/ventas_entradas.json')
    patrocinadores = cargar_xml('datos/patrocinadores.xml')
    print("Todos los ficheros cargados con éxito.\n")

    print("=== FASES 2 A 5: AUDITORÍA, LIMPIEZA Y NORMALIZACIÓN ===")
    
    # Procesamos cada conjunto de datos utilizando tu módulo de limpieza
    print("Procesando tabla de artistas...")
    artistas_limpio = procesar_artistas(artistas)
    
    print("Procesando programa y horarios...")
    programa_limpio = procesar_programa(programa)
    
    print("Procesando ventas de entradas...")
    ventas_limpias = procesar_ventas(ventas)
    
    print("Procesando patrocinadores...")
    patrocinadores_limpios = procesar_patrocinadores(patrocinadores)
    
    print("\n[OK] ¡Todos los datos han sido limpiados y normalizados!")

if __name__ == "__main__":
    main()
