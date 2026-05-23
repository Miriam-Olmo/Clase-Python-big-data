from lib.carga import resumen,leer_csv, cargar_excel, cargar_json, cargar_xml


artistas = leer_csv('datos', 'artistas.csv')
programa = cargar_excel('datos', 'escenarios_horarios.xlsx')
ventas = cargar_json('datos', 'ventas_entradas.json')
patrocinadores = cargar_xml('datos', 'patrocinadores.xml')








correcciones_tildes = {

    "jose": "José",
    "maria": "María",

    "garcia": "García",
    "gonzalez": "González",
    "martinez": "Martínez",
    "lopez": "López",

    "perez": "Pérez",
    "sanchez": "Sánchez",

    "gomez": "Gómez",
    "fernandez": "Fernández",

    "rodriguez": "Rodríguez",

    "hernandez": "Hernández",

    "ramirez": "Ramírez",

    "gutierrez": "Gutiérrez"
}

def limpiar_texto(texto):

    if texto is None:
        return "vacio"

    texto = str(texto)
     # quitar espacios delante y detrás
    texto = texto.strip()
     # quitar espacios dobles
    texto = " ".join(texto.split())

    return texto



def normalizar_texto(texto):

    texto = limpiar_texto(texto)

    texto = texto.lower()

    palabras = texto.split()

    palabras_corregidas = []

    for palabra in palabras:

        if palabra in correcciones_tildes:

            palabras_corregidas.append(
                correcciones_tildes[palabra]
            )

        else:

            palabras_corregidas.append(
                palabra.capitalize()
            )

    texto_final = " ".join(palabras_corregidas)

    return texto_final


def limpiar_artistas(artistas):

    correcciones = 0

    for artista in artistas:

        campos = [
            "nombre",
            "pais",
            "genero_musical",
            "manager",
            "email_manager"
        ]

        for campo in campos:

            if campo in artista:

                valor_original = artista[campo]

                valor_limpio = normalizar_texto(
                    valor_original
                )

                if valor_original != valor_limpio:
                    correcciones += 1

                artista[campo] = valor_limpio

    print(
        f"artistas.csv -> {correcciones} textos corregidos"
    )

    return artistas



def limpiar_programa(horarios):

    correcciones = 0

    for horario in horarios:

        campos = [
            "artista",
            "escenario"
        ]

        for campo in campos:

            if campo in horario:

                valor_original = horario[campo]

                valor_limpio = normalizar_texto(
                    valor_original
                )

                if valor_original != valor_limpio:
                    correcciones += 1

                horario[campo] = valor_limpio

    print(
        f"escenarios_horarios.xlsx -> "
        f"{correcciones} textos corregidos"
    )

    return horarios

def limpiar_ventas(ventas):

    correcciones = 0

    for venta in ventas:

        campos = [
            "comprador",
            "tipo_entrada",
            "metodo_pago"
        ]

        for campo in campos:

            if campo in venta:

                valor_original = venta[campo]

                valor_limpio = normalizar_texto(
                    valor_original
                )

                if valor_original != valor_limpio:
                    correcciones += 1

                venta[campo] = valor_limpio

    print(
        f"ventas_entradas.json -> "
        f"{correcciones} textos corregidos"
    )

    return ventas



def limpiar_patrocinadores(patrocinadores):

    correcciones = 0

    for patrocinador in patrocinadores:

        campos = [
            "nombre_empresa",
            "contacto",
            "categoria"
        ]

        for campo in campos:

            if campo in patrocinador:

                valor_original = patrocinador[campo]

                valor_limpio = normalizar_texto(
                    valor_original
                )

                if valor_original != valor_limpio:
                    correcciones += 1

                patrocinador[campo] = valor_limpio

    print(
        f"patrocinadores.xml -> "
        f"{correcciones} textos corregidos"
    )

    return patrocinadores


# def limpiar_id(id):
#     if not id:
#         return 'vacio'
#     id = str(id).strip()
#     id = id.lower()
#     return id




