import unittest
from app.api.core.models import DNAVerificationModel


class TestDNAVerificationModel(unittest.TestCase):

    def test_valid_dna(self):
        # Prueba una lista de ADN válida
        valid_dna = ["ATCG", "TACT", "GTAC", "AGTA"]
        model = DNAVerificationModel(dna=valid_dna)
        self.assertEqual(model.dna, valid_dna)

    def test_invalid_chars(self):
        # Prueba una lista de ADN con caracteres inválidos
        invalid_dna = ["ATCG", "TACX", "GTAC", "AGTA"]
        with self.assertRaises(ValueError):
            DNAVerificationModel(dna=invalid_dna)

    def test_invalid_matrix(self):
        # Prueba una lista de ADN con matrices no cuadradas
        invalid_matrix = ["ATCG", "TACTA", "GTAC", "AGTA"]
        with self.assertRaises(ValueError):
            DNAVerificationModel(dna=invalid_matrix)

    def test_empty_list(self):
        # Prueba una lista de ADN vacía
        empty_dna = []
        with self.assertRaises(ValueError):
            DNAVerificationModel(dna=empty_dna)


if __name__ == '__main__':
    unittest.main()
