import os
import app.api.core.utils as utils


MONGO_DB = os.getenv('MONGO_DB', 'mutantes_db')
MONGO_URI = utils.valida_mongo_uri(os.getenv('MONGO_URI',''))+MONGO_DB+'?retryWrites=true&w=majority'
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'mutantes')
ENTORNO = os.getenv('ENTORNO', 'DEV')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID'),
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY'),
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')
DEBUG = os.getenv('DEBUG', False)