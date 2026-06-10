import mysql.connector
from mysql.connector import Error

# configurar nuestra conexion

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'V4ll3c4n@93',
    'database': 'tinta_eterna'
}

def get_connection():
    try:
        return mysql.connector.connect(**db_config)
    except Error as E:
        print(f'Error: {E}')
        return None
    

# # obtener listado con todos los libros

# def get_all_books():
#     try:
#         # lo primero sera conectarse a la base
#         conection = get_connection()
#         # hacer consulta
#         cursor = conection.cursor(dictionary=True)
#         cursor.execute('select * from libros')
#         return cursor.fetchall()
#     except Error as E:
#         print(f'Error: {E}')
#         return []
#     finally:
#         conection.close()

# libros = get_all_books()
# print(libros)


# voy a hacer una peticion de un libro por id
def get_book_by_id(id_libro):
    try:
        conection = get_connection()
        cursor = conection.cursor(dictionary=True)
        cursor.execute(f'select * from libros where id=%s', (id_libro,))
        return cursor.fetchone()
    except Error as E:
        print(f'Error: {E}')
        return None
    finally:
        conection.close()

libro_1 = get_book_by_id(12)
print(libro_1)