from pydantic import BaseModel, ValidationError, Field
from typing import List


class DNAVerificationModel(BaseModel):
    dna: List[str]

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

    def __init__(self, dna: List[str]):
        self.validate_dna(dna)
        super().__init__(dna=dna)
