from fastapi import APIRouter, HTTPException, status
from app.api.core.models import DNAVerificationModel, DNAStatsModel
from app.api.core.utils import is_mutant
from app.api.core.repositories.dna_repository import DNARepository
from config.logger import logger

router = APIRouter()

@router.post("/mutant")
async def detect_mutant(dna: DNAVerificationModel):
    """
    Detect whether a person is mutant based on their DNA sequence. the valus of the dna parameter must be a list of strings with the same length.
    and matrix must be NxN

    Args:
        dna (DNAVerificationModel): A JSON object containing the DNA sequence to be verified.

    Returns:
        int: HTTP status code 200 if the DNA sequence belongs to a mutant, otherwise 403.

    Explanation:
        This endpoint accepts a POST request with a JSON payload containing a DNA sequence to be verified. The DNA sequence should be provided in an array format as follows:
        {
            "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        }

        If the provided DNA sequence belongs to a mutant, the endpoint returns HTTP status code 200 (OK). Otherwise, it returns HTTP status code 403 (Forbidden).

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
    """
    Retrieve DNA verification statistics.

    Returns:
        dict: A JSON object containing the statistics of DNA verifications.

    Explanation:
        This endpoint exposes a service to retrieve statistics about DNA verifications. It returns a JSON object with the following structure:
        {
            "count_mutant_dna": 40,
            "count_human_dna": 100,
            "ratio": 0.4
        }
        
        - "count_mutant_dna": Represents the total number of mutant DNA sequences detected.
        - "count_human_dna": Represents the total number of human DNA sequences detected.
        - "ratio": Represents the ratio of mutant DNA sequences to human DNA sequences.
    """
    repository = DNARepository()
    stats_data = repository.get_stats() 
    return DNAStatsModel(**stats_data)

@router.get("/health")
async def health():
    """
    This endpoint is used to check the health of the API
    """
    return {"status": "ok"}

