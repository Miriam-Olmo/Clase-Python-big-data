import csv

lista_de_juegos = list('./data/game.csv')

def filtrar_stock(lista_de_juegos):
    print("--- Juegos con stock disponible ---")
    for juego in lista_de_juegos:
        if juego["en_stock"] > 0:
            print(f"Disponible: {juego['titulo']}")
filtrar_stock(lista_de_juegos)


# def crear_archivo_rebajas():
#     pass

# crear_archivo_rebajas()

# def juego_caro():
#     pass
# juego_caro()


# def juego_barato():
#     pass
# juego_barato()
