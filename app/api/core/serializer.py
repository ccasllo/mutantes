from .models import DNAVerificationModel
from typing import List

def serialize_dna_verification(model: DNAVerificationModel) -> dict:
    """
    Serializa un objeto DNAVerificationModel a un diccionario.
    """
    return model.model_dump()
