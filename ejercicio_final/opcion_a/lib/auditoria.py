valores_vacios = [

    '',
    None,
    'N/A',
    '-',
    'no disponible'
]


# ====================================
# FUNCIONES GENERALES
# ====================================

def obtener_valor(
    registro,
    campo
):

    return registro.get(campo)


def convertir_texto(valor):

    return str(valor)


def convertir_minusculas(texto):

    return texto.lower()


def quitar_espacios_laterales(
    texto
):

    return texto.strip()


def normalizar_clave(valor):

    valor = convertir_texto(
        valor
    )

    valor = convertir_minusculas(
        valor
    )

    valor = quitar_espacios_laterales(
        valor
    )

    return valor


def es_texto(valor):

    return isinstance(valor, str)


# ====================================
# VALORES VACÍOS
# ====================================

def esta_vacio(valor):

    return valor in valores_vacios


def contar_vacios_campo(
    datos,
    campo
):

    contador = 0

    for registro in datos:

        valor = obtener_valor(
            registro,
            campo
        )

        if esta_vacio(valor):

            contador += 1

    return contador


def contar_valores_vacios(datos):

    resultado = {}

    for campo in datos[0]:

        cantidad = contar_vacios_campo(
            datos,
            campo
        )

        resultado[campo] = cantidad

    return resultado


# ====================================
# DUPLICADOS
# ====================================

def existe_en_vistos(
    valor,
    vistos
):

    return valor in vistos


def guardar_en_vistos(
    valor,
    vistos
):

    vistos.add(valor)


# ----------------------------
# DUPLICADOS EXACTOS
# ----------------------------

def detectar_duplicados_exactos(
    datos,
    campo
):

    vistos = set()

    duplicados = 0

    for registro in datos:

        valor = obtener_valor(
            registro,
            campo
        )

        if existe_en_vistos(
            valor,
            vistos
        ):

            duplicados += 1

        else:

            guardar_en_vistos(
                valor,
                vistos
            )

    return duplicados


# ----------------------------
# DUPLICADOS PARCIALES
# ----------------------------

def detectar_duplicados_parciales(
    datos,
    campo
):

    vistos = set()

    duplicados = 0

    for registro in datos:

        valor = obtener_valor(
            registro,
            campo
        )

        valor = normalizar_clave(
            valor
        )

        if existe_en_vistos(
            valor,
            vistos
        ):

            duplicados += 1

        else:

            guardar_en_vistos(
                valor,
                vistos
            )

    return duplicados


# ====================================
# FORMATOS INCONSISTENTES
# ====================================

def crear_set():

    return set()


def agregar_variacion(
    variaciones,
    valor
):

    variaciones.add(valor)


def obtener_variaciones(
    datos,
    campo
):

    variaciones = crear_set()

    for registro in datos:

        valor = obtener_valor(
            registro,
            campo
        )

        if valor:

            valor = normalizar_clave(
                valor
            )

            agregar_variacion(
                variaciones,
                valor
            )

    return variaciones


def contar_formatos_inconsistentes(
    datos
):

    resultado = {}

    for campo in datos[0]:

        variaciones = obtener_variaciones(
            datos,
            campo
        )

        resultado[campo] = list(
            variaciones
        )

    return resultado


# ====================================
# FUERA DE RANGO
# ====================================

def convertir_float(valor):

    return float(valor)


def esta_fuera_de_rango(
    valor,
    minimo,
    maximo
):

    return valor < minimo or valor > maximo


def contar_fuera_rango(
    datos,
    campo,
    minimo,
    maximo
):

    contador = 0

    for registro in datos:

        valor = obtener_valor(
            registro,
            campo
        )

        try:

            valor = convertir_float(
                valor
            )

            if esta_fuera_de_rango(
                valor,
                minimo,
                maximo
            ):

                contador += 1

        except:

            pass

    return contador


# ====================================
# ESPACIOS EXTRA
# ====================================

def tiene_espacios_laterales(
    texto
):

    return texto != texto.strip()


def tiene_espacios_dobles(
    texto
):

    return '  ' in texto


def tiene_espacios_extra(texto):

    if not es_texto(texto):

        return False

    if tiene_espacios_laterales(
        texto
    ):

        return True

    if tiene_espacios_dobles(
        texto
    ):

        return True

    return False


