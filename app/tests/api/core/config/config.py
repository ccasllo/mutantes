import os


def valida_mongo_uri(mongo_uri):
    URL_CON = mongo_uri
    if not mongo_uri.endswith('/'):
        URL_CON = os.getenv('MONGO_URI', '')+'/'
    return URL_CON


MONGO_DB = os.getenv('MONGO_DB', 'mutantes_db')
MONGO_URI = valida_mongo_uri(os.getenv('MONGO_URI'))+MONGO_DB+'?retryWrites=true&w=majority'
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'mutantes')
ENTORNO = os.getenv('ENTORNO', 'DEV')
