regclas_artistas = {

    'nombre': {

        'tipo': 'texto',

        'vacio': 'SIN DATOS'
    },

    'pais': {

        'tipo': 'texto',

        'vacio': 'SIN DATOS'
    },

    'genero_musical': {

        'tipo': 'texto',

        'vacio': 'SIN DATOS'
    },

    'cache_eur': {

        'tipo': 'float',

        'vacio': 0
    },

    'email_manager': {

        'tipo': 'texto',

        'vacio': 'SIN DATOS'
    }
}


# ====================================
# VALORES VACÍOS
# ====================================

valores_vacios = [

    '',
    None,
    'N/A',
    '-',
    'no disponible'
]


# ====================================
# CORRECCIONES DE TILDES
# ====================================

correcciones_tildes = {

    "jose":       "José",
    "maria":      "María",
    "garcia":     "García",
    "gonzalez":   "González",
    "martinez":   "Martínez",
    "lopez":      "López",
    "perez":      "Pérez",
    "sanchez":    "Sánchez",
    "gomez":      "Gómez",
    "fernandez":  "Fernández",
    "rodriguez":  "Rodríguez",
    "hernandez":  "Hernández",
    "ramirez":    "Ramírez",
    "gutierrez":  "Gutiérrez",
}


# ====================================
# FUNCIONES GENERALES
# ====================================

def convertir_texto(valor):

    return str(valor)


def quitar_espacios_laterales(
    texto
):

    return texto.strip()


def obtener_valor(
    registro,
    campo
):

    return registro.get(campo)


def es_texto(valor):
    # para preguntar si es de x tipo
    return isinstance(valor, str)


# ====================================
# LIMPIEZA DE TEXTO
# ====================================

def separar_palabras(texto):

    return texto.split()


def unir_palabras(lista):

    return ' '.join(lista)


def quitar_espacios_multiples(
    texto
):

    palabras = separar_palabras(
        texto
    )

    return unir_palabras(
        palabras
    )


def limpiar_texto(texto):

    if texto is None:

        return ''

    texto = convertir_texto(
        texto
    )

    texto = quitar_espacios_laterales(
        texto
    )

    texto = quitar_espacios_multiples(
        texto
    )

    return texto


# ====================================
# NORMALIZAR TEXTO
# ====================================

def convertir_minusculas(texto):

    return texto.lower()


def convertir_titulo(texto):

    return texto.title()


def palabra_tiene_tilde(
    palabra
):

    palabra = convertir_minusculas(
        palabra
    )

    return palabra in correcciones_tildes


def obtener_palabra_corregida(
    palabra
):

    palabra = convertir_minusculas(
        palabra
    )

    return correcciones_tildes[
        palabra
    ]


def corregir_palabra(palabra):

    if palabra_tiene_tilde(
        palabra
    ):

        return obtener_palabra_corregida(
            palabra
        )

    return palabra


def corregir_tildes(texto):

    palabras = separar_palabras(
        texto
    )

    nuevas = []

    for palabra in palabras:

        nueva = corregir_palabra(
            palabra
        )

        nuevas.append(nueva)

    return unir_palabras(
        nuevas
    )


def normalizar_texto(texto):

    texto = limpiar_texto(
        texto
    )

    texto = convertir_titulo(
        texto
    )

    texto = corregir_tildes(
        texto
    )

    return texto


# ====================================
# LIMPIEZA NUMERO
# ====================================

def eliminar_simbolo(
    valor,
    simbolo
):

    return valor.replace(
        simbolo,
        ''
    )


def eliminar_puntos_miles(
    valor
):

    return valor.replace(
        '.',
        ''
    )


def cambiar_coma_decimal(
    valor
):

    return valor.replace(
        ',',
        '.'
    )


def limpiar_moneda(valor):

    valor = eliminar_simbolo(
        valor,
        '€'
    )

    valor = eliminar_simbolo(
        valor,
        '$'
    )

    return valor


def normalizar_numero(valor):

    valor = eliminar_puntos_miles(
        valor
    )

    valor = cambiar_coma_decimal(
        valor
    )

    return valor


def convertir_float(valor):

    return float(valor)


def es_entero(numero):

    return numero.is_integer()


def convertir_int(numero):

    return int(numero)


