

def limpiar_id(id):
    if not id:
        return 'vacio'
    id = str(id).strip()
    id = id.lower()
    return id


def limpiar_texto(valor, minusculas=True):
    if not valor:
        return 'vacio'
    valor = str(valor).strip()
    valor = " ".join(valor.split())
    return valor.lower() if minusculas else valor

def limpiar_eur(valor):
    if not valor:
        return 'vacio'
    valor = str(valor).replace('€', '').strip()
    valor = valor.replace('$', '')
    valor = valor.replace(',', '.')
    valor = round(float(valor), 2)
    return valor


def limpiar_fecha(valor): # falta unificar formato
    if not valor:
        return 'vacio'
    valor = valor.strip()
    valor= valor.replace('-','/')
    valor = valor[2/2/4]
    return valor

def limpiar_hora(valor): # fallo despues de la hora pone none
    if not valor:
        return 'vacio'
    valor = str(valor).strip().upper()
    valor = valor.replace('.', ':').replace('PM', '').replace('AM', '')
    valor = valor.strip()
    return valor



def limpiar_soundcheck(valor):
    if not valor:
        return 'vacio'
    valor = str(valor).strip()
    valor = valor.replace('PM', '').replace(':', '')
    valor = valor.replace('.', '').replace('AM', '')
    return valor


def limpiar_dni(dni):
    if dni == dni.zfill(9).upper():
        return dni
    elif dni != dni.zfill(9):
        print('dni erroneo')
    elif dni == 'N/A':
        print('vacio')
    

def procesar_artistas(lista,nombre):
    lista_limpia = []
    for item in lista:
        item_limpio = {
            'id_artista': limpiar_id(item.get('id_artista')),
            'nombre': limpiar_texto(item.get('nombre')),
            'genero_musical': limpiar_texto(item.get('genero_musical')),
            'pais': limpiar_texto(item.get('pais')),
            'cache_eur': limpiar_eur(item.get('cache_eur')),
            'email_manager': limpiar_texto(item.get('email_manager')),
            'telefono': limpiar_texto(item.get('telefono'))
        }
        lista_limpia.append(item_limpio)
    return lista_limpia

def procesar_programa(lista,nombre):
    lista_limpia = []
    for item in lista:
        item_limpio = {
            'fecha': limpiar_fecha(item.get('fecha')),
            'escenario': limpiar_texto(item.get('escenario')),
            'artista': limpiar_texto(item.get('artista')),
            'hora_inicio': limpiar_hora(item.get('hora_inicio')),
            'hora_fin': limpiar_hora(item.get('hora_fin')),
            'soundcheck': limpiar_soundcheck(item.get('soundcheck')),
            'notas': limpiar_texto(item.get('notas'))
        }
        lista_limpia.append(item_limpio)
    return lista_limpia

def procesar_ventas(lista,nombre):
    lista_limpia = []
    for item in lista:
        item_limpio = {
            'id_venta': limpiar_id(item.get('id_venta')),
            'nombre_comprador': limpiar_texto(item.get('nombre_comprador')),
            'email': limpiar_texto(item.get('email')),
            'dni': limpiar_dni(item.get('dni')),
            'tipo_entrada': limpiar_texto(item.get('tipo_entrada')),
            'precio': limpiar_eur(item.get('precio')),
            'fecha_compra': limpiar_fecha(item.get('fecha_compra')),
            'metodo_pago': limpiar_texto(item.get('metodo_pago'))
        }
        lista_limpia.append(item_limpio)
    print(lista_limpia)


def procesar_patrocinadores(lista,nombre):
    lista_limpia = []
    for item in lista:
        item_limpio = {
            'nombre_empresa': limpiar_texto(item('nombre_empresa')),
            'contacto': limpiar_texto(item('contacto')),
            'email': limpiar_texto(item('email')),
            'importe_patrocinio': limpiar_eur(item('importe_patrocinio')),
            'categoria': limpiar_texto(item('categoria')),
            'fecha_inicio': limpiar_fecha(item('fecha_inicio')),
            'fecha_fin': limpiar_fecha(item('fecha_fin'))
        }
        lista_limpia.append(item_limpio)
    print(lista_limpia)





# artistas = leer_csv('datos', 'artistas.csv')
# programa = cargar_excel('datos', 'escenarios_horarios.xlsx')
# ventas = cargar_json('datos', 'ventas_entradas.json')
# patrocinadores = cargar_xml('datos', 'patrocinadores.xml')