def contar_espacios_extra(
    datos,
    campo
):

    contador = 0

    for registro in datos:

        valor = obtener_valor(
            registro,
            campo
        )

        if tiene_espacios_extra(
            valor
        ):

            contador += 1

    return contador


# ====================================
# CREAR AUDITORÍA
# ====================================

def crear_auditoria_fichero():

    return {

        'total_registros': 0,

        'valores_vacios': {},

        'duplicados': 0,

        'formatos_inconsistentes': {},

        'fuera_de_rango': {},

        'espacios_extra': {}
    }


def contar_registros(datos):

    return len(datos)


# ====================================
# AUDITORÍA COMPLETA
# ====================================

def generar_auditoria(
    nombre_fichero,
    datos,
    campo_duplicados,
    rangos={}
):

    auditoria = (
        crear_auditoria_fichero()
    )

    # -------------------------
    # TOTAL REGISTROS
    # -------------------------

    auditoria[
        'total_registros'
    ] = contar_registros(
        datos
    )

    # -------------------------
    # VACÍOS
    # -------------------------

    auditoria[
        'valores_vacios'
    ] = contar_valores_vacios(
        datos
    )

    # -------------------------
    # DUPLICADOS
    # -------------------------

    auditoria[
        'duplicados'
    ] = (
        detectar_duplicados_parciales(
            datos,
            campo_duplicados
        )
    )

    # -------------------------
    # FORMATOS
    # -------------------------

    auditoria[
        'formatos_inconsistentes'
    ] = (
        contar_formatos_inconsistentes(
            datos
        )
    )

    # -------------------------
    # FUERA DE RANGO
    # -------------------------

    fuera_rango = {}

    for campo, rango in rangos.items():

        minimo = rango[0]

        maximo = rango[1]

        cantidad = contar_fuera_rango(
            datos,
            campo,
            minimo,
            maximo
        )

        fuera_rango[campo] = cantidad

    auditoria[
        'fuera_de_rango'
    ] = fuera_rango

    # -------------------------
    # ESPACIOS EXTRA
    # -------------------------

    espacios = {}

    for campo in datos[0]:

        cantidad = contar_espacios_extra(
            datos,
            campo
        )

        espacios[campo] = cantidad

    auditoria[
        'espacios_extra'
    ] = espacios

    return auditoria


# ====================================
# INFORMES
# ====================================

def imprimir_titulo(nombre):

    print(
        '\n=== AUDITORÍA:',
        nombre,
        '==='
    )


def imprimir_total(total):

    print(
        'Total registros:',
        total
    )


def imprimir_valores_vacios(
    valores
):

    print('\nValores vacíos:')

    for campo, cantidad in valores.items():

        print(
            ' -',
            campo + ':',
            cantidad,
            'vacíos'
        )


def imprimir_duplicados(
    cantidad
):

    print(
        '\nDuplicados:',
        cantidad,
        'registros duplicados'
    )


def imprimir_formatos(
    formatos
):

    print(
        '\nFormatos inconsistentes:'
    )

    for campo, variaciones in formatos.items():

        print(
            ' -',
            campo + ':',
            len(variaciones),
            'variaciones'
        )

        print(
            '   ',
            variaciones
        )


def imprimir_fuera_rango(
    fuera_rango
):

    print('\nFuera de rango:')

    for campo, cantidad in fuera_rango.items():

        print(
            ' -',
            campo + ':',
            cantidad
        )


def imprimir_espacios_extra(
    espacios
):

    print('\nEspacios extra:')

    for campo, cantidad in espacios.items():

        print(
            ' -',
            campo + ':',
            cantidad,
            'campos con espacios extra'
        )


def imprimir_informe(
    nombre_fichero,
    auditoria
):

    imprimir_titulo(
        nombre_fichero
    )

    imprimir_total(
        auditoria[
            'total_registros'
        ]
    )

    imprimir_valores_vacios(
        auditoria[
            'valores_vacios'
        ]
    )

    imprimir_duplicados(
        auditoria[
            'duplicados'
        ]
    )

    imprimir_formatos(
        auditoria[
            'formatos_inconsistentes'
        ]
    )

    imprimir_fuera_rango(
        auditoria[
            'fuera_de_rango'
        ]
    )

    imprimir_espacios_extra(
        auditoria[
            'espacios_extra'
        ]
    )