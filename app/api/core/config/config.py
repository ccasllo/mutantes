import os

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mutantes')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'mutantes')