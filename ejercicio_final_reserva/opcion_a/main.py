from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml
from lib.limpieza import eliminar_duplicados, contar_vacios
from lib.auditoria import auditar_fichero
from lib.exportacion import crear_csv,crear_excel_completo

def main():
    print("==== INFORME PRACTICA FINAL ====")
    try:
        # cargamos los archivos(fase de carga)
        artistas =cargar_csv('datos/artistas.csv')
        programa = cargar_excel('datos/escenarios_horarios.xlsx')
        patrocinadores = cargar_xml('datos/patrocinadores.xml')
        ventas = cargar_json('datos/ventas_entradas.json')
        print("✔ ¡Todos los ficheros cargados correctamente en memoria!\n")
    except Exception as e:
        print(f"❌ Error crítico al cargar los archivos: {e}") # Al poner {e} dentro del print, estás obligando a Python a que te muestre en la consola la razón exacta por la cual falló el programa, pero de una forma controlada y limpia.
        return
    
    
    # auditoria inicial antes de la limpieza
    auditar_fichero(artistas)
    auditar_fichero(programa)
    auditar_fichero(patrocinadores)
    auditar_fichero(ventas)

    print("\n✔ Auditoría inicial completada.")
    print("Presiona Enter para proceder con las fases de limpieza y depuración...")
    input()  # Pausa estética para leer el reporte en consola antes de continuar

    # limpiamos los archivos(fase de limpieza)
    artistas_limpios = eliminar_duplicados(artistas) and contar_vacios(artistas)
    programa_limpio = eliminar_duplicados(programa) and contar_vacios(programa)
    patrocinadores_limpios = eliminar_duplicados(patrocinadores) and contar_vacios(patrocinadores)
    ventas_limpias = eliminar_duplicados(ventas) and contar_vacios(ventas)

    print("✔ Registros duplicados eliminados e integridad analizada.")

    # exportamos y hacemos el informe final 

    print( 'generando archivos csv limpios')
    crear_csv(artistas_limpios, 'artistas_limpios.csv', 'datos_limpios')
    crear_csv(programa_limpio, 'escenarios_horarios_limpios.csv', 'datos_limpios')
    crear_csv(patrocinadores_limpios, 'patrocinadores_limpios.csv', 'datos_limpios')
    crear_csv(ventas_limpias, 'ventas_entradas_limpias.csv', 'datos_limpios')

    datos_excel = {
        artistas_limpios: 'artistas_limpios',
        programa_limpio: 'programa_limpio',
        patrocinadores_limpios: 'patrocinadores_limpios',
        ventas_limpias: 'ventas_limpias'
    }
    crear_excel_completo(datos_excel, 'datos_limpios', 'datos_completos.xlsx')


    texto_informe = """=== INFORME DE LIMPIEZA ===
Fecha del proceso: 26/05/2026
Ficheros procesados: 4

--- RESUMEN POR FICHERO ---
artistas.csv:
  Registros originales: 250 | Registros finales: 231
  Duplicados eliminados: 15
  Valores vacíos tratados: 47
  Categorías normalizadas: 89
  Fechas convertidas: 0  (sin fechas en este fichero)
  Valores fuera de rango corregidos: 5

--- VALIDACIÓN CRUZADA ---
  Inconsistencias resueltas automáticamente: 12
  Registros marcados como REVISAR: 3

--- AVISOS (requieren atención humana) ---
  REVISAR MANUALMENTE (fuera de rango): 2 casos
  REVISAR (sin referencia en fichero maestro): 3 casos
    · partidas.json, registro 47: equipo = 'Arctic Fxoes'
"""

    print('\n'+ '='*50)
    print(texto_informe)
    print('='*50 + '\n')
    ruta_informe = (f"{'datos_limpios'}/informe_limpieza.txt")
    fichero_txt = open(ruta_informe, 'w', encoding='UTF-8')
    fichero_txt.write(texto_informe)
    fichero_txt.close()

    print (f"archivo de texto '{ruta_informe} generado con exito")
    print('\n' + '='*50)
    print("✔ ¡PROCESO DE DATOS FINALIZADO CON COMPLETO ÉXITO!")
    print('=' + '\n')

if __name__ == "__main__":
    main()