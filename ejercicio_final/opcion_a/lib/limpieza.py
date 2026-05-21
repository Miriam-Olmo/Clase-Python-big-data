

def limpiar_id(id_artista):
    if not id_artista:
        return 'vacio'
    id_artista = str(id_artista).strip()
    return id_artista


def limpiar_texto(valor, minusculas = True):
    if not valor:
        return None
    valor = str(valor).strip()
    return valor.lower() if minusculas else valor.upper()

def limpiar_cache_eur(valor):
    if not valor:
        return 'desconocido'
    valor = str(valor).replace('€', '').strip()
    valor = valor.replace(',', '.')
    valor = round(float(valor), 2)
    return valor

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






artistas = leer_csv('datos', 'artistas.csv')
programa = cargar_excel('datos', 'escenarios_horarios.xlsx')
ventas = cargar_json('datos', 'ventas_entradas.json')
patrocinadores = cargar_xml('datos', 'patrocinadores.xml')