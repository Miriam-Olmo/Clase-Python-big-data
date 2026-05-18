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
# 'precio': limpiar_precio(item['precio']),
# 'stock': limpiar_stock(item['stock'])
def  limpiar_precio(precio):
    precio = float(precio)
    if precio == 'gratis':
        return 0.0
    elif precio != 'gratis':
        return precio
    else:
        print('no hay precio registrado')
    return precio

def limpiar_stock(stock):
    stock = int(stock)
    if stock == '-' or 'N/A':
        return 0