# def limpiar_eur(valor):
#     if not valor:
#         return 'vacio'
#     valor = str(valor).replace('€', '').strip()
#     valor = valor.replace('$', '')
#     valor = valor.replace(',', '.')
#     valor = round(float(valor), 2)
#     return valor


# def limpiar_fecha(valor): # falta unificar formato
#     if not valor:
#         return 'vacio'
#     valor = valor.strip()
#     valor= valor.replace('-','/')
#     valor = valor[2/2/4]
#     return valor

# def limpiar_hora(valor): # fallo despues de la hora pone none
#     if not valor:
#         return 'vacio'
#     valor = str(valor).strip().upper()
#     valor = valor.replace('.', ':').replace('PM', '').replace('AM', '')
#     valor = valor.strip()
#     return valor



# def limpiar_soundcheck(valor):
#     if not valor:
#         return 'vacio'
#     valor = str(valor).strip()
#     valor = valor.replace('PM', '').replace(':', '')
#     valor = valor.replace('.', '').replace('AM', '')
#     return valor


# def limpiar_dni(dni):
#     if dni == dni.zfill(9).upper():
#         return dni
#     elif dni != dni.zfill(9):
#         print('dni erroneo')
#     elif dni == 'N/A':
#         print('vacio')
    

# def procesar_artistas(lista,nombre):
#     lista_limpia = []
#     for item in lista:
#         item_limpio = {
#             'id_artista': limpiar_id(item.get('id_artista')),
#             'nombre': limpiar_texto(item.get('nombre')),
#             'genero_musical': limpiar_texto(item.get('genero_musical')),
#             'pais': limpiar_texto(item.get('pais')),
#             'cache_eur': limpiar_eur(item.get('cache_eur')),
#             'email_manager': limpiar_texto(item.get('email_manager')),
#             'telefono': limpiar_texto(item.get('telefono'))
#         }
#         lista_limpia.append(item_limpio)
#     return lista_limpia

# def procesar_programa(lista,nombre):
#     lista_limpia = []
#     for item in lista:
#         item_limpio = {
#             'fecha': limpiar_fecha(item.get('fecha')),
#             'escenario': limpiar_texto(item.get('escenario')),
#             'artista': limpiar_texto(item.get('artista')),
#             'hora_inicio': limpiar_hora(item.get('hora_inicio')),
#             'hora_fin': limpiar_hora(item.get('hora_fin')),
#             'soundcheck': limpiar_soundcheck(item.get('soundcheck')),
#             'notas': limpiar_texto(item.get('notas'))
#         }
#         lista_limpia.append(item_limpio)
#     return lista_limpia

# def procesar_ventas(lista,nombre):
#     lista_limpia = []
#     for item in lista:
#         item_limpio = {
#             'id_venta': limpiar_id(item.get('id_venta')),
#             'nombre_comprador': limpiar_texto(item.get('nombre_comprador')),
#             'email': limpiar_texto(item.get('email')),
#             'dni': limpiar_dni(item.get('dni')),
#             'tipo_entrada': limpiar_texto(item.get('tipo_entrada')),
#             'precio': limpiar_eur(item.get('precio')),
#             'fecha_compra': limpiar_fecha(item.get('fecha_compra')),
#             'metodo_pago': limpiar_texto(item.get('metodo_pago'))
#         }
#         lista_limpia.append(item_limpio)
#     print(lista_limpia)


# def procesar_patrocinadores(lista,nombre):
#     lista_limpia = []
#     for item in lista:
#         item_limpio = {
#             'nombre_empresa': limpiar_texto(item('nombre_empresa')),
#             'contacto': limpiar_texto(item('contacto')),
#             'email': limpiar_texto(item('email')),
#             'importe_patrocinio': limpiar_eur(item('importe_patrocinio')),
#             'categoria': limpiar_texto(item('categoria')),
#             'fecha_inicio': limpiar_fecha(item('fecha_inicio')),
#             'fecha_fin': limpiar_fecha(item('fecha_fin'))
#         }
#         lista_limpia.append(item_limpio)
#     print(lista_limpia)





