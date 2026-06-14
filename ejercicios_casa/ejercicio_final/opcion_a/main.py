# exportamos a main para la carga de funciones y archivos
from lib.carga import cargar_csv, cargar_json, cargar_xml, cargar_excel

artistas = cargar_csv('./datos/artistas.csv')
# escenarios = cargar_excel('./datos/escenarios_horarios.xlsx')
# patrocinadores = cargar_xml('./datos/patrocinadores.xml')
# ventas = cargar_json('./datos/ventas_entradas.json')

print(artistas)