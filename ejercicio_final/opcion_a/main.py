from lib.carga import leer_csv, cargar_excel, cargar_json, cargar_xml
from lib.limpieza import procesar_artistas, 

artistas = leer_csv('datos', 'artistas.csv')
programa = cargar_excel('datos', 'escenarios_horarios.xlsx')
ventas = cargar_json('datos', 'ventas_entradas.json')
patrocinadores = cargar_xml('datos', 'patrocinadores.xml')


artistas_limpios = procesar_artistas(artistas)

def procesar_artistas(lista):
    lista_limpia = []
    for item in lista:
        item_limpio = {
            'id_artista': limpiar_id(item['id_artista']),
            'nombre': limpiar_texto(item['nombre']),
            'genero_musical': limpiar_texto(item['genero_musical']),
            'pais': limpiar_texto(item['pais']),
            'cache_eur': limpiar_cache_eur(item['cache_eur']),
            'email_manager': limpiar_texto(item['email_manager']),
            'telefono': limpiar_texto(item['telefono'])
        }
        lista_limpia.append(item_limpio)
    return lista_limpia

