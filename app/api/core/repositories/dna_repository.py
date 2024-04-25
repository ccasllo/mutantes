from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from app.api.core.config import MONGO_COLLECTION, MONGO_URI, ENTORNO
from app.api.core.event_bridge import enviar_evento_eventbridge


class DNARepository:
    def __init__(self,
                 mongo_uri: str = MONGO_URI,
                 collection_name: str = MONGO_COLLECTION):
        self.client = MongoClient(mongo_uri)
        db_name = self.client.get_database().name
        self.collection = self.client[db_name][collection_name]
        self.collection.create_index([("dna", 1)], unique=True)

    def save_person(self, document: dict) -> bool:
        if ENTORNO != "PRODUCTION":
            try:
                result = self.collection.insert_one(document)
                return result.inserted_id is not None
            except DuplicateKeyError:
                return 200
        else:
            enviar_evento_eventbridge(document["dna"],document["is_mutant"])
            return 200

    def get_stats(self) -> dict:
        count_mutant = self.collection.count_documents({"is_mutant": True})
        count_human = self.collection.count_documents({"is_mutant": False})
        ratio = count_mutant / max(1, count_human)
        return {
            "count_mutant_dna": count_mutant,
            "count_human_dna": count_human,
            "ratio": ratio
        }
