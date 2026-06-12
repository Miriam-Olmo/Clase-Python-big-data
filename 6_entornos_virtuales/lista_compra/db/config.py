# servira para crear la  conexion a base de datos
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# crear el diccionario de conexion a base de datos

load_dotenv()

db_config = {
    'host': os.getenv("MYSQL_LOCALHOST"),
    'port': int(os.getenv("MYSQL_PORT")),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE")
}

def get_connection():
    try:
        return mysql.connector.connect(**db_config)
    except Error as e:
        print(f"Error: {e}")
        return None
    

def get_compra():
    try:
        # crear la conexion
        conn = get_connection()
        # abrimos el sql file para hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select * from productos')
        return cursor.fetchall()
    except Error as e:
        print(f'Error: {e}')
    finally:
        conn.close()


resultado = get_compra()
print(resultado)