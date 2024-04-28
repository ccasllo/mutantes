from pydantic import BaseModel
from typing import List
import json


class DNAVerificationModel(BaseModel):
    """
    Represents a DNA verification model.

    Attributes:
        dna (List[str]): The DNA sequences to be verified.

    Example:
        {
            "dna": [
                "ATGCGA",
                "CAGTGC",
                "TTATGT",
                "AGAAGG",
                "CCCCTA",
                "TCACTG"
            ]
        }
    """
    dna: List[str]
    
    

    class Config:
        with open("app/api/core/schema/dna_verification.json") as file:
            schema_extra = json.load(file)
    

    @classmethod
    def validate_dna(cls, value):
        allowed_chars = set("ATCG")
        for seq in value:
            if not set(seq).issubset(allowed_chars):
                raise ValueError("La secuencia de ADN solo puede contener los caracteres A, T, C, G.")

        # Validar que todos los elementos de la lista tengan la misma longitud
        n = len(value)
        if any(len(seq) != n for seq in value):
            raise ValueError("Los elementos de la secuencia deben formar una matriz cuadrada (NxN).")

        if n == 0:
            raise ValueError("La secuencia de ADN no puede estar vacía.")

    def __init__(self, dna: List[str]):
        self.validate_dna(dna)
        super().__init__(dna=dna)


class DNAStatsModel(BaseModel):
    """
    Represents a DNA stats model.

    Attributes:
        count_mutant_dna (int): The number of mutant DNA sequences.
        count_human_dna (int): The number of human DNA sequences.
        ratio (float): The ratio of mutant DNA sequences to human DNA sequences.

    Example:
        {
            "count_mutant_dna": 40,
            "count_human_dna": 100,
            "ratio": 0.4
        }
    """
    count_mutant_dna: int
    count_human_dna: int
    ratio: float

    class Config:
        with open("app/api/core/schema/dna_stats.json") as file:
            schema_extra = json.load(file)


