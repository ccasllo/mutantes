import unittest
from app.api.core.helper import isMutant


class TestIsMutant(unittest.TestCase):
    def test_horizontal_sequence(self):
        # Prueba una secuencia horizontal válida
        dna = [
            "ATGCGA",
            "CAGTTC",
            "TTCTGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"]
        self.assertTrue(isMutant(dna))

    def test_vertical_sequence(self):
        # Prueba una secuencia vertical válida
        dna = [
            "ACTGGA",
            "ACTGAT",
            "ACTGGT",
            "ACTGCA"
        ]
        self.assertTrue(isMutant(dna))

    def test_diagonal_sequence(self):
        # Prueba una secuencia diagonal (\) válida
        dna = [
            "ACTGGA",
            "TACTAT",
            "GTACGT",
            "AGTACA"
        ]
        self.assertTrue(isMutant(dna))

        # Prueba una secuencia diagonal (/) válida
        dna = [
            "GTCAGA",
            "TCATAT",
            "CATGGT",
            "ATGACA"
        ]
        self.assertTrue(isMutant(dna))

    def test_non_mutant_sequence(self):
        # Prueba una secuencia que no es mutante
        dna = [
            "ACTGGA",
            "TGCAAT",
            "GTACGT",
            "GTACGA",
            "CGATCA"
        ]
        self.assertFalse(isMutant(dna))


if __name__ == '__main__':
    unittest.main()
