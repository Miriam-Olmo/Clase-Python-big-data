# ====================================
# IMPORTACIONES
# ====================================

from lib.auditoria import *

from lib.limpieza import *


# ====================================
# DATOS DE EJEMPLO
# ====================================

artistas = [

    {
        'nombre': ' jose  garcia ',
        'pais': ' españa ',
        'genero_musical': 'rokc',
        'cache_eur': '1.500,50€'
    },

    {
        'nombre': 'MARIA LOPEZ',
        'pais': 'francia',
        'genero_musical': 'Rock',
        'cache_eur': '2000€'
    },

    {
        'nombre': '',
        'pais': 'Portugal',
        'genero_musical': 'electro',
        'cache_eur': '750€'
    },

    {
        'nombre': ' jose  garcia ',
        'pais': ' españa ',
        'genero_musical': 'ROCK',
        'cache_eur': '1.500,50€'
    }
]


# ====================================
# AUDITORÍA INICIAL
# ====================================

print('\n====================')
print('AUDITORÍA INICIAL')
print('====================')


vacios = contar_vacios(
    artistas
)

print('\nVALORES VACÍOS')

for campo, cantidad in vacios.items():

    print(
        campo,
        ':',
        cantidad
    )


espacios = detectar_espacios_extra(
    artistas
)

print('\nESPACIOS EXTRA')

for campo, cantidad in espacios.items():

    print(
        campo,
        ':',
        cantidad
    )


duplicados = detectar_duplicados(
    artistas,
    'nombre'
)

print('\nDUPLICADOS')

print(duplicados)


formatos = contar_formatos(
    artistas
)

print('\nFORMATOS')

for campo, cantidad in formatos.items():

    print(
        campo,
        ':',
        cantidad
    )


# ====================================
# LIMPIEZA
# ====================================

print('\n====================')
print('LIMPIEZA')
print('====================')


for registro in artistas:

    # ----------------
    # NOMBRE
    # ----------------

    registro['nombre'] = normalizar_texto(
        registro['nombre']
    )

    # ----------------
    # PAÍS
    # ----------------

    registro['pais'] = normalizar_texto(
        registro['pais']
    )

    # ----------------
    # GÉNERO
    # ----------------

    registro['genero_musical'] = normalizar_categoria(
        registro['genero_musical'],
        mapeo_generos
    )

    # ----------------
    # CACHÉ
    # ----------------

    registro['cache_eur'] = limpiar_valor_numerico(
        registro['cache_eur']
    )


# ====================================
# ELIMINAR DUPLICADOS
# ====================================

artistas = eliminar_duplicados(
    artistas,
    ['nombre']
)


# ====================================
# RESULTADO FINAL
# ====================================

print('\n====================')
print('DATOS LIMPIOS')
print('====================')


for registro in artistas:

    print(registro)