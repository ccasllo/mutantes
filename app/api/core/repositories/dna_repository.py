from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import config.environment as env 
from app.api.core.providers.aws import AWSProvider


class DNARepository:
    def __init__(self):
        self.client = MongoClient(env.MONGO_URI)
        db_name = self.client.get_database().name
        self.collection = self.client[db_name][env.MONGO_COLLECTION]
        self.collection.create_index([("dna", 1)], unique=True)

    def save_person(self, document: dict) -> bool:
        aws_provider = AWSProvider()
        try:
            aws_provider.enviar_evento_eventbridge(document["dna"], document["is_mutant"])
            return 200
        except Exception as e:
            print(f"Error al enviar el evento a EventBridge {e}")
            raise Exception(e)

    def get_stats(self) -> dict:
        count_mutant = self.collection.count_documents({"is_mutant": True})
        count_human = self.collection.count_documents({"is_mutant": False})
        ratio = count_mutant / max(1, count_human)
        return {
            "count_mutant_dna": count_mutant,
            "count_human_dna": count_human,
            "ratio": ratio
        }
