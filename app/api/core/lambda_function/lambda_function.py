import pymongo
import json
import os

def valida_mongo_uri(mongo_uri):
    URL_CON = mongo_uri
    if not mongo_uri.endswith('/'):
        URL_CON = os.getenv('MONGO_URI', '')+'/'
    return URL_CON


MONGO_DB = os.getenv('MONGO_DB', 'mutantes_db')
MONGO_URI = valida_mongo_uri(os.getenv('MONGO_URI'))+MONGO_DB+'?retryWrites=true&w=majority'
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'mutantes')


def lambda_handler(event, context):
    # Extraer datos del evento
    detalle = event['detail']
    dna = json.loads(detalle['dna'])
    is_mutant = detalle['is_mutant']

    client = pymongo.MongoClient(MONGO_URI)
    db = client.get_database()
    collection = db[MONGO_COLLECTION]  

    # Crear un documento para insertar en la colección
    documento = {
        "dna": dna,
        "is_mutant": is_mutant
    }

    # Insertar el documento en la colección
    try:
        result = collection.insert_one(documento)
        return {
            'statusCode': 200,
            'body': json.dumps(f"Documento insertado correctamente con ID: {result.inserted_id}")
        }
    except pymongo.errors.DuplicateKeyError:
        return {
            'statusCode': 200,
            'body': json.dumps("El documento ya existe en la base de datos")
        }


if __name__ == '__main__':
    event = {
        "detail": {
            "dna": '["ATGCGA","CCGTTC","TTATGT","AGAAGG","CCCCTA","TCACTG"]',
            "is_mutant": True
        }
    }
    print(lambda_handler(event, None))