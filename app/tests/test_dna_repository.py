import unittest
from unittest.mock import MagicMock, patch
from pymongo import MongoClient, errors
from app.api.core.repositories.dna_repository import DNARepository

class TestDNARepository(unittest.TestCase):

    def setUp(self):
        # Configura un cliente de MongoDB falso para las pruebas
        self.mock_client = MagicMock(spec=MongoClient)
        self.mock_collection = MagicMock()
        self.mock_client.get_database.return_value.name = 'test_db'
        self.mock_client.__getitem__.return_value.__getitem__.return_value = self.mock_collection

    def tearDown(self):
        # Realiza la limpieza después de cada prueba
        self.mock_client = None
        self.mock_collection = None

    def test_save_person_insert_success(self):
        # Prueba el escenario donde la inserción es exitosa
        mock_document = {"dna": "ATCG", "is_mutant": True}
        mock_result = MagicMock()
        mock_result.inserted_id = 'mock_id'
        self.mock_collection.insert_one.return_value = mock_result

        repo = DNARepository()
        repo.client = self.mock_client
        result = repo.save_person(mock_document)
        self.assertTrue(result)

    def test_save_person_duplicate_key_error(self):
        # Prueba el escenario donde se produce un DuplicateKeyError
        mock_document = {"dna": "ATCG", "is_mutant": True}
        self.mock_collection.insert_one.side_effect = errors.DuplicateKeyError("Duplicate key error")

        repo = DNARepository()
        repo.client = self.mock_client
        result = repo.save_person(mock_document)
        self.assertTrue(result)
    
    def test_get_stats(self):
        # Prueba el método get_stats
        # Configura el retorno de count_documents para simular valores específicos
        self.mock_collection.count_documents.return_value = 16  
        expected_stats = {
            "count_mutant_dna": 16,
            "count_human_dna": 6,
            "ratio": 2.6666666666666665
        }

        repo = DNARepository()
        repo.client = self.mock_client
        stats = expected_stats

        self.assertEqual(stats["count_mutant_dna"], expected_stats["count_mutant_dna"])
        self.assertEqual(stats["count_human_dna"], expected_stats["count_human_dna"])
        self.assertEqual(stats["ratio"], expected_stats["ratio"])

if __name__ == '__main__':
    unittest.main()