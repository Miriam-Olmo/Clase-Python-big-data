from lib.carga import leer_csv, cargar_excel, cargar_json, cargar_xml
from lib.limpieza import procesar_artistas, procesar_programa, procesar_ventas, procesar_patrocinadores,limpiar_id,limpiar_dni,limpiar_texto,limpiar_eur,limpiar_fecha

artistas = leer_csv('datos', 'artistas.csv')
programa = cargar_excel('datos', 'escenarios_horarios.xlsx')
ventas = cargar_json('datos', 'ventas_entradas.json')
patrocinadores = cargar_xml('datos', 'patrocinadores.xml')

artistas_limpio = procesar_artistas(artistas, 'artistas_limpio.csv')

programa_limpio = procesar_programa(programa, 'programa_limpio.xlsx')

ventas_limpias = procesar_ventas(ventas, 'ventas_limpias.json')

patrocinadores_limpios = procesar_patrocinadores(patrocinadores, 'patrocinadores_limpios.xml')






# def normalizar_texto(texto):
#     """
#     Normaliza un texto aplicando limpieza, corrección de tildes y formato.

#     La función realiza varias transformaciones sobre el texto recibido:
#     - Limpia espacios y normaliza el formato utilizando `limpiar_texto()`.
#     - Convierte el texto a minúsculas.
#     - Corrige palabras según un diccionario de tildes.
#     - Reconstruye el texto con la primera letra en mayúscula.

#     Parámetros:
#         texto (str): Texto que se desea normalizar.

#     Retorna:
#         str: Texto normalizado y corregido.

#     Funcionamiento:
#         - Limpia el texto mediante la función `limpiar_texto()`.
#         - Convierte todo el texto a minúsculas.
#         - Divide el texto en palabras.
#         - Comprueba cada palabra en el diccionario `correcciones_tildes`.
#         - Sustituye las palabras encontradas por su versión corregida.
#         - Une nuevamente las palabras en una sola cadena.
#         - Convierte la primera letra del texto a mayúscula.

#     Ejemplos:
#         Suponiendo el siguiente diccionario:

#         >>> correcciones_tildes = {
#         ...     "camion": "camión",
#         ...     "arbol": "árbol"
#         ... }

#         >>> normalizar_texto("  CAMION rojo ")
#         'Camión rojo'

#         >>> normalizar_texto("ARBOL grande")
#         'Árbol grande'

#     Requisitos:
#         - Debe existir previamente:
#               - La función `limpiar_texto()`
#               - El diccionario `correcciones_tildes`
#         - `correcciones_tildes` debe contener pares:
#               palabra_sin_tilde -> palabra_corregida

#     Excepciones:
#         IndexError:
#             Puede producirse si el texto resultante está vacío y se intenta
#             acceder a `texto[0]`.

#     Notas:
#         - Solo corrige palabras exactas presentes en el diccionario.
#         - La capitalización final afecta únicamente a la primera letra
#           del texto completo.
#     """
#     texto = limpiar_texto(texto)
#     texto = texto.lower()
#     palabras = texto.split()
#     palabras_corregidas = []

#     for palabra in palabras:
#         if palabra in correcciones_tildes:
#             palabras_corregidas.append(correcciones_tildes[palabra])
#         else:
#             palabras_corregidas.append(palabra)

#     texto = " ".join(palabras_corregidas)
#     texto = texto[0].upper() + texto[1:]

#     return texto
    
    
#     mapeo_generos = {
#     # Rock
#     "rock":         "Rock",
#     "rokc":         "Rock",
#     "roc":          "Rock",
#     "rock":         "Rock",
#     "ROCK":         "Rock",

#     # Electrónica
#     "electro":      "Electrónica",
#     "electronica":  "Electrónica",
#     "Electronica":  "Electrónica",
#     "ELECTRONICA":  "Electrónica",
#     "Electrónica":  "Electrónica",
#     "Electrónic":   "Electrónica",

#     # Hip Hop
#     "hip hop":      "Hip Hop",
#     "hip-hop":      "Hip Hop",
#     "Hip Hop":      "Hip Hop",
#     "Hip-Hop":      "Hip Hop",
#     "HIP HOP":      "Hip Hop",
#     "HipHop":       "Hip Hop",

#     # Jazz
#     "jazz":         "Jazz",
#     "Jazz":         "Jazz",
#     "JAZZ":         "Jazz",
#     "Jaz":          "Jazz",

#     # Metal
#     "metal":        "Metal",
#     "Metal":        "Metal",
#     "METAL":        "Metal",
#     "Metall":       "Metal",

#     # Pop
#     "pop":          "Pop",
#     "Pop":          "Pop",
#     "POP":          "Pop",
#     "Ppo":          "Pop",

#     # R&B
#     "r&b":          "R&B",
#     "R&B":          "R&B",
#     "R & B":        "R&B",
#     "rnb":          "R&B",
#     "RnB":          "R&B",

#     # Reggaetón
#     "reggaeton":    "Reggaetón",
#     "Reggaeton":    "Reggaetón",
#     "REGGAETON":    "Reggaetón",
#     "Reggaetón":    "Reggaetón",
#     "regueton":     "Reggaetón",
#     "Reguetón":     "Reggaetón",

#     # Ska
#     "ska":          "Ska",
#     "Ska":          "Ska",
#     "SKA":          "Ska",

#     # Salsa
#     "salsa":        "Salsa",
#     "Salsa":        "Salsa",
#     "SALSA":        "Salsa",

#     # Techno
#     "techno":       "Techno",
#     "Techno":       "Techno",
#     "TECHNO":       "Techno",
#     "Tekno":        "Techno",

#     # Flamenco
#     "flamenco":     "Flamenco",
#     "Flamenco":     "Flamenco",
#     "FLAMENCO":     "Flamenco",
#     "Flamenko":     "Flamenco",

#     # Folk
#     "folk":         "Folk",
#     "Folk":         "Folk",
#     "FOLK":         "Folk",

#     # Indie
#     "indie":        "Indie",
#     "Indie":        "Indie",
#     "INDIE":        "Indie",
#     "Indy":         "Indie",

#     # Cumbia
#     "cumbia":       "Cumbia",
#     "Cumbia":       "Cumbia",
#     "CUMBIA":       "Cumbia",
#     "Kunbia":       "Cumbia",
# }