def limpiar_valor_numero(valor):

    if valor is None:

        return None

    valor = convertir_texto(
        valor
    )

    valor = quitar_espacios_laterales(
        valor
    )

    valor = limpiar_moneda(
        valor
    )

    valor = normalizar_numero(
        valor
    )

    try:

        numero = convertir_float(
            valor
        )

        if es_entero(numero):

            return convertir_int(
                numero
            )

        return numero

    except:

        return None


# ====================================
# TRATAMIENTO DE VACÍOS
# ====================================

def esta_vacio(valor):

    return valor in valores_vacios


def obtener_regla_vacio(
    reglas,
    campo
):

    return reglas[campo]['vacio']


def reemplazar_vacio(
    registro,
    campo,
    valor
):

    registro[campo] = valor


def tratar_vacio(
    registro,
    campo,
    reglas
):

    valor = obtener_valor(
        registro,
        campo
    )

    if esta_vacio(valor):

        nuevo = obtener_regla_vacio(
            reglas,
            campo
        )

        reemplazar_vacio(
            registro,
            campo,
            nuevo
        )

        return True

    return False


# ====================================
# CONVERSIÓN DE TIPOS
# ====================================

def obtener_tipo_campo(
    reglas,
    campo
):

    return reglas[campo]['tipo']


def es_campo_numerico(tipo):

    return tipo in [
        'int',
        'float'
    ]


def convertir_campo_numerico(
    registro,
    campo
):

    valor = obtener_valor(
        registro,
        campo
    )

    nuevo = limpiar_valor_numero(
        valor
    )

    registro[campo] = nuevo

    return nuevo != valor


def aplicar_conversion_tipos(
    datos,
    reglas
):

    resumen = {}

    for campo in reglas:

        resumen[campo] = 0

    for registro in datos:

        for campo in reglas:

            tipo = obtener_tipo_campo(
                reglas,
                campo
            )

            if es_campo_numerico(
                tipo
            ):

                convertido = (
                    convertir_campo_numerico(
                        registro,
                        campo
                    )
                )

                if convertido:

                    resumen[campo] += 1

    return resumen


# ====================================
# APLICAR VACÍOS
# ====================================

def aplicar_tratamiento_vacios(
    datos,
    reglas
):

    resumen = {}

    for campo in reglas:

        resumen[campo] = 0

    for registro in datos:

        for campo in reglas:

            cambiado = tratar_vacio(
                registro,
                campo,
                reglas
            )

            if cambiado:

                resumen[campo] += 1

    return resumen


# ====================================
# LIMPIAR TEXTOS
# ====================================

def limpiar_campo_texto(
    registro,
    campo
):

    valor = obtener_valor(
        registro,
        campo
    )

    if es_texto(valor):

        nuevo = normalizar_texto(
            valor
        )

        registro[campo] = nuevo

        return nuevo != valor

    return False


def aplicar_limpieza_texto(
    datos
):

    resumen = {}

    for campo in datos[0]:

        resumen[campo] = 0

    for registro in datos:

        for campo in registro:

            cambiado = limpiar_campo_texto(
                registro,
                campo
            )

            if cambiado:

                resumen[campo] += 1

    return resumen


# ====================================
# INFORMES
# ====================================

def imprimir_conversiones(
    nombre_fichero,
    resumen
):

    print(
        '\n=== CONVERSIONES:',
        nombre_fichero,
        '==='
    )

    for campo, cantidad in resumen.items():

        if cantidad > 0:

            print(
                nombre_fichero,
                '>',
                campo + ':',
                cantidad,
                'valores convertidos a número'
            )


def imprimir_vacios(
    nombre_fichero,
    resumen,
    reglas
):

    print(
        '\n=== VACÍOS:',
        nombre_fichero,
        '==='
    )

    for campo, cantidad in resumen.items():

        if cantidad > 0:

            valor = obtener_regla_vacio(
                reglas,
                campo
            )

            print(
                nombre_fichero,
                '>',
                campo + ':',
                cantidad,
                "vacíos → marcados como",
                repr(valor)
            )


def imprimir_correcciones(
    nombre_fichero,
    resumen
):

    print(
        '\n=== CORRECCIONES:',
        nombre_fichero,
        '==='
    )

    for campo, cantidad in resumen.items():

        if cantidad > 0:

            print(
                nombre_fichero,
                '>',
                campo + ':',
                cantidad,
                'textos corregidos'
            )