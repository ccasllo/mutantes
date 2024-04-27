from fastapi import APIRouter, HTTPException, status
from app.api.core.models import DNAVerificationModel
from app.api.core.utils import is_mutant
from app.api.core.repositories.dna_repository import DNARepository
from config.logger import logger

router = APIRouter()

@router.post("/mutant")
async def detect_mutant(dna: DNAVerificationModel):
    """
    This endpoint receives a DNA sequence and checks if it is a mutant or not.
    the valus of the dna parameter must be a list of strings with the same length.
    and matrix must be NxN
    """
    document = {"dna": str(dna.dna), "is_mutant": is_mutant(dna.dna)}
    

    repository = DNARepository()
    result = repository.save_person(document=document)

    if result:
        if document["is_mutant"]:
            message = "Mutant detected"
            response = {"status_code": 200, "detail": message}
            return response
        else:
            message = "Forbidden"
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=message)
    else:
        logger.error("Internal Server Error")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/stats")
async def get_stats():
    repository = DNARepository()
    return repository.get_stats()

@router.get("/health")
async def health():
    """
    This endpoint is used to check the health of the API
    """
    return {"status": "ok"}

