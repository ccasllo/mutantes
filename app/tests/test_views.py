import unittest
import asyncio
from fastapi import HTTPException
from unittest.mock import MagicMock, patch
from app.api.core.models import DNAVerificationModel
from app.api.core.helper import isMutant
from app.api.core.repositories.dna_repository import DNARepository
from app.api.core.views import detect_mutant, get_stats

class TestMutantAPI(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    def test_detect_mutant_mutant_detected(self):
        # Prueba el escenario donde se detecta un mutante
        mock_dna = DNAVerificationModel(dna=["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"])
        mock_repository = MagicMock(spec=DNARepository)
        mock_repository.save_person.return_value = True
        with patch('app.api.core.views.DNARepository', return_value=mock_repository):
            async def run_test():
                response = await detect_mutant(mock_dna)
                self.assertEqual(response.status_code, 200)
            self.loop.run_until_complete(run_test())


    def test_detect_mutant_human_detected(self):
        # Prueba el escenario donde se detecta un humano
        mock_dna = DNAVerificationModel(dna=["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"])
        mock_repository = MagicMock(spec=DNARepository)
        mock_repository.save_person.return_value = True
        with patch('app.api.core.views.DNARepository', return_value=mock_repository):
            async def run_test():
                try:
                    await detect_mutant(mock_dna)
                except HTTPException as exc:
                    self.assertEqual(exc.status_code, 403)
                else:  
                    self.assertEqual(1,2)
            self.loop.run_until_complete(run_test())

    def test_detect_mutant_internal_server_error(self):
        # Prueba el escenario donde ocurre un error interno en el servidor
        mock_dna = DNAVerificationModel(dna=["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"])
        mock_repository = MagicMock(spec=DNARepository)
        mock_repository.save_person.return_value = False
        with patch('app.api.core.views.DNARepository', return_value=mock_repository):
            async def run_test():
                with self.assertRaises(HTTPException) as cm:
                    await detect_mutant(mock_dna)
                self.assertEqual(cm.exception.status_code, 500)
            self.loop.run_until_complete(run_test())

    def test_get_stats(self):
        # Prueba la función get_stats de manera asíncrona
        mock_repository = MagicMock()
        mock_repository.get_stats.return_value = {"count_mutant_dna": 40, "count_human_dna": 100, "ratio": 0.4}

        async def async_get_stats():
            return await get_stats()

        with patch('app.api.core.views.DNARepository', return_value=mock_repository):
            # Ejecuta la función asíncrona y espera su resolución
            loop = asyncio.get_event_loop()
            response = loop.run_until_complete(async_get_stats())

            # Realiza la comparación con los valores esperados del diccionario
            expected_response = {"count_mutant_dna": 40, "count_human_dna": 100, "ratio": 0.4}
            self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
