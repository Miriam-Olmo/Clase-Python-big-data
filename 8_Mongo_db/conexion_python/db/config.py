from pymongo import MongoClient
from dotenv import load_dotenv
import os

# cargamos las variables de entorno
load_dotenv()

# extraemos la variable del fichero .env usando la libreria os
mongo_uri = os.getenv('mongo_uri', 'mongodb://localHost:27017')
db_name = os.getenv('mongo_db_name', 'sismosdb')
collection_name = os.getenv('mongo_collection_name', 'sismos')