def limpiar_id(id):
    # si no hay id:
    if not id:
        return None
    id = str(id).strip()
    return int(id)



def limpiar_texto(valor, mayusculas = False):
    if not valor:
        return 'sin datos'
    valor = str(valor).strip()
    return valor.upper( ) if mayusculas else valor.lower()

