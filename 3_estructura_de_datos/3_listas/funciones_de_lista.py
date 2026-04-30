nombres = 'Juan', 'Mario', 'Pablo', 'Paula', 'Miriam'

# agregar un unico elemento por el final
nombres.append('Joaquin')
print('append', nombres)

# agregar varios elementos a la vez en una lista por el final
nombres.extend(['Miguel Angel', 'reniel'])
print('extend', nombres)

# agregar un elemento en cualquier posicion
nombres.insert(1, 'Luis')
print('insert', nombres)

# borrar un elemento de la lista
# metodo pringle ( POP() )
# elimina las cosas por el final

ultimo_elemento = nombres.pop()
print(nombres)
print(ultimo_elemento)

elemento_tres = nombres.pop(3)
print(elemento_tres)

# eliminar elementos de la lista por contenido
nombres.remove('Mario')
print(nombres)