def añadir_producto(nombre, cantidad):
    # Abrimos el archivo en modo 'a' (append) para añadir al final sin borrar lo anterior
    fichero = open(f"./data/lista_compra.txt", 'a', encoding='UTF-8')
    fichero.write(f"{nombre} => {cantidad} \n")
    fichero.close()
    print("¡Guardado!")



def ver_lista(lista_compra):
    print("\n--- COSAS POR COMPRAR ---")
    # Usamos try/except por si el archivo no existe todavía (así no da error)
    try:
        fichero = open(f'./data/lista_compra.txt', "r", encoding='UTF-8')
        print(fichero.readlines())
        fichero.close()
    except:
        print("La lista está vacía o no existe")
