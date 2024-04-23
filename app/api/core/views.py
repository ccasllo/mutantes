from fastapi import APIRouter, HTTPException
from app.api.core.models import DNAVerificationModel
from app.api.core.helper import isMutant
from app.api.core.repositories.dna_repository import DNARepository

router = APIRouter()

@router.post("/mutant")
async def detect_mutant(dna: DNAVerificationModel):
    document = {"dna": str(dna.dna), "is_mutant": isMutant(dna.dna)}

    repository = DNARepository()
    result = repository.save_person(document=document)

    if document["is_mutant"]:
        message = "Mutant detected"
        status_code = 200
    else:
        message = "Forbidden"
        status_code = 403

    if result:
        return {"message": message}, status_code
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/stats")
async def get_stats():
    repository = DNARepository()
    return repository.get_stats()
