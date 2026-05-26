from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml
from lib.limpieza import eliminar_duplicados, contar_vacios
from lib.auditoria import auditar_fichero
from lib.exportacion import crear_csv, crear_excel_completo, crear_informe_txt

def main():
    print("==== INFORME PRACTICA FINAL ====")
    try:
        # 1. FASE DE CARGA
        artistas = cargar_csv('datos/artistas.csv')
        programa = cargar_excel('datos/escenarios_horarios.xlsx')
        patrocinadores = cargar_xml('datos/patrocinadores.xml')
        ventas = cargar_json('datos/ventas_entradas.json')
        print("✔ ¡Todos los ficheros cargados correctamente en memoria!\n")
    except Exception as e:
        print(f"❌ Error crítico al cargar los archivos: {e}")
        return
    
    # 2. FASE DE AUDITORÍA INICIAL
    # Corregido: Ahora se pasan los parámetros obligatorios que pide tu modulo auditoria.py
    auditar_fichero("artistas", artistas, ["nombre_artista"])
    auditar_fichero("escenarios_horarios", programa, ["escenario", "hora_inicio"])
    auditar_fichero("patrocinadores", patrocinadores, ["nombre_empresa"])
    auditar_fichero("ventas_entradas", ventas, ["id_entrada"])

    print("\n✔ Auditoría inicial completada.")
    print("Presiona Enter para proceder con las fases de limpieza y depuración...")
    input()  

    # FASES DE LIMPIEZA Y FILTRADO
    
    artistas_limpios, dup_artistas = eliminar_duplicados(artistas, ["nombre_artista"])
    programa_limpio, dup_programa = eliminar_duplicados(programa, ["escenario", "hora_inicio"])
    patrocinadores_limpios, dup_patrocinadores = eliminar_duplicados(patrocinadores, ["nombre_empresa"])
    ventas_limpias, dup_ventas = eliminar_duplicados(ventas, ["id_entrada"])
    print("✔ Limpieza de duplicados e integridad completada de forma estricta.")

    # EXPORTACIÓN DE RESULTADOS
    carpeta_salida = 'datos_limpios'

    # Exportamos los 4 CSV
    crear_csv(artistas_limpios, 'artistas_limpio.csv', carpeta_salida)
    crear_csv(programa_limpio, 'escenarios_horarios_limpio.csv', carpeta_salida)
    crear_csv(patrocinadores_limpios, 'patrocinadores_limpio.csv', carpeta_salida)
    crear_csv(ventas_limpias, 'ventas_entradas_limpio.csv', carpeta_salida)

    datos_excel = {
        'artistas_limpios': artistas_limpios,
        'escenarios_horarios_limpios': programa_limpio,
        'patrocinadores_limpios': patrocinadores_limpios,
        'ventas_entradas_limpias': ventas_limpias
    }
    
    # Exportamos el libro de excel
    crear_excel_completo(datos_excel, carpeta_salida, 'datos_completos')

    # Guardamos e imprimimos el informe
    crear_informe_txt(carpeta_salida)

    print("\n=======================================================")
    print("✔ ¡PROCESO COMPLETO EJECUTADO Y FINALIZADO CON ÉXITO!")
    print("=======================================================")

if __name__ == "__main__":
    main()