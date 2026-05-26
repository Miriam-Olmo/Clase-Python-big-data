# creacion de carpeta datos limpios con csv, excel, json,xml
import os
from openpyxl import Workbook
import csv



def crear_csv(lista, nombre, carpeta):
    """Genera un archivo CSV individual por cada fichero original"""
    os.makedirs(carpeta, exist_ok=True)
    
    fichero = open(f"./{carpeta}/{nombre}", 'w', encoding='UTF-8', newline='')
    
    if lista:
        # Extraemos las cabeceras de las llaves del diccionario
        cabeceras = list(lista[0].keys())
        
        mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras)
        mi_csv.writeheader()
        
        # escribe todas las filas con los datos limpios
        mi_csv.writerows(lista)
        
    fichero.close()
    print(f"✔ Archivo CSV '{nombre}' guardado correctamente en ./{carpeta}")



def crear_excel_completo(diccionario_de_datos, carpeta, nombre_archivo="datos_completos"):
    # 1. Creamos la carpeta si no existe
    os.makedirs(carpeta, exist_ok=True)
    
    # 2. Ruta completa con la extensión .xlsx
    ruta_completa = f"./{carpeta}/{nombre_archivo}.xlsx"
    
    # 3. Creamos el archivo Excel
    excel = Workbook()
    
    # Grabamos la hoja que viene
    hoja_activa = excel.active
    primer_fichero = True
    
    # 4. Recorremos el diccionario para crear cada pestaña de forma automática
    for nombre_pestaña, lista_datos in diccionario_de_datos.items():
        
        if primer_fichero:
            # Para el primer fichero, usamos la hoja por defecto y le cambiamos el nombre
            hoja_actual = hoja_activa
            hoja_actual.title = nombre_pestaña
            primer_fichero = False # Cambiamos el interruptor
        else:
            # Para los siguientes ficheros, creamos una pestaña nueva con su nombre correcto
            hoja_actual = excel.create_sheet(title=nombre_pestaña)
        
        # 5. Si la lista tiene datos, los metemos SOLAMENTE en la hoja de esta vuelta
        if lista_datos:
            # Ponemos las cabeceras (las llaves del primer diccionario)
            cabeceras = list(lista_datos[0].keys())
            hoja_actual.append(cabeceras)
            
            # Ponemos los datos fila por fila
            for registro in lista_datos:
                valores_fila = list(registro.values())
                hoja_actual.append(valores_fila)
                
    # 6. Guardamos el archivo físico con todas sus hojas dentro
    excel.save(ruta_completa)
    print(f"Excel creado correctamente en: {ruta_completa}")


def crear_informe_txt(carpeta, nombre_archivo="informe_limpieza.txt"):
    """Crea e imprime por pantalla el informe final estático exigido (Fase 10)"""
    os.makedirs(carpeta, exist_ok=True)
    ruta_completa = f"./{carpeta}/{nombre_archivo}"
    
    # Texto plano exacto requerido por la plantilla de tu enunciado
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
    
    # 1. Imprimir por pantalla (Requisito)
    print("\n" + "="*50)
    print(texto_informe)
    print("="*50 + "\n")
    
    # 2. Guardar en el fichero txt usando open (Requisito)
    fichero = open(ruta_completa, 'w', encoding='utf-8')
    fichero.write(texto_informe)
    fichero.close()
    print(f"✔ Archivo de texto '{nombre_archivo}' generado correctamente